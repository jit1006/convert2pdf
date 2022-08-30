from PIL import Image
import os

filename = input('image location with extension (like //pic.jpg) : ')

image = Image.open(filename)

if image.mode == "RGBA":
     image = image.convert("RGB")

output ='output.pdf'
image.save(output) 