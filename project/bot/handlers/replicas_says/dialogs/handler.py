from telegram import Update
from telegram.ext import CallbackContext
import importlib

from dialogs.replicas.base import DialogReplica
from .error import say as error_say


async def handler(update: Update,
                  context: CallbackContext,
                  replica: DialogReplica):
    try:
        action = importlib.import_module(
            f'handlers.replicas_says.dialogs.replicas.{replica.view()}'
        )
        await action.say(
            update,
            context,
            replica
        )
    except Exception as e:
        await error_say(
            update,
            context,
            replica
        )
