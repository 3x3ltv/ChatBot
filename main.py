from scipy.spatial import KDTree
from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
import io
from base_coordinates import base_coordinates

TOKEN = '6721006067:AAEpHivlsux5MYKh49UdWdrNC9KGwFT5nGQ'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я Знаток Петроградской стороны Петербурга. Чтобы получить информацию о ближайшем историческом здании к вам, просто пришлите мне свою геолокацию!')

def handle_text_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text.lower()
    if user_message == 'Привет':
        update.message.reply_text('Привет!')
    else:
        update.message.reply_text('Я не понимаю тебя :(')

base_coords_tree = KDTree([(coord["latitude"], coord["longitude"]) for coord in base_coordinates])

def handle_location(update: Update, context: CallbackContext) -> None:
    location = update.message.location
    latitude = location.latitude
    longitude = location.longitude

    # Используем k-d дерево для поиска ближайшей локации
    _, index = base_coords_tree.query((latitude, longitude))

    closest_location = base_coordinates[index]["name"]
    closest_text = base_coordinates[index]["text"]
    image_url = base_coordinates[index]["URL_link"]

    if image_url:
        # Отправка изображения по URL
        image_data = requests.get(image_url).content
        update.message.reply_photo(photo=InputFile(io.BytesIO(image_data)), caption=f'Ближайшее место это: {closest_location}. Вот немного его истории: {closest_text}')
    else:
        update.message.reply_text(f'Ближайшее место это: {closest_location}. Вот немного его истории: {closest_text}')


def main() -> None:
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Обработчики команд
    dp.add_handler(CommandHandler("start", start))

    # Обработчик текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text_message))

    # Обработчик геолокации
    dp.add_handler(MessageHandler(Filters.location, handle_location))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
