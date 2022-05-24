from picamera import PiCamera
from time import sleep
import os


def set_target_path(path='img_captured/'):
#def set_target_path(path='../fish-length-opencv/img/'):
	# projects/
	# 	iot_aquaculture/
	#		img_captured/	>> use this as test
	#		camera.py
	#	fish-length-opencv/
	#		img/			>> use this as final
	working_path = os.path.dirname(__file__)	# Find path of this file
	path = os.path.join(working_path, path)		# I want to save the captured img in this path
	return path

# Delete all old files in path folder
def empty_folder(path):
	for f in os.listdir(path):
		os.remove(os.path.join(path, f))

def main():
	camera = PiCamera()

	camera.rotation = 0     # Rotatae: 0, 90, 180, 270
	camera.start_preview(alpha=200) # Make the preview slightly see-through. 0 - 255
	camera.resolution = (1024, 768)

	camera.start_preview()
	camera.brightness = 70  # 0 - 100, default 50
	camera.contrast = 50    # 0 - 100, default 50
	camera.image_effect = 'none'    # default 'none'
	camera.exposure_mode = 'sports' # default 'auto'
	camera.awb_mode = 'sunlight'    # default 'auto'

	# Delete old files in img/ folder
	path = set_target_path(path='img_captured/')
	#path = set_target_path(path='../fish-length-opencv/img/')
	empty_folder(path=path)

	# To capture repeatedly until n repetition
	for i in range(3):
		sleep(2)    # preview the camera for n secondsi
		# save captured image as 0.jpg, 1.jpg, ..., 4.jpg
		camera.capture(path + '%s.jpg' % i)
	camera.stop_preview()

	print('Run camera.py ... Done' )


if __file__ == '__main__':
	main()