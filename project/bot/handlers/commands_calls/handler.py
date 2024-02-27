import importlib

from telegram import Update
from telegram.ext import CallbackContext

from handlers.commands_calls import error


async def handler(update: Update,
                  context: CallbackContext):
    action = update.message.text[1:]
    try:
        command = importlib.import_module(
            f'handlers.commands_calls.actions.{action}'
        )
        await command.call(
            update,
            context,
        )
    except Exception as e:
        await error.call(
            update,
            context,
        )
