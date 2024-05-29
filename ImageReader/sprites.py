from ImageProcessor import *

# File to hold sprites created from pixel art in ImageProcessor
blocks = [f'ImageReader{dir_sep}BlocksSprites{dir_sep}Blocks.png']
blocks =  pixelImage(blocks)

blocksBig = [f'ImageReader{dir_sep}BlocksSprites{dir_sep}blocksBig.png']
blocksBig = pixelImage(blocksBig)

toolsBig = [f'ImageReader{dir_sep}BlocksSprites{dir_sep}ToolsBig.png']
toolsBig = pixelImage(toolsBig)

backgroundBig =  [f'ImageReader{dir_sep}BackgroundSprites{dir_sep}BackgroundBlue.png']
backgroundBig = pixelImage(backgroundBig)

numbers = [f'ImageReader{dir_sep}LettersSprites{dir_sep}Numbers.png']
numbers = pixelImage(numbers)