from PIL import Image, ImageChops, ImageFilter


def check_if_black(first, second, pixels, folder=""):
    im1 = Image.open(folder + first)
    im2 = Image.open(folder + second)

    difference = ImageChops.difference(im1, im2)
    bw = difference.filter(ImageFilter.MinFilter(9)).convert('1')
    bbox = bw.getbbox()
    if bbox is not None:
        pixel = im2.getpixel((int((bbox[0] + bbox[2]) / 2), int((bbox[1] + bbox[3]) / 2)))
        pixels.append(pixel)
        return sum(pixel) < 120 and pixel[0] < 50
    return False


if __name__ == '__main__':
    print(check_if_black("clear.jpg", "with_marble.jpg", [], "sample/black/"))
