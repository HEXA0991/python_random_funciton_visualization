from PIL import Image
import random

def gen_pixel(dummy = -1):
    if dummy == -1:
        return random.randint(0, 255)
    else:
        return dummy

img = Image.new('L', (1280, 720))

for i in range(1280):
    for j in range(720):
        img.putpixel((i, j), gen_pixel())

img.save('random_img.jpg')
