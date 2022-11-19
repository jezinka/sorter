import time
from picamera2 import Picamera2


def init_camera():
    picam2 = Picamera2()
    capture_config = picam2.create_still_configuration()
    picam2.start()
    time.sleep(1)
    return picam2, capture_config


def close_camera(picam2):
    picam2.stop()
    time.sleep(5)


def get_shot(picam2, capture_config, image_name):
    array = picam2.switch_mode_and_capture_array(capture_config, "main")
    picam2.capture_file(image_name)
    return array
