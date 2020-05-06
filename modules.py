import os
import sys
from os import listdir
from os.path import isfile, join

import json

subfolders = [ f.path for f in os.scandir('.') if f.is_dir() ]
config = []
files = {}

for folder in subfolders:
	for file in [f for f in listdir(folder) if isfile(join(folder, f))]:
		if not file[0] == '.':
			print(file)
		


print(subfolders)
