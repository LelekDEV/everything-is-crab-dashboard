# evolutions.py:

# Extracts evolution icons from the remote folder.
# Called when needed through index.php -> main -> * this file *


from const_loader import ROOT_PATH

from PIL import Image
from os import fsencode, listdir, path, makedirs, getcwd

class Scan:
	SCANNING = 0
	SCANNED = 1
	EMPTY = 2

def generate_evolution_icons(img_path, dir_path, abs_path):
	with Image.open(fsencode(path.join(abs_path, img_path))) as img:
		if not path.isdir(dir_path):
				makedirs(dir_path)

		resized = img.convert('RGBA').resize((480, 270), Image.Resampling.NEAREST)

		for y_idx in range(5):
			for x_idx in range(11):
				pos_x = 18 + x_idx * 40
				pos_y = 35 + y_idx * 42
				cropped = resized.crop((pos_x, pos_y, pos_x + 37, pos_y + 39))

				state = Scan.SCANNING

				for x in range(cropped.size[0]):
					for y in range(cropped.size[1]):
						pos = (x, y)

						if not cropped.getpixel(pos) in [(237, 201, 125, 255), (229, 173, 133, 255)]:
							state = Scan.SCANNED
							break

						state = Scan.EMPTY

					if state != Scan.SCANNING:
						break

				match state:
					case Scan.SCANNED:
						for x in range(cropped.size[0]):
							for y in range(cropped.size[1]):
								pos = (x, y)

								if cropped.getpixel(pos) in [(237, 201, 125, 255), (229, 173, 133, 255)]:
									cropped.putpixel(pos, (0, 0, 0, 0))

						cropped.save(path.join(dir_path, f'{x_idx + y_idx * 11}.png'))

					case Scan.EMPTY:
						return
def fetch_evolutions():
	for rel_path in listdir(fsencode(ROOT_PATH)):
		abs_path = path.join(ROOT_PATH, rel_path)

		if path.isdir(abs_path):
			b_num = rel_path.split(b'#')[-1]
			num = b_num.decode('utf-8')

			img_path = f'Evolutions #{num}.png'.encode('utf-8')
			dir_path = f'../dynamic_assets/evolutions/e_{num}'

			generate_evolution_icons(img_path, dir_path, abs_path)
