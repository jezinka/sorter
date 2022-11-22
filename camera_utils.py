import time
from picamera2 import Picamera2


def init_camera():
    picam2 = Picamera2()
    picam2.start()
    time.sleep(1)
    return picam2


def close_camera(picam2):
    picam2.stop()
    time.sleep(5)


def get_shot(picam2, image_name):
    time.sleep(3)
    picam2.capture_file(image_name)


if __name__ == '__main__':
    picam = init_camera()
    get_shot(picam, "shot.jpg")