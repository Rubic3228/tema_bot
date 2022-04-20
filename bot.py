from telegram.ext import MessageHandler, ConversationHandler, CommandHandler, \
    Filters, Updater, CallbackContext
from telegram import Update, ReplyKeyboardMarkup
from key import TOKEN


WAIT_NAME, WAIT_SEX, WAIT_GRADE = range(3)

sex_keyboard = [
    ["М", "Ж"]
]


def main():
    updater = Updater(
        token=TOKEN,
        use_context=True
    )
    dispatcher = updater.dispatcher

    meet_handler = ConversationHandler(
        entry_points=[CommandHandler('True', meet)],

        states={
            WAIT_NAME: [MessageHandler(Filters.text, ask_sex)],
            WAIT_SEX: [MessageHandler(Filters.text, ask_grade)],
            WAIT_GRADE: [MessageHandler(Filters.text, greed)]
        },
        fallbacks=[MessageHandler(Filters.text("cancel"), cancel)]
    )

    dispatcher.add_handler(meet_handler)

    updater.start_polling()
    print("Бот запущен")
    updater.idle()


def meet(update: Update, context: CallbackContext):
    """Начинает диалог получения данных пользователя


    :param update:
    :param context:
    :return:
    """
    update.message.reply_text(
        'привет, ЧМО!'
    )
    context.user_data["user"] = {}
    return ask_name(update, context)


def ask_name(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Как тебя звать?'
    )
    return WAIT_NAME


def ask_sex(update: Update, context: CallbackContext):
    """
    TODO add keyboard
    TODO add validation
    :param update:
    :param context:
    :return:
    """
    message = update.message
    if not validate_name(message.text):
        message.reply_text(
            "Неверное имя!"
        )
        return WAIT_NAME

    context.user_data["user"]["name"] = message.text
    message.reply_text(
        "Выберите ваш пол",
        reply_markup=ReplyKeyboardMarkup(sex_keyboard, resize_keyboard=True)
    )
    return WAIT_SEX


def ask_grade(update: Update, context: CallbackContext):
    if not validate_sex(update.message.text):
        update.message.reply_text(
            "Ты ЧМО!\n"
            "Мы Русские у нас два пола!!1"
        )
        return WAIT_SEX
    return WAIT_GRADE


def greed(update: Update, context: CallbackContext):
    pass


def cancel(update: Update, context: CallbackContext):
    return ConversationHandler.END


def validate_name(name: str) -> bool:
    return True


def validate_sex(sex: str) -> bool:
    return sex in sex_keyboard[0]


if __name__ == '__main__':
    main()
