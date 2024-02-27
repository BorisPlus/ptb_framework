from telegram import Update
from telegram.ext import CallbackContext

from manual import call as manual_call


async def call(update: Update,
               context: CallbackContext):
    await manual_call(update, context)
