# Фреймворк для Телеграм-ботов

Получилось субъективно хорошо и гибко. Не претендуя на догму, делюсь наработками, надеясь, что будет полезно.

## Посыл

Обработка сообщений (или команд) в одной функции-обработчике приводит к ее росту и снижению наглядности. Ветвистая портянка из `if ... elif ... elif ... elif ... else ...` очень и очень не читабельна.

Я смастерил для себя что-то типа фреймворка для конструирования Телеграм-ботов, основанного на пакете `python-telegram-bot` и подходе динамического импорта `importlib.import_module()`.

## Запуск примера

Введите свой токен в `project/configs/config.ini` и запустите:

```shell
cd project
bin/python3.11 ./project/bot/main.py -c ./project/configs/config.ini
```

Команда вызова мануала - `/manual`.

## Новая команда

Для ввода новой команды нужно сделать один файлик в папке `bot/handlers/command_calls/actions` строгого вида:

```python
from telegram import Update
from telegram.ext import CallbackContext

async def call(update: Update,
               context: CallbackContext):
    ...
```

## Новая логика взаимодействия

Мне симпатизирует логика взаимодействия с пользователем на основе диалога <https://habr.com/ru/articles/316666/> (как последовательности yield-реплик).

Так, для разработки диалога нужно создать файл в папке `bot/dialogs` с функцией строгого вида:

```python

def dialog_rectangle():
    _ = yield ''  # Строка обязательна. Фича.
    ... = yield from ...
    ... = yield from ...
    yield ...

```

При этом диалог состоит из формализованных реплик `bot/dialogs/replicas`, потсупающих от Телеграм-бота. Каждая такая реплика "рисуется" по-своему.

В примере реплика `bot/dialogs/replicas/image_with_caption.py`:

```python
class ImageWithCaption(DialogReplica):
    image_file_path: str
    caption: str
    ...
```

состоит из картинки и подписи к ней.

И для ее "отрисовки" при ее возникновении в рамках АБСОЛЮТНО любого диалога реализованы файл и строгого вида функция реакции `bot/handlers/replicas_says/dialogs/replicas/image_with_caption.py`:

```python
from telegram import Update
from telegram.ext import CallbackContext

from dialogs.replicas import ImageWithCaption


async def say(update: Update,
              context: CallbackContext,
              replica: ImageWithCaption):
    await context.application.bot.send_photo(
        chat_id=update.message.chat.id,
        photo=open(replica.image_file_path, 'rb'),
        caption=replica.caption
    )
```

То есть конструируете диалог из таких вот `yield` и формализуете вид отдельных реплик диалога (того - что должно печататься ботом, исходя из этой реплики). Но `snake_case`-имена файлов реплик должны соответствовать `CamelCase`-названиям классов (это тоже зашито в "магию" фреймворка).

## Кнопки

Если Телеграм-бот не отслеживает, что шлет ему пользователь посредством нажатия на инлайн-кнопку, то это может привести к непредвиденному событию.

В статье <https://github.com/python-telegram-bot/python-telegram-bot/wiki/Arbitrary-callback_data#security-of-inlinekeyboardbuttons> приводится возможность удаления иного сообщения Телеграм-бота, вовсе не того, чей идентификатор "зашит" в кнопку удаления.

Одним из способов недопущения - передача в кнопке вместе с параметризованной командой ее цифровой подписи, сформированной ботом. При нажатии клиентом на кнопку перед исполнением боту необходимо проверить цифровую подпись от планируемого вызова, сравнив с уже зашитым в кнопку образцом.

Стоит учитывать, что "цифровая" подпись в таком вызове отнимет место у "зашиваемого" в кнопку запроса, ограниченного 64 байтами.

Кнопки исполнены также в строгой форме, например, `bot/ui/buttons/rectangle_perimeter.py`:

```python
import typing

from ui.buttons.base import CallbackDataButton


class RectanglePerimeter(CallbackDataButton):
    action: str = "rectangle_perimeter"
    title: str = "Рассчитать периметр прямоугольника"
    length: int
    width: int

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def get_callback_data(self) -> typing.Tuple[str]:
        return f"{self.length}", f"{self.width}"
```

как и обработчики их нажатия `bot/handlers/buttons_clicks/actions/rectangle_perimeter.py`:

```python
from telegram import Update

from ui.buttons import decode


async def click(update: Update, _):
    _, length, width, _ = decode(update.callback_query.data)
    length = int(length)
    width = int(width)
    await update.callback_query.message.reply_text(
        "P = %d" % (2*(length+width))
    )
```

## Фишка

В боте есть ссылка на самого себя

```python
    # обратная ссылка дает возможность доступа ко внутренней
    # структуре (конфигурация, база данных и пр.)
    self.application.vise_versa = self
```

Таким образом, из люого места

в обработчиках команд:

```python
async def call(update: Update,
               context: CallbackContext):
    ...
```

в обработчиках реплик:

```python
async def say(update: Update,
              context: CallbackContext,
              replica: DialogReplica):
    ...
```

в обработчиках кнопок:

```python
async def click(update: Update,
              context: CallbackContext):
    ...
```

есть доступ к внутренности Телеграм-бота:

```python
    vise_versa: DialogueBotInterface = context.application.vise_versa
    ...
```

В примере выше этот подход продемонстрирован на доступе к конфигурации:

```python
    secret = vise_versa.config.secret
    ...
```

При развитии Телеграм-бота это может быть, например, дексриптор соединения с базой данных:

```python
    dataset = vise_versa.db.select_data()
    ...
```

## Послесловие

Всем добра.
