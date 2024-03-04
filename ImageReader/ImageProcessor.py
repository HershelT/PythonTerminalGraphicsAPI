#Code to generate an image from a png file
from PIL import Image, ImageChops
import os
import re
from AnsiiEscapeColors import *
import numpy as np

def generate_ascii_colors():
    basic_colors = [(0, 0, 0), (128, 0, 0), (0, 128, 0), (128, 128, 0),
                    (0, 0, 128), (128, 0, 128), (0, 128, 128), (192, 192, 192),
                    (128, 128, 128), (255, 0, 0), (0, 255, 0), (255, 255, 0),
                    (0, 0, 255), (255, 0, 255), (0, 255, 255), (255, 255, 255)]    
    levels = [0, 95, 135, 175, 215, 255]
    extended_colors = [(r, g, b) for r in levels for g in levels for b in levels]    
    return basic_colors + extended_colors
ascii_colors = generate_ascii_colors()

pixel_to_asciicode = {}
# Class to create a list of images in ascii array format 
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
    def __init__(self, img : list , scaleRatio = False, trim = True):
        imageList = []
        self.ImageAscii = []
        for image in img:
            if trim:
                imageList.append(self.trim_image(Image.open(image)))
            else:
                imageList.append(Image.open(image))
            # imageList.append(Image.open(image))
        for rgb in imageList:
            self.ImageAscii.append(self.getPixelToAscii(rgb, scaleRatio))

    def getAsciiList(self):
        return self.ImageAscii
    def size(self, image):
        width, height = image.size
        return width, height
    def rgb_to_ascii(self, r, g, b):
        def distance(c1, c2):
            return sum((x1-x2)**2 for x1,x2 in zip(c1, c2))
        rgb_color = (r, g, b)
        # Find the index of the closest color in the ascii_colors list
        closest_color = min(range(len(ascii_colors)), key=lambda index: distance(rgb_color, ascii_colors[index]))
        # Return the ANSI color code
        pixel_to_asciicode[rgb_color] = "\033[48;5;{}m".format(closest_color)
        return "\033[48;5;{}m".format(closest_color)
    def getPixelToAscii(self, image, scaleRatio = False):
        # Convert the image to RGB if it's not already
        if image.mode != 'RGB':
            image = image.convert('RGB')
        sizes = self.size(image)
        ansi_codes = []
        for x in range(sizes[1]):
            row = []
            for y in range(sizes[0]):
                r, g, b = image.getpixel((y, x))
                if (r,g,b) in pixel_to_asciicode:
                    color = pixel_to_asciicode[(r,g,b)]
                    row.append(color + ' ')
                    if scaleRatio:
                        row.append(color + ' ')
                else:
                    color = self.rgb_to_ascii(r,g,b)
                    row.append(color + ' ')
                    if scaleRatio:
                        row.append(color + ' ')
            ansi_codes.append(row)
        return ansi_codes
        # ansi_codes = list(map(lambda pixel: (self.rgb_to_ascii(*pixel) + ' ') *(2 if scaleRatio else 1), pixels))
        # Convert the list of ANSI codes to a 2D numpy array and return it
        # return [ansi_codes[i*width:(i+1)*width] for i in range(height)]
        # return np.array(ansi_codes).reshape(img.size[1], img.size[0])
    def printOutImage(self, imageAscii : list):
        # drawing = self.colors.tolist()  
        print('\033[0m\n'.join(''.join(row) for row in imageAscii), end=reset)
    def printOutNumpy(self, imageAscii : list):
        print(np.array(imageAscii))
    def getPixelArray(self, imageAtSpot):
        return self.ImageAscii[imageAtSpot]

# Convert the 2D array to a string



# Check if the operating system is Windows
is_windows = os.name == 'nt'
dir_sep = '\\' if is_windows else '/'

#declare all the images
ConnectFourBoard = [f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourBoard1.png',
                     f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourBoard2.png',
                      f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourBoard3.png',
                       f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourBoard4.png',]
AlternateConnectFourBoard = [f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourBoard5.png',
                        f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourBoard6.png',
                        f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourBoard7.png',
                        f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourBoard8.png',]
                        # f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourPieces9.png',]

ConnectFourPieces = [f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourPieces1.png',
                      f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourPieces2.png',
                      f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourPieces3.png',
                      f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourPieces4.png',
                      f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourPieces9.png',]

AlternateConnectFourPieces = [f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourPieces5.png',
                        f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourPieces6.png',
                        f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourPieces7.png',
                        f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourPieces8.png',
                        f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourPieces9.png',]

OthelloBoard = [f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}OthelloBoard1.png',
                    f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}OthelloBoard2.png',
                    f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}OthelloBoard3.png',
                    f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}OthelloBoard4.png',]

OthelloPieces = [f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}OthelloPieces1.png',
                    f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}OthelloPieces2.png',
                    f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}OthelloPieces3.png',
                    f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}OthelloPieces4.png',
                    f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}OthelloPieces5.png',]
WinDisplay = [f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourBoard9.png',
              f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourBoard10.png',
              f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourBoard11.png',
              f'ImageReader{dir_sep}PythonTerminalSprites{dir_sep}ConnectFourBoard12.png',]

#create a pixel image object
ConnectFourBoard = pixelImage(ConnectFourBoard, True)
ConnectFourPieces = pixelImage(ConnectFourPieces, True)
#alternate Colors
AlternateConnectFourBoard = pixelImage(AlternateConnectFourBoard, True)
AlternateConnectFourPieces = pixelImage(AlternateConnectFourPieces, True)
# print(np.array(list((AlternateConnectFourBoard.rgb_to_ascii(0, 135, 215)))))
#Win display
WinDisplay = pixelImage(WinDisplay, True)
#working on othello board
OthelloBoard = pixelImage(OthelloBoard, True)
OthelloPieces = pixelImage(OthelloPieces, True)


