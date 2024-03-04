import os

from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ContentType

from keyboards.client_kb import RegisterKB
from fsm.register_fsm import RegisterFSM
from create import bot, dp
from utils import ai, download_photo


async def start_cmd(message: Message):
	await message.answer("Здравствуйте! Я бот-помощник Российской Академии каратэдо Шотокан.\nЯ помогу Вам зарегестрироваться в качестве Судьи, Тренера-секунданта, Представителя команды или получить Аккредитацию для прессы на турнир и фестиваль «Кубок России по каратэ Шотокан» 24 марта 2024 года.", reply_markup=RegisterKB.register_kb)


async def register_cmd(query: CallbackQuery):
	await query.answer()
	# Запускаем FSM регистрации.
	await RegisterFSM.last_name.set()
	await query.message.answer('Введите пожалуйста фамилию:')


async def last_name(message: Message, state: FSMContext):
	async with state.proxy() as data:
		data['last_name'] = message.text
	await RegisterFSM.next()
	await message.answer('Введите пожалуйста имя:')


async def first_name(message: Message, state: FSMContext):
	async with state.proxy() as data:
		data['first_name'] = message.text
	await RegisterFSM.next()
	await message.answer('Введите пожалуйста отчество:')


async def sur_name(message: Message, state: FSMContext):
	async with state.proxy() as data:
		data['sur_name'] = message.text
	await RegisterFSM.next()
	await message.answer('Введите пожалуйста телефон:')


async def phone(message: Message, state: FSMContext):
	async with state.proxy() as data:
		data['phone'] = message.text
	await RegisterFSM.next()
	await message.answer('Выберите пожалуйста роль:')


async def role(message: Message, state: FSMContext):
	async with state.proxy() as data:
		data['role'] = message.text
	await RegisterFSM.next()
	await message.answer('Отправьте пожалуйста вашу фотографию:')


async def photo(message: Message, state: FSMContext):
	async with state.proxy() as data:
		# Сохраняем данные в CSV.
		pass
	# Сохраняем файл в папке images/processing.
	path_photo, img_name = download_photo.download_photo(message)
	# После сохранения файла отправляем в ИИ.
	ai.removing_photo_background(path_photo, img_name)
	await state.finish()
	await message.answer('Регистрация завершена!')
	# Удаляем файл из папки images/processing.
	os.remove(path_photo)



def register_client_handlers(dp):
	"""Регистрируем все клиентские хэндлеры."""
	dp.register_message_handler(start_cmd, commands='start')
	dp.register_callback_query_handler(register_cmd, text='register', state=None)
	dp.register_message_handler(last_name, state=RegisterFSM.last_name)
	dp.register_message_handler(first_name, state=RegisterFSM.first_name)
	dp.register_message_handler(sur_name, state=RegisterFSM.sur_name)
	dp.register_message_handler(phone, state=RegisterFSM.phone)
	dp.register_message_handler(role, state=RegisterFSM.role)
	dp.register_message_handler(photo, content_types=ContentType.PHOTO, state=RegisterFSM.photo)