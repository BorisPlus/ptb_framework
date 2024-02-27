from telegram import (
    Update,
    InlineKeyboardMarkup
) 
from telegram.ext import CallbackContext

from dialogs.replicas.rectangle import Rectangle
from ui.buttons.rectangle_area import RectangleArea
from ui.buttons.rectangle_perimeter import RectanglePerimeter
from bot_interface import DialogueBotInterface


async def say(update: Update,
              context: CallbackContext,
              replica: Rectangle):
    vise_versa: DialogueBotInterface = context.application.vise_versa
    secret = vise_versa.config.secret
    await context.application.bot.send_message(
        chat_id=update.message.chat.id,
        text=str(replica),
        reply_markup=InlineKeyboardMarkup.from_column([
            RectanglePerimeter(
                replica.length, replica.width).as_button(secret),
            RectangleArea(replica.length, replica.width).as_button(secret)
        ])
    )
