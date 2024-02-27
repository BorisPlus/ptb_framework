from telegram import Update
from telegram.ext import CallbackContext

from handlers.replicas_says.dialogs.handler import handler as replica_handler
from bot_interface import DialogueBotInterface


async def handler(update: Update, context: CallbackContext):
    vise_versa: DialogueBotInterface = context.application.vise_versa
    if update.message.chat.id in vise_versa.dialogs:
        try:
            replica = vise_versa.dialogs[update.message.chat.id].send(update)
            await replica_handler(
                update,
                context,
                replica
            )
        except StopIteration:
            stop_dialogue(vise_versa, update.message.chat.id)
        return


async def start_dialogue(update: Update,
                         context: CallbackContext,
                         dialogue_function,
                         *dialogue_function_args):
    vise_versa: DialogueBotInterface = context.application.vise_versa
    vise_versa.dialogs[update.message.chat.id] = dialogue_function(
        *dialogue_function_args
    )
    _ = next(vise_versa.dialogs[update.message.chat.id])
    await handler(update, context)


def stop_dialogue(vise_versa: DialogueBotInterface, user_id: int):
    if user_id in vise_versa.dialogs:
        del vise_versa.dialogs[user_id]
