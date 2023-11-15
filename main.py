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
        {"name": "Петропавловская крепость", "text": "Заложенная ещё в далёком 1703 году, фортеция сегодня представляет собой музейных комплекс. В его в состав входят, например, музеи: «Тюрьма Трубецкого бастиона», истории, денег, – а также царская усыпальница, \nвеличественный Петропавловский собор с золочённым шпилем, давно ставшим символом Санкт-Петербурга", "latitude": 59.950186, "longitude": 30.317488},
        {"name": "Дом Макса", "text": "Заложенная ещё в далёком 2013 году, он строился еще несколько лет. В 2017 году здесь стал проживать Максим", "latitude": 59.905536, "longitude": 30.312425},
        {"name": "Троицкая площадь", "text": "Эта, находящаяся неподалёку от Петропавловки, площадь является самой старой в Северной столице. В своё время она проектировалась как главная, а потому стало местом расположения зданий сената, таможни, рынка, первого петербургского трактира «Аустерия». \nВ её центре находился Троицкий собор, которому обсуждаемая площадь и обязана своим названием" , "latitude": 59.952754, "longitude": 30.325884},
        {"name": "Домик императора Петра I", "text": "Это самое старое в городе здание было возведено в 1703 году вблизи Петропавловки. Оно представляет собой небольшое одноэтажное четырёхкомнатное строение, не имеющее ничего общего с царскими резиденциями в привычном для нас понимании.\nВ середине XIX столетия вокруг домика был возведён защитный футляр из камня. Сегодня домик императора Петра I стал «приютом» для филиала Русского музея, в котором экспонируется уникальная коллекция личных вещей первого российского императора.", "latitude": 59.953316, "longitude": 30.330841},
    ]

    closest_location = None
    min_distance = float('inf')
    59.910924, 30.314822
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

    # Возвращаем ответ с учетом ближайшей локации
    update.message.reply_text(f'Ближайшее место: {closest_location} Вот немного истории: {closest_text}')

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
