from aiogram import executor
from handlers import client, other
from create import dp

# Регистрируем все хэндлеры.
client.register_client_handlers(dp)
other.register_other_handlers(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)