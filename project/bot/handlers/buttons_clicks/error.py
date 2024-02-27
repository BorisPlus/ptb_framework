from telegram import Update


async def click(update: Update, _):
    await update.callback_query.message.reply_text(
        "Не найден обработчик кнопки или возникло иное исключение"
    )
