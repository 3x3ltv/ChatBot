from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
import io
from base_coordinates import base_coordinates

TOKEN = '6721006067:AAEpHivlsux5MYKh49UdWdrNC9KGwFT5nGQ'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я Знаток Петроградской стороны Петербурга. Чтобы получить информаию о ближайшем историческом здании к вам, просто пришлите мне свою геолокацию!')

def handle_text_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text.lower()
    if user_message == 'привет':
        update.message.reply_text('Привет!')
    else:
        update.message.reply_text('Я не понимаю тебя :(')

def handle_location(update: Update, context: CallbackContext) -> None:
    location = update.message.location
    latitude = location.latitude
    longitude = location.longitude

    closest_location = None
    min_distance = float('inf')
    for base_coord in base_coordinates:
        base_latitude = base_coord["latitude"]
        base_longitude = base_coord["longitude"]

        # Рассчитываем расстояние между базовой точкой и точкой пользователя
        distance = ((latitude - base_latitude)**2 + (longitude - base_longitude)**2)**0.5

        # Если расстояние меньше, чем минимальное до этого, обновляем ближайшую локацию
        if distance < min_distance:
            min_distance = distance
            closest_location = base_coord["name"]
            closest_text = base_coord["text"]
            image_url = base_coord["URL_link"]

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
