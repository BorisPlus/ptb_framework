from telegram import Update

from ui.buttons import decode


async def click(update: Update, _):
    _, radius, _ = decode(update.callback_query.data)
    radius = int(radius)
    await update.callback_query.message.reply_text(
        "S = %d" % (3.14*radius*radius)
    )
