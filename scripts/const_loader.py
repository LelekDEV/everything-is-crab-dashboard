# const_loader.py:

# Loads consts from consts.json to be used in both Python and PHP files.

# Change root_path in consts.json to match your game files path


from json import load

with open('../consts.json', 'r') as file:
	consts = load(file)

ROOT_PATH = consts['root_path'].encode('utf-8')
