from camera_utils import get_shot, init_camera
from dump import dump_left
from get_one import get_marble


def sort():
    picam2, config = init_camera()
    get_shot(picam2, "clear.jpg")
    get_marble()
    get_shot(picam2, "with_marble.jpg")
    dump_left()


if __name__ == '__main__':
    sort()
