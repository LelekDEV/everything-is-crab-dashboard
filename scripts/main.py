# main.py:

# Controller script, calls creatures.py and components.py.

# Called from index.php when cheksums (sorted normalized directory names) don't match in local and remote
# As of now, the checksums are only based on creatures and not evolutions,
# so if they were to get desynced somehow, your best bet would be to clear assets of both


from creatures import fetch_creatures
from evolutions import fetch_evolutions

from os import fsencode, listdir, path, getcwd, chdir

if getcwd().split('\\')[-1] != 'scripts':
	chdir('scripts')

ROOT_PATH = b'C:\\Users\\Euro\\Pictures\\Everything is Crab'

fetch_creatures()
fetch_evolutions()
