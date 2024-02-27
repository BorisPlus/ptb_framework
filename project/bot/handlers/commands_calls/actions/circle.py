from telegram import Update
from telegram.ext import CallbackContext

from dialogs import dialog_circle
from handlers.replicas_says.handler import start_dialogue


async def call(update: Update,
               context: CallbackContext):
    await start_dialogue(
        update,
        context,
        dialog_circle
    )
