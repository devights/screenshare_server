from screenshare_server.models import Screenshot
from PIL import ImageChops
from PIL import Image
from decimal import *


def handle_uploaded_file(in_file, source):
    s = Screenshot(image=in_file,
                   source=source)

    last_shot = Screenshot.objects.filter(source=source).order_by('-id')[0]
    if not is_image_similar(s.image, last_shot.image):
        s.save()


def is_image_similar(img1, img2):
    first = Image.open(img1)
    second = Image.open(img2)

    diff = ImageChops.difference(first, second)
    percent_diff = get_percent_difference(first.getbbox(), diff.getbbox())
    if percent_diff < 10:
        return True
    return False


def _get_box_area(bbox):
    try:
        height = abs(bbox[1] - bbox[3])
        width = abs(bbox[0] - bbox[2])
        area = height * width
    except TypeError:
        area = 0
    return area


def get_percent_difference(original, diff):
    orig_area = Decimal(_get_box_area(original))
    diff_area = Decimal(_get_box_area(diff))
    return int(100*(diff_area/orig_area))


