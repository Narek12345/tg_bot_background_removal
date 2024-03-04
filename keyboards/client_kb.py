from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class RegisterKB:
	register_but = InlineKeyboardButton('Пройти регистрацию', callback_data="register")

	register_kb = InlineKeyboardMarkup().add(register_but)
