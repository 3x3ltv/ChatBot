from telegram.ext import Updater, MessageHandler, CommandHandler
from telegram import Location
import logging

# Установка уровня логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = '6721006067:AAEpHivlsux5MYKh49UdWdrNC9KGwFT5nGQ'

# Создание объектов Updater и Dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Обработчик команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Отправь мне свою геолокацию.")

# Обработчик геолокации
def location_handler(update, context):
    user_location = update.message.location
    latitude = user_location.latitude
    longitude = user_location.longitude

    # Пример: создаем текстовый ответ на основе геолокации
    response_text = f"Ты находишься на широте {latitude} и долготе {longitude}."
    context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)

# Добавление обработчиков команд и геолокации
start_handler = CommandHandler('start', start)
location_handler = MessageHandler(Filters.location, location_handler)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(location_handler)

# Запуск бота
updater.start_polling()
updater.idle()
