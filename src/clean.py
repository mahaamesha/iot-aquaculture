# Run this program on linux to delete some folder

import os

target = [
	'test/',
	'img/',
	'img_captured/'
]

def clean(list_dir=target, isLinux=True):
	working_path = os.path.dirname(__file__)    # in src/
	project_path = os.path.join(working_path, '../')    # in iot-aquaculture/

	for dir in list_dir:
		dir_path = os.path.join(project_path, dir)

		if isLinux:
			os.system('sudo rm -rf %s' %dir_path)
		else:	# for windows
			dir_path = dir_path.replace('/', '\\')
			os.system('cmd /c "rmdir /s /q %s"' %dir_path)
	print('Delete target directory ... Done')

if __name__ == '__main__':
	clean(isLinux=False)