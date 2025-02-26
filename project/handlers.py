from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from project.services import crud


# Это файл обработчиков

# Добро пожаловать
async def welcome(message: Message) -> None:
    await crud.add_gamer(message)


# Начать викторину
async def start_quiz(message: Message) -> None:
    await crud.get_question(message.from_user.id, message)


# Показать результаты
async def show_result(message: Message) -> None:
    await crud.get_result(message.from_user.id, message)


# Показать записи таблицы
async def show_table_records(message: Message) -> None:
    await crud.get_table_records(message)


# Новая игра
async def new_game(message: Message) -> None:
    await crud.reset_result(message.from_user.id, message)


# Обновляет счёт в БД
async def right_answer(message: Message) -> None:
    await crud.add_point(message.from_user.id, message)


# Ошибочный ответ
async def wrong_answer(message: Message) -> None:
    await crud.next_question(message.from_user.id, message)


# Когда пользователь ввёл неправильную опцию работы Telegram
async def random_text_handler(message: Message) -> None:
    await message.answer('Нет такого варианта')


# Регистрация обработчиков
def register_handlers(dispatcher: Dispatcher) -> None:
    # Слева в скобках обработчик, справа - команда обработчика
    dispatcher.register_message_handler(welcome, commands=['start'])
    dispatcher.register_message_handler(start_quiz, Text(['Начать викторину', 'go', 'Да']))
    dispatcher.register_message_handler(right_answer, right_answer=True)
    dispatcher.register_message_handler(wrong_answer, in_answer_options=True)
    dispatcher.register_message_handler(show_result, Text(['Показать результат', "results"]))
    dispatcher.register_message_handler(show_table_records, Text(['Показать таблицу рекордов', 'table']))
    dispatcher.register_message_handler(new_game, Text(['Сыграть заново', 'restart']))
    dispatcher.register_message_handler(random_text_handler)
