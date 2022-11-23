import time

from picamera2 import Picamera2, Preview


def init_camera():
    picam2 = Picamera2()
    camera_config = picam2.create_preview_configuration()
    picam2.configure(camera_config)
    picam2.start_preview(Preview.QTGL)
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
    i = 0
    while True:
        get_shot(picam, "sample/shot_"+str(i)+".jpg")
        i += 1
        
