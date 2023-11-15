from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler

# Замените 'YOUR_TOKEN' на реальный токен вашего бота
TOKEN = '6721006067:AAEpHivlsux5MYKh49UdWdrNC9KGwFT5nGQ'
# Add this decorator
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот. Чем могу помочь?')

# Add this decorator
def handle_text_message(update: Update, context: CallbackContext) -> None:
    try:
        user_message = update.message.text.lower()
        if user_message == 'привет':
            update.message.reply_text('Привет!')
        elif user_message == 'как дела':
            update.message.reply_text('У меня все отлично, спасибо! А у тебя?')
        else:
            update.message.reply_text('Я не понимаю тебя :(')
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Add this decorator
def handle_location(update: Update, context: CallbackContext) -> None:
    try:
        location = update.message.location
        latitude = location.latitude
        longitude = location.longitude
        update.message.reply_text(f'Твои координаты: {latitude}, {longitude}')
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main() -> None:
    try:
        updater = Updater(TOKEN)
        dp = updater.dispatcher

        # Обработчики команд
        dp.add_handler(CommandHandler("start", start))

        # Обработчик текстовых сообщений
        dp.add_handler(MessageHandler(filters=filters.TEXT & ~filters.COMMAND, callback=handle_text_message))

        # Обработчик геолокации
        dp.add_handler(MessageHandler(filters=filters.LOCATION, callback=handle_location))

        updater.start_polling()
        updater.idle()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
