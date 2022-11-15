from dump import dump_left, dump_right
from get_one import get_marble


def sort():
    while True:
        get_marble()
        dump_left()
        get_marble()
        dump_right()


if __name__ == '__main__':
    sort()
