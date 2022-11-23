from camera_utils import get_shot, init_camera
from color_request import get_color_prediction
from dump import dump_left, dump_right
from get_one import get_marble

clear_photo = "clear.jpg"
marble_photo = "with_marble.jpg"


def sort(max_round=10):
    picam2 = init_camera()
    pixels = []
    for i in range(0, max_round):
        get_marble()
        get_shot(picam2, marble_photo)
        if get_color_prediction(marble_photo) == 'black':
            dump_left()
        else:
            dump_right()
    print(pixels)


if __name__ == '__main__':
    sort()
