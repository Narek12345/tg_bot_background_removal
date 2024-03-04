import io
import secrets
import requests

from PIL import Image

from config import BOT_TOKEN

URI_INFO = f'https://api.telegram.org/bot{BOT_TOKEN}/getFile?file_id='
URI = f'https://api.telegram.org/file/bot{BOT_TOKEN}/'


def download_photo(message):
	"""Обработка изображение."""
	try:
		file_id = message.photo[3].file_id
	except:
		try:
			file_id = message.photo[2].file_id
		except:
			try:
				file_id = message.photo[1].file_id
			except:
				try:
					file_id = message.photo[0].file_id
				except:
					pass

	resp = requests.get(URI_INFO + file_id)
	img_path = resp.json()['result']['file_path']
	img = requests.get(URI + img_path)

	# Открываем файн.
	img = Image.open(io.BytesIO(img.content))

	# Сохраняем файл.
	img_name = secrets.token_hex(8)
	path_to_img = f'images/processing/{img_name}.png'
	img.save(path_to_img, format='PNG')

	return (path_to_img, img_name)