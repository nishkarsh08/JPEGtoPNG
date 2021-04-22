# Converter JPEG to PNG

import sys  # for taking arguments from the command line
import os  # for path manipulations
from PIL import Image  # To convert the type of images

image_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):  # os.path.exists gonna return True if path exists else False
    os.makedirs(output_folder)  # os.makedirs create directory if not present

for filename in os.listdir(image_folder):  # os.listdir takes a path of the directory and
    # returns a list of files contains inside it.['bulbasaur.jpg', 'charmander.jpg', 'pikachu.jpg', 'squirtle.jpg']
    print(os.listdir(image_folder))
    # print(filename)
    img = Image.open(f"{image_folder}{filename}")
    print(os.path.splitext(filename))  # returns a split text tuple like ('pikachu', '.jpg')
    clean_name = os.path.splitext(filename)[0]
    img.save(f"{output_folder}{clean_name}.png", "png")
    print('All done!!')
