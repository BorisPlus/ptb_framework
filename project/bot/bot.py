from telegram.ext import (
    filters,
    ApplicationBuilder,
    MessageHandler,
    CallbackQueryHandler,
)

from config import Config
from handlers.replicas_says import handler as dialog_handler
from handlers.commands_calls import handler as command_handler
from handlers.buttons_clicks import handler as button_handler
from bot_interface import DialogueBotInterface


class DialogueBot(DialogueBotInterface):

    def __init__(self, config: Config):

        self.dialogs = dict()
        self.config = config

        self.application = ApplicationBuilder().token(
            self.config.token
        ).build()

        # обратная ссылка дает возможность доступа ко внутренней
        # структуре (конфигурация, база данных и пр.)
        self.application.vise_versa = self

        # вызовы команд - call()
        self.application.add_handler(
            MessageHandler(
                filters.COMMAND,
                command_handler.handler
            )
        )

        # вызовы реплик диалогов - say()
        self.application.add_handler(
            MessageHandler(
                filters.ALL,
                dialog_handler.handler
            )
        )

        # вызовы кнопок - click()
        self.application.add_handler(
            CallbackQueryHandler(
                button_handler.handler
            )
        )

    def start(self):
        self.application.run_polling()
