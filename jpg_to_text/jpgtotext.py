#image to text

from PIL import Image

from pytesseract import image_to_string

img=Image.open('/home/soham/Pictures/check.png')

text=image_to_string(img)
print(text)
