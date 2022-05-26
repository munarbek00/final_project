from PIL import Image
from errors import ChoiceError

options = {
    'Right':-90,
    'Left': 90,
    }


def rotate(image_path, option):
    if option == 'Choose option':
        raise ChoiceError()
    path = image_path.split('/')
    image_format = path[-1].split('.')
    pt = '/'.join(path[:-1])
    saved_location = f'{pt}/{image_format[0]}_{option}.{image_format[1]}'
    if option == 'Flip':
        flip_image(image_path, saved_location)
    else:
        rotate_images(image_path, options[option], saved_location)

def flip_image(image_path, saved_location):
    image_obj = Image.open(image_path)
    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    rotated_image.save(saved_location)


def rotate_images(image_path, option, saved_location):
    image_obj = Image.open(image_path)
    rotated_image = image_obj.rotate(option)
    rotated_image.save(saved_location)