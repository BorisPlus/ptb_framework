from telegram import Update
from telegram.ext import CallbackContext

from dialogs.replicas.image_with_caption import ImageWithCaption


async def say(update: Update,
              context: CallbackContext,
              replica: ImageWithCaption):
    await context.application.bot.send_photo(
        chat_id=update.message.chat.id,
        photo=open(replica.image_file_path, 'rb'),
        caption=replica.caption
    )
