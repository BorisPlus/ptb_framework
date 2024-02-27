from telegram import (
    Update,
    InlineKeyboardMarkup
)
from telegram.ext import CallbackContext

from dialogs.replicas.circle import Circle
from ui.buttons.circle_area import CircleArea
from ui.buttons.circle_length import CircleLength
from bot_interface import DialogueBotInterface


async def say(update: Update,
              context: CallbackContext,
              replica: Circle):
    vise_versa: DialogueBotInterface = context.application.vise_versa
    secret = vise_versa.config.secret
    await context.application.bot.send_message(
        chat_id=update.message.chat.id,
        text=str(replica),
        reply_markup=InlineKeyboardMarkup.from_column([
            CircleLength(replica.radius).as_button(secret),
            CircleArea(replica.radius).as_button(secret)
        ])
    )
