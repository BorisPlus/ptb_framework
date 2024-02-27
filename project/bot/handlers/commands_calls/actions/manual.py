from telegram import Update


async def call(update: Update, _):
    await update.message.reply_text(
        "Рассчеты для:\n"
        "/circle - окружности\n"
        "/rectangle - прямоугольника\n"
    )
