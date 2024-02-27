import hashlib
import typing
from telegram import InlineKeyboardButton
from abc import (
    abstractmethod,
    ABC
)


class CallbackDataButton(ABC):
    title: str
    action: str

    @abstractmethod
    def get_callback_data(self) -> typing.Tuple[str]:
        ...

    def as_button(self, secret: str) -> InlineKeyboardButton:
        return InlineKeyboardButton(
            self.title,
            callback_data=encode_with_sign(
                secret,
                self.action,
                *self.get_callback_data()
            )
        )


__DELIM = "|"


def sign(secret: str, callback_data: str) -> str:
    return hashlib.md5(f"{callback_data}{secret}".encode()).hexdigest()


def check_signature(callback_data_with_signature: str, secret: str) -> bool:
    *callback_data_without_signature, signature = callback_data_with_signature.split(__DELIM)
    if sign(secret, __DELIM.join(callback_data_without_signature)) == signature:
        return True
    return False


def encode(*args: str) -> str:
    return __DELIM.join([str(arg) for arg in args])


def encode_with_sign(secret: str, *args: str) -> str:
    callback_data_without_signature = encode(*args)
    signature = sign(secret, callback_data_without_signature)
    return encode(callback_data_without_signature, signature)


def decode(callback_data_with_signature: str) -> typing.List[str]:
    return callback_data_with_signature.split(__DELIM)


def fetch_action(callback_data: str) -> str:
    action, _ = callback_data.split(__DELIM, 1)
    return action


def fetch_signature(callback_data_with_signature: str) -> str:
    *_, signature = callback_data_with_signature.split(__DELIM)
    return signature
