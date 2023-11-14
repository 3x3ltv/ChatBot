from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
from telegram import Location

# Замените 'YOUR_BOT_TOKEN' на фактический токен вашего бота
TOKEN = '6721006067:AAEpHivlsux5MYKh49UdWdrNC9KGwFT5nGQ'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Этот бот реагирует на отправленную геолокацию.')

def location_handler(update: Update, context: CallbackContext) -> None:
    user_location = update.message.location
    latitude = user_location.latitude
    longitude = user_location.longitude

    # Пример: создаем текстовое сообщение на основе координат
    response_message = f'Вы находитесь на координатах: {latitude}, {longitude}'

    update.message.reply_text(response_message)

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Обработка команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Обработка геолокации
    dispatcher.add_handler(MessageHandler(filters.Location, location_handler))

    # Запускаем бота
    updater.start_polling()

    # Ожидаем завершение работы бота (например, нажатие Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()
