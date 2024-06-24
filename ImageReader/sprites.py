from ImageProcessor import *

# File to hold sprites created from pixel art in ImageProcessor
blocks = [f'ImageReader{dir_sep}BlocksSprites{dir_sep}Blocks.png']
blocks =  pixelImage(blocks)

blocksBig = [f'ImageReader{dir_sep}BlocksSprites{dir_sep}blocksBig.png']
blocksBig = pixelImage(blocksBig)

toolsBig = [f'ImageReader{dir_sep}BlocksSprites{dir_sep}ToolsBig.png']
toolsBig = pixelImage(toolsBig)

itemsTools = [f'ImageReader{dir_sep}ItemSprites{dir_sep}Items(8x8).png']
itemsTools = pixelImage(itemsTools)

backgroundBig =  [f'ImageReader{dir_sep}BackgroundSprites{dir_sep}BackgroundBlue.png', 
                  f'ImageReader{dir_sep}BackgroundSprites{dir_sep}Background.png',
                    f'ImageReader{dir_sep}BackgroundSprites{dir_sep}BackgroundTile.png',
                    f'ImageReader{dir_sep}BackgroundSprites{dir_sep}NewLevel.png']
backgroundBig = pixelImage(backgroundBig)

numbers = [f'ImageReader{dir_sep}LettersSprites{dir_sep}Numbers.png']
numbers = pixelImage(numbers)

letters = [f'ImageReader{dir_sep}LettersSprites{dir_sep}Letters1.png', 
           f'ImageReader{dir_sep}LettersSprites{dir_sep}Letters.png',]
letters = pixelImage(letters)



spriteBlack = letters.getPixel(0).getPixel(0, 8)
# print(f"{spriteBlack} Hello World")
# import time
# time.sleep(5)