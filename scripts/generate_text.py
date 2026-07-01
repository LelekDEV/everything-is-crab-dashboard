# generate_text.py:

# Generates an image from text (generate_text) or a set of characters (generate_chars_from_text).
# This is done so text on the dashboard is displayed via images, which allows for perfect crispiness
# (a thing that cannot be done with pure HTML5/CSS text as a known limitation).

# However it doesn't actually get called from the site, but all the needed assets (as of now)
# are stored in dynamic_assets/chars.
# If you somehow accidentally deleted these assets simply run the script manually


from PIL import Image, ImageDraw, ImageFont
from os import path

CHARS_PATH = '..\\dynamic_assets\\chars'

def generate_text(text, color, save_path):
	font = ImageFont.truetype('..\\m6x11plus.ttf', 64)

	tmp = Image.new('RGB', (1, 1))
	draw = ImageDraw.Draw(tmp)

	bbox = draw.textbbox((0, 0), text, font = font)

	width = bbox[2] - bbox[0]
	height = bbox[3] - bbox[1]

	img = Image.new('RGBA', (width, height))
	draw = ImageDraw.Draw(img)

	draw.fontmode = '1'

	draw.text((-bbox[0], -bbox[1]), text, font = font, fill = color)

	img.save(f'{save_path}.png')

def generate_chars_from_text(text, color, save_path):
	chars = set(char for char in text)
	chars.remove(' ')

	for char in chars:
		filename = f'{char.lower()}_u' if char.isupper() else char
		generate_text(char, color, path.join(save_path, filename))

#generate_text('Everything is Crab - creature dashboard', (255, 255, 255))
generate_chars_from_text('Everything is Crab - creature dashboard', (255, 255, 255), CHARS_PATH)