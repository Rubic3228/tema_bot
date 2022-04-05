from telegram.ext import MessageHandler, ConversationHandler, CommandHandler, \
    Filters, Updater, CallbackContext
from telegram import Update
from key import TOKEN


WAIT_NAME, WAIT_SEX, WAIT_GRADE = range(3)


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

    dispatcher.add_hander(meet_handler)

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
    return ask_name(update, context)


def ask_name(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Как тебя звать?'
    )
    return WAIT_NAME


def ask_sex(update: Update, context: CallbackContext):
    pass


def ask_grade(update: Update, context: CallbackContext):
    pass


def greed(update: Update, context: CallbackContext):
    pass


def cancel(update: Update, context: CallbackContext):
    return ConversationHandler.END


if __name__ == '__main__':
    main()
