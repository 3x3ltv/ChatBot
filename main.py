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

    # Базовые значения координат
    base_coordinates = [
        {"name": "Москва", "latitude": 55.7558, "longitude": 37.6176},
        {"name": "Санкт-Петербург", "latitude": 59.9343, "longitude": 30.3351},
        # Добавьте другие базовые значения координат при необходимости
    ]

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

    # Возвращаем ответ с учетом ближайшей локации
    update.message.reply_text(f'Твои координаты: {latitude}, {longitude}. Ближайшее место: {closest_location}')

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
