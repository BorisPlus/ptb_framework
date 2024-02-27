from telegram import Update

from ui.buttons import decode


async def click(update: Update, _):
    _, length, width, _ = decode(update.callback_query.data)
    length = int(length)
    width = int(width)
    await update.callback_query.message.reply_text(
        "S = %d" % (length*width)
    )
