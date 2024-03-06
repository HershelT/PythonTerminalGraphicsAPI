# Import the Pillow library
# from PythonTerminalSprites import *
from PIL import Image, ImageChops
import os
import re
from AnsiiEscapeColors import *
# from numpy import  array, reshape, asarray, ndarray
import numpy as np

def generate_ansi_colors():
    basic_colors = [(0, 0, 0), (128, 0, 0), (0, 128, 0), (128, 128, 0),
                    (0, 0, 128), (128, 0, 128), (0, 128, 128), (192, 192, 192),
                    (128, 128, 128), (255, 0, 0), (0, 255, 0), (255, 255, 0),
                    (0, 0, 255), (255, 0, 255), (0, 255, 255), (255, 255, 255)]    
    levels = [0, 95, 135, 175, 215, 255]
    extended_colors = [(r, g, b) for r in levels for g in levels for b in levels]    
    return basic_colors + extended_colors
ansi_colors = generate_ansi_colors()
# print(ansi_colors)

# Open the .gpl file
# Open the .gpl file
# with open("ansi_colors.gpl", "w") as file:
#     # Write the header
#     file.write("GIMP Palette\n")
#     file.write("Name: ANSI Colors\n")
#     file.write("Columns: 4\n")
#     file.write("#\n")
#     # Write the colors
#     for rgb in ansi_colors:
#         file.write(f"{rgb[0]} {rgb[1]} {rgb[2]} Color\n")
# Loop through each pixel in the image to get the rgb value
pixel_to_ansicode = {}
import copy
class Pixel: 
    def __init__(self, image: list):
        self.image = image
    def get(self):
        return self.image
    def getCopy(self, image):
        return Pixel(copy.deepcopy(image))
    def getPixel(self, row, col):
        return self.image[row][col]
    def setPixel(self, row, col, color):
        self.image[row][col] = color
    def replaceAllPixels(self, newColor):
        for row in range(len(self.image)):
            for col in range(len(self.image[row])):
                self.image[row][col] = newColor
    def replacePixels(self, oldColor, newColor):
        for row in range(len(self.image)):
            for col in range(len(self.image[row])):
                if self.image[row][col] == oldColor:
                    self.image[row][col] = newColor
    def getColorAtSpot(self, row, col):
        return self.image[row][col]
    
    

class pixelImage:
    
    @staticmethod
    def trim_image(img):
    # Convert the image to RGB if it's not already
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Create a background image of the same color as the corner pixel
        bg = Image.new('RGB', img.size, img.getpixel((0,0)))

        # Find the difference between the input image and the background image
        diff = ImageChops.difference(img, bg)

        # The difference is zero for all pixels that match the background color,
        # so we need to find the bounding box of the non-zero regions
        bbox = diff.getbbox()

        # If the bounding box is not None, crop the image to that bounding box
        if bbox:
            img = img.crop(bbox)

        return img
    def __init__(self, img : list , scaleRatio = False):
        imageList = []

        self.ImageAnscii = []
        for image in img:
            imageList.append(self.trim_image(Image.open(image)))
            # imageList.append(Image.open(image))
        for rgb in imageList:
            pixel = self.getPixelToAnscii(rgb, scaleRatio)
            self.ImageAnscii.append(Pixel(pixel))

    def getAnsciiList(self):
        return self.ImageAnscii
    def size(self, image):
        width, height = image.size
        return width, height
    def rgb_to_anscii(self, r, g, b):
        def distance(c1, c2):
            return sum((x1-x2)**2 for x1,x2 in zip(c1, c2))
        rgb_color = (r, g, b)
        # Find the index of the closest color in the ansi_colors list
        closest_color = min(range(len(ansi_colors)), key=lambda index: distance(rgb_color, ansi_colors[index]))
        # Return the ANSI color code
        pixel_to_ansicode[rgb_color] = "\033[48;5;{}m".format(closest_color)
        return "\033[48;5;{}m".format(closest_color)
    def getPixelToAnscii(self, image, scaleRatio = False):
        # Convert the image to RGB if it's not already
        if image.mode != 'RGB':
            image = image.convert('RGB')
        sizes = self.size(image)
        ansi_codes = []
        for x in range(sizes[1]):
            row = []
            for y in range(sizes[0]):
                r, g, b = image.getpixel((y, x))
                if (r,g,b) in pixel_to_ansicode:
                    row.append(pixel_to_ansicode[(r,g,b)] + ' ')
                    if scaleRatio:
                        row.append(pixel_to_ansicode[(r,g,b)] + ' ')
                else:
                    row.append(self.rgb_to_anscii(*(r,g,b)) + ' ')
                    if scaleRatio:
                        row.append(self.rgb_to_anscii(*(r,g,b)) + ' ')
            ansi_codes.append(row)
        # ansi_codes = list(map(lambda pixel: (self.rgb_to_anscii(*pixel) + ' ') *(2 if scaleRatio else 1), pixels))
        # Convert the list of ANSI codes to a 2D numpy array and return it
        return ansi_codes
        # return [ansi_codes[i*width:(i+1)*width] for i in range(height)]
        # return np.array(ansi_codes).reshape(img.size[1], img.size[0])
    def printOutImage(self, imageAnscii : list):
        # drawing = self.colors.tolist()  
        print('\033[0m\n'.join(''.join(row) for row in imageAnscii), end=reset)
    def printOutNumpy(self, imageAnscii : list):
        print(np.array(imageAnscii))
    def getPixel(self, index) -> Pixel:
        return self.ImageAnscii[index]
    def getPixelArray(self, index):
        array : Pixel = self.ImageAnscii[index]
        return array.get()
    

# Convert the 2D array to a string



# Check if the operating system is Windows
is_windows = os.name == 'nt'
dir_sep = '\\' if is_windows else '/'





#declare all the images
# humanList = [f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human1.png',
#             f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human2.png',
#             f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human3.png',
#             f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human4.png',
#             f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human5.png',
#             f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human6.png',
#             f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human7.png',
#             f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human8.png',
#             f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human9.png',
#             f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human10.png',
#             f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Human11.png']
# bulletList = [f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Bullet1.png',
#             f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Bullet2.png']
# heartList = [f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Heart.png']
# healthList = [f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Health1.png',
#               f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Health2.png',
#               f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Health3.png',]
# BackgroundList = [f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}Background.png']

# Human  = pixelImage(humanList, True)
# Bullet = pixelImage(bulletList, True)
# Heart  = pixelImage(heartList,True)
# Health = pixelImage(healthList,True)
# Background = pixelImage(BackgroundList,False)