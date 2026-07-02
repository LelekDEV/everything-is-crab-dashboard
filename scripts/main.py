# main.py:

# Controller script, calls creatures.py and components.py.

# Called from index.php when cheksums (sorted normalized directory names) don't match in local and remote
# As of now, the checksums are only based on creatures and not evolutions,
# so if they were to get desynced somehow, your best bet would be to clear assets of both


from os import fsencode, listdir, path, getcwd, chdir

if path.split(getcwd())[-1] != 'scripts':
	chdir('scripts')

from creatures import fetch_creatures
from evolutions import fetch_evolutions

fetch_creatures()
fetch_evolutions()
