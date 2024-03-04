from rembg import remove
from PIL import Image


def removing_photo_background(photo_path, img_name):
	output_path = f'images/{img_name}.png'
	photo = Image.open(photo_path)
	output = remove(photo).save(output_path)
