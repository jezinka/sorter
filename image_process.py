from PIL import Image, ImageChops


def find_difference(first, second):
    im1 = Image.open(first)
    im2 = Image.open(second)

    box = (200, 60, 580, 200)
    im1_cropped = im1.crop(box)
    im2_cropped = im2.crop(box)

    diff = ImageChops.difference(im2_cropped, im1_cropped)
    print(diff.getcolors(diff.size[0] * diff.size[1]))
    diff.save("diff.jpg")


if __name__ == '__main__':
    find_difference("clear.jpg", "with_marble.jpg")
