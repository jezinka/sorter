from camera_utils import get_shot, init_camera
from dump import dump_left, dump_right
from get_one import get_marble
from image_process import check_if_black

clear_photo = "clear.jpg"
marble_photo = "with_marble.jpg"


def sort(max_round=10):
    picam2 = init_camera()
    pixels = []
    for i in range(0, max_round):
        get_shot(picam2, clear_photo)
        get_marble()
        get_shot(picam2, marble_photo)
        if check_if_black(clear_photo, marble_photo, pixels):
            dump_left()
        else:
            dump_right()
    print(pixels)


if __name__ == '__main__':
    sort()
