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

	for dir in target:
		dir_path = os.path.join(project_path, dir)

		list_file = os.listdir(dir_path)
		print(list_file)

		# Delete all files in dir_path
		for file_name in list_file:
			file_path = os.path.join(dir_path, file_name)
			try:
				os.remove(file_path)
			except: 
				print('Not found:', file_path)

if __name__ == '__main__':
	clean(list_dir=target)