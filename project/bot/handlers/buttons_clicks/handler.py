import importlib

from telegram import Update
from telegram.ext import CallbackContext

from handlers.buttons_clicks import error
from bot_interface import DialogueBotInterface
from ui.buttons import (
    check_signature,
    fetch_action
)


async def handler(update: Update,
                  context: CallbackContext):
    query = update.callback_query
    await query.answer()
    vise_versa: DialogueBotInterface = context.application.vise_versa
    if not check_signature(query.data, vise_versa.config.secret):
        await context.application.bot.send_message(
            chat_id=update.callback_query.from_user.id,
            text="Неверная сигнатура кнопки"
        )
        return
    try:
        action = fetch_action(query.data)
        command = importlib.import_module(
            f'handlers.buttons_clicks.actions.{action}'
        )
        await command.click(
            update,
            context,
        )
    except Exception as e:
        await error.click(
            update,
            context,
        )
