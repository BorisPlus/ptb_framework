from telegram import Update


async def call(update: Update, _):
    await update.message.reply_text(
        "Не найден обработчик команды или возникло иное исключение"
    )
