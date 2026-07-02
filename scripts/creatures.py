# creatures.py:

# Extracts creature frame images from the remote folder.
# Applies operations such as background and text removal.
# Finally merges everything into new GIFs to be displayed.

# Called when needed through index.php -> main -> * this file *


from const_loader import ROOT_PATH

from PIL import Image, ImageDraw
from os import fsencode, listdir, path, getcwd, chdir

REMOVE_COLORS = [(255, 255, 253), (252, 170, 58), (241, 191, 132), (248, 171, 67), (232, 173, 95), (255, 239, 211), (255, 253, 237), (245, 170, 77), (255, 171, 49), (255, 253, 246), (255, 170, 53), (252, 195, 126), (255, 255, 255), (255, 238, 212), (255, 240, 212), (254, 255, 255), (244, 172, 74), (246, 170, 76), (255, 239, 213), (246, 191, 126), (255, 241, 213), (248, 170, 70), (255, 242, 227), (249, 169, 70), (254, 169, 50), (249, 170, 69), (245, 171, 74), (255, 239, 200), (255, 254, 243), (255, 253, 241), (255, 254, 246), (245, 171, 76), (245, 169, 83)]

def custom_floodfill(img, start, tc, rc, thresh):
	# those are the optimal data types
	visited = set()
	stack = [start]
	filled_pixels = []

	while stack:
		pos = stack.pop()

		if pos in visited:
			continue
		if pos[0] < 0 or pos[1] < 0 or pos[0] >= img.size[0] or pos[1] >= img.size[1]:
			continue
		
		c = img.getpixel(pos)
		if abs(c[0] - tc[0]) > thresh or abs(c[1] - tc[1]) > thresh or abs(c[2] - tc[2]) > thresh:
			continue

		visited.add(pos)
		filled_pixels.append(pos)

		img.putpixel(pos, rc)

		stack.append((pos[0] + 1, pos[1]))
		stack.append((pos[0] - 1, pos[1]))
		stack.append((pos[0], pos[1] + 1))
		stack.append((pos[0], pos[1] - 1))

	return filled_pixels

def fetch_creatures():
	for rel_path in listdir(fsencode(ROOT_PATH)):
		abs_path = path.join(ROOT_PATH, rel_path)

		if path.isdir(abs_path):
			num = rel_path.split(b'#')[-1]
			img_path = f'Creature #{num.decode('utf-8')}_Stills'.encode('utf-8')
			frames = []

			for img in listdir(fsencode(path.join(abs_path, img_path))):
				with Image.open(path.join(abs_path, img_path, img)) as img:
					SIZE = 32
					resized = img.convert('RGB').resize((SIZE, SIZE), Image.Resampling.NEAREST)
					colors = set()

					for x in range(SIZE):
						for y in range(min(SIZE, 4)):
							pos = (x, y)
							if resized.getpixel(pos) in REMOVE_COLORS:
								resized.putpixel(pos, (255, 170, 51))

					BG_COLOR = (255, 170, 51, 255)
					SHADOW_COLOR = (217, 146, 58, 255)

					transparent = resized.convert('RGBA')
					shadow_pixels = custom_floodfill(transparent, (16, 29), SHADOW_COLOR, BG_COLOR, 5)

					expanded = Image.new('RGBA', (SIZE + 2, SIZE + 2), BG_COLOR)
					expanded.paste(transparent, (1, 1))
					ImageDraw.floodfill(expanded, (0, 0), (0, 0, 0, 0), thresh = 50)

					cropped = expanded.crop((1, 1, SIZE + 1, SIZE + 1))

					for pos in shadow_pixels:
						cropped.putpixel(pos, SHADOW_COLOR)

					frames.append(cropped)

			frames[0].save(
				f'../dynamic_assets/creatures/c_{num.decode('utf-8')}.gif', 
				save_all = True, 
				append_images = frames[1:], 
				duration = 100, 
				loop = 0, 
				disposal = 2, 
				optimize = False
			)
