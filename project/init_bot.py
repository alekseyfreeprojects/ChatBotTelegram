import logging
from aiogram import Bot, Dispatcher
from decouple import config
from project import custom_filters, handlers

# Из конфигурации вытаскивает токен телеграмма
API_TOKEN = config('API_TOKEN')
# делает баховое конфигурирование логгирования
logging.basicConfig(level=logging.INFO)
# Создаёт бота
bot = Bot(token=API_TOKEN)
# Нужно чтобы обновлять данные бота
dispatcher = Dispatcher(bot)

# Регистрирует фильтры проверки правильного/неправильного ввода
custom_filters.register_filters(dispatcher)
# Регистрирует обработчики
handlers.register_handlers(dispatcher)
