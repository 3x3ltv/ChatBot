from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Замените 'YOUR_TOKEN' на реальный токен вашего бота
TOKEN = '6721006067:AAEpHivlsux5MYKh49UdWdrNC9KGwFT5nGQ'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот. Чем могу помочь?')

def handle_text_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text.lower()
    if user_message == 'привет':
        update.message.reply_text('Привет!')
    elif user_message == 'как дела':
        update.message.reply_text('У меня все отлично, спасибо! А у тебя?')
    else:
        update.message.reply_text('Я не понимаю тебя :(')

def handle_location(update: Update, context: CallbackContext) -> None:
    location = update.message.location
    latitude = location.latitude
    longitude = location.longitude
    update.message.reply_text(f'Твои координаты: {latitude}, {longitude}')

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
