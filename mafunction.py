import os

# Delete all old files in path folder
def empty_folder(path = 'fish-length-opencv/img/'):
	for f in os.listdir(path):
		os.remove(os.path.join(path, f))