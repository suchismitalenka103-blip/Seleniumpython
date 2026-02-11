from email.mime import image
from PIL import Image

f = open("../Screenshots/demofile.txt", "r")
print(f.read())

im = open("../Screenshots/image.png")
print(im)
im1 = Image.open("../Screenshots/image.png")
print(im1)
# Image.open("../Screenshots/image.png")
