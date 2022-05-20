from picamera import PiCamera
from time import sleep

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

# To capture repeatedly until 5 repetition
path = '../img_captured/'
for i in range(5):
    sleep(2)    # preview the camera for n secondsi
    # save captured image as 0.jpg, 1.jpg, ..., 4.jpg
    camera.capture(path + '%s.jpg' % i)
camera.stop_preview()

print( str('Run camera.py').ljust(37,'.') + str('Done').rjust(5,' '), end='\n\n' )