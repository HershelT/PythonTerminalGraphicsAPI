from drawing import *
sys.path.insert(0, 'ImageReader')
from ImageReader import *
from keyboardListener import *

#set a background color for all the sprites
BACKGROUND_COLOR = cyan
# clear()
# resizeWindow(2)
# time.sleep(0.5)
BLOCK_SIZE = 16

#Get the Sprite Sheet
BlockSprites = [f'ImageReader{dir_sep}BlocksSprites{dir_sep}newGameSprites.png']
BlockSprites = pixelImage(BlockSprites, SPRITE_COLOR_REPLACE, BACKGROUND_COLOR).getPixel(0)
#Get the lengths of the sprite sheet
SPRITE_SHEET_LENGTH = len(BlockSprites)
SPRITE_SHEET_WIDTH = len(BlockSprites[0])
#Set a dictionary to hold all the sprites
SPRITE_SHEET = {}

class Sprite:
    def __init__(self, name, solid = True, moveable = False, breakable = False):
        self.name = name
        self.sprite = []
        self.solid = solid
        self.moveable = moveable
        self.breakable = breakable
    def getName(self):
        return self.name
    def getSprite(self):
        return self.sprite
    def getSolid(self):
        return self.solid
    def getMoveable(self):
        return self.moveable
    def getBreakable(self):
        return self.breakable
    def setMoveable(self, newMoveable):
        self.moveable = newMoveable
    def setSolid(self, newSolid):
        self.solid = newSolid
    def setBreakable(self, newBreakable):
        self.breakable = newBreakable
    def setSprite(self, newSprite):
        self.sprite = newSprite

#Create a function to scan all sprites on given line
def scanSpriteSheet(spriteSheet : list[list], SPRITE_NAMES_LIST : list[Sprite], placement= 0 ):
    for i in range(0, len(SPRITE_NAMES_LIST)):
        SPRITE_NAMES_LIST[i].setSprite(scanArea(spriteSheet, (i*BLOCK_SIZE, placement), BLOCK_SIZE, BLOCK_SIZE))
        SPRITE_SHEET[SPRITE_NAMES_LIST[i].getName()] = SPRITE_NAMES_LIST[i]



ORES = [Sprite(name = "Iron Ore", solid = True, moveable = False, breakable = True), 
        Sprite(name = "Diamond Ore", solid = True, moveable = False, breakable = True), 
        Sprite(name = "Gold Ore", solid = True, moveable = False, breakable = True),
        Sprite(name = "Emerald Ore", solid = True, moveable = False, breakable = True)]
TERRAIN = [Sprite(name = "Grass", solid = True, moveable = False, breakable = True),
           Sprite(name = "Dirt", solid = True, moveable = False, breakable = True),
           Sprite(name = "Grass Corner", solid = True, moveable = False, breakable = True)]
STONE = [Sprite(name = "Stone", solid = True, moveable = False, breakable = True),
         Sprite(name = "Mossy Cobblestone", solid = True, moveable = True, breakable = True)]
END = [Sprite(name = "Obsidian", solid = True, moveable = False, breakable = False),
       Sprite(name = "Portal Block", solid = False, moveable = False, breakable = True),
       Sprite(name = "Portal", solid = False, moveable = False, breakable = False)]
# END = [Sprite(name, True, False, False) for name in END]
TRAVEL = [Sprite(name = "Door", solid = False, moveable = False, breakable = True),
          Sprite(name = "Platform", solid = False, moveable = False, breakable = True),
          Sprite(name = "Ladder", solid = False, moveable = False, breakable = True)]
DECORATION = [Sprite(name = "Glass", solid = True, moveable = False, breakable = True),
              Sprite(name = "Brick", solid = True, moveable = False, breakable = True),
              Sprite(name = "Wood Plank", solid = True, moveable = False, breakable = True),
              Sprite(name = "Stone Brick", solid = True, moveable = False, breakable = True)]
INTERACTABLE = [Sprite(name = "Chest", solid = False, moveable = False, breakable = True),
                Sprite(name = "Item Frame", solid = False, moveable = False, breakable = True)]
NETHER = [Sprite(name = "Netherrack", solid = True, moveable = False, breakable = True),
            Sprite(name = "Fire", solid = False, moveable = False, breakable = False)]
MOVEABLE = [Sprite(name = "TNT", solid = True, moveable = True, breakable = True)]

#List of all sprite lists that hold all names of sprites
ALL_SPRITE_NAMES = [ORES, TERRAIN, STONE, END, TRAVEL, DECORATION, INTERACTABLE, NETHER, MOVEABLE]

for i, spriteClass in enumerate(ALL_SPRITE_NAMES, 1):
    scanSpriteSheet(BlockSprites, spriteClass, SPRITE_SHEET_LENGTH-(i*BLOCK_SIZE))

# # print out all sprites to see if they displayed correctly
# for sprite in SPRITE_SHEET:
#     printScreen(SPRITE_SHEET[sprite].getSprite())
#     time.sleep(0.1)


