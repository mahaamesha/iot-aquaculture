# Run this program on linux to delete some folder

import os

target = [
	'test/',
	'img/',
	'img_captured/'
]

def clean(list_dir=target):
	working_path = os.path.dirname(__file__)    # in src/
	project_path = os.path.join(working_path, '../')    # in iot-aquaculture/

	for dir in list_dir:
		dir_path = os.path.join(project_path, dir)

		try:
			os.system('sudo rm -rf %s' %dir_path)
		except:
			print('Error: run this program in linux')

if __name__ == '__main__':
	clean(list_dir=target)