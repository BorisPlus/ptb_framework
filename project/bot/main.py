from configparser import ConfigParser
from optparse import OptionParser

from config import Config
import bot


def main(config: Config):
    try:
        dialog_bot = bot.DialogueBot(config)
        dialog_bot.start()
    except Exception as e:
        raise e


if __name__ == "__main__":
    usage = "usage: %prog -c/--config config.ini"

    option_parser = OptionParser(usage)
    option_parser.add_option(
        "-c", "--config", dest="config", default='config.ini',
        help="Config ini-file")
    (options, args) = option_parser.parse_args()

    config_parser = ConfigParser()
    config_parser.read(options.config)

    bot_config = Config(
        token=config_parser.get('bot', 'token'),
        secret=config_parser.get('bot', 'secret'),
    )

    main(bot_config)
