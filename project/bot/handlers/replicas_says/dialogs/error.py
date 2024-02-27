from telegram import Update


async def say(update: Update, _, __):
    await update.message.reply_text(
        "Не найден обработчик реплики или возникло иное исключение"
    )
