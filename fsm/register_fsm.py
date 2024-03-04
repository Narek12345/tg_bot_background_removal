from aiogram.dispatcher.filters.state import State, StatesGroup


class RegisterFSM(StatesGroup):
	last_name = State()
	first_name = State()
	sur_name = State()
	phone = State()
	role = State()
	photo = State()
