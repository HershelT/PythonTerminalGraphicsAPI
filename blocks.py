# import sys, os
# import copy
# current_script_path = os.path.dirname(os.path.abspath(__file__))

# parent_directory = os.path.dirname(current_script_path)

# sys.path.insert(0, parent_directory)

from drawing import *
sys.path.insert(0, './ImageReader')
from keyboardListener import *
clear()
resizeWindow()
# clear()
backgroundColor = rgb(95, 215, 175)
# backgroundColor = black

#Setting up nether to align with background color
netherLevelIndex = 3
netherLevel = backgroundBig.getPixel(netherLevelIndex)
netherLevel.replacePixels(netherLevel.getPixel(0, 0), backgroundColor)
netherLevel = netherLevel.getImage()
#newLevel with index 4
startWorldIndex = 4
startWorld = backgroundBig.getPixel(startWorldIndex)
startWorld.replacePixels(startWorld.getPixel(0, 0), backgroundColor)
startWorld = startWorld.getImage()


#replacing all sprites to have same background color, as well as background color
chooseBackgroundIndex = 2
#getting world scale
scaleOfWorld = backgroundBig.getPixel(chooseBackgroundIndex).getWidth()
heightOfWorld = backgroundBig.getPixel(chooseBackgroundIndex).getLength()

newBlack = toolsBig.getPixel(0); replacePixel = backgroundBig.getPixel(chooseBackgroundIndex)
colorNew = newBlack.getPixel(0, 0); newReplace = replacePixel.getPixel(0, 0)
newBlack.replacePixels(colorNew, backgroundColor); replacePixel.replacePixels(newReplace, backgroundColor)
spriteSheet = newBlack.getImage(); 
backgroundBig = replacePixel.getImage()

#Sets newBlack as the go to background color
newBlack = newBlack.getPixel(0, 0)
newBlack = getColorFromAnsi(newBlack)









#Defining starting point for the screen
lastPoints = 0
points = 0

#initliaze a screen size
backgroundColor = newBlack
pixelRatio = 16
height = int(14*1)
width = int(22*1)
scale = 1
predefinedSquare = square(pixelRatio, pixelRatio, backgroundColor)


#Displacement for adding inventory and hearts to top
globalDisplacement = pixelRatio*2 - 8 + 1

#Moving left and right
#Important world generation stuff
#current chunk
Chunk = [0, 0]
#length of world
worldWidth = 0  
#height of world
worldHeight = 0
sideBySideView = {}
chunkPosition = {}
time.sleep(1)
for i in range(0, int(scaleOfWorld/(pixelRatio*width*scale))):
    worldWidth += 1
    worldHeight = 0
    # sideBySideView[i] = scanArea(backgroundBig, (i*width*pixelRatio, 0), height*pixelRatio, width*pixelRatio)
    for j in range(0, int(heightOfWorld/(pixelRatio*height*scale))):
        areaScaned = scanArea(backgroundBig, (i*width*pixelRatio, heightOfWorld-pixelRatio*height*scale - pixelRatio - j*pixelRatio*height*scale), height*pixelRatio, width*pixelRatio)
        if j == 0:  
            sideBySideView[i] = areaScaned
        chunkPosition[(i, j)] = areaScaned
        worldHeight += 1



worldLength = len(sideBySideView)
backgroundBig = sideBySideView[0]




#initliaze a inventory
#ITem perimeter color
inventoryPerimeterColor = white
Inventory = []
lastInventory = Inventory
#check if Scene.txt exists and if it does, then it will load the scene
if os.path.exists("Scene.txt"):
    Scene = getScene("Scene.txt")
    Inventory = getScene("Inventory.txt")[0]
    points = getScene("Points.txt")[0]
    # InventoryDrawnOver = getScene("Points")[1]
    points = int(points[0])
else:
    # print(f"{blue} New Game {reset}")
    Scene = screen(pixelRatio*height*scale + 9, pixelRatio*width*scale, backgroundColor)
    #Add predetermined background
    addToScreen(Scene, backgroundBig, 0, 0)
sceneLength = len(Scene)
sceneWidth = len(Scene[0])

#Setting up world travel and dimensions
changedWorld = False
overWorld = backgroundBig
netherWorld = netherLevel
currentWorld = 0
worldToTravel = {
    0: Scene,
    1: startWorld,
    2: netherWorld
}
amountOfWorlds = len(worldToTravel)




# Hide cursor
sys.stdout.write("\033[?25l")
print("\033[?25l", flush=True)



replace = numbers.getPixel(0)
replacePixel = replace.getPixel(0, 0)
replace.replacePixels(replacePixel, backgroundColor)

#Setting up the number sprites for the game
numbers = replace.getImage()
numbersHeight = 7
numbersWidth = 5
numbersDict = {}
for i in range(0, 11):
    numbersDict[i] = scanArea(numbers, (i*numbersWidth, 0),numbersHeight, numbersWidth)


#Setting up the letter sprites for the game
replace = letters.getPixel()
replacePixel = replace.getPixel(0, 0)
replace.replacePixels(replacePixel, backgroundColor)
letters = replace.getImage()
#Letter height and width
lettersHeight = 9
lettersWidth = 7
lettersDict = {}
for i in range(0, 26):
    lettersDict[chr(i+65)] = scanArea(letters, (i*lettersWidth, 0), lettersHeight, lettersWidth)
lettersDict[" "] = square(lettersHeight, lettersWidth, backgroundColor)
lettersDict["?"] = scanArea(letters, (26*lettersWidth, 0), lettersHeight, lettersWidth)
lettersDict["."] = scanArea(letters, (27*lettersWidth, 0), lettersHeight, lettersWidth)
lettersDict[":"] = scanArea(letters, (28*lettersWidth, 0), lettersHeight, lettersWidth)
lettersDict["!"] = scanArea(letters, (29*lettersWidth, 0), lettersHeight, lettersWidth)
lettersDict["'"] = scanArea(letters, (30*lettersWidth, 0), lettersHeight, lettersWidth)








#Setting up Old Sprited (Defunct)
# spritesTop = ["Grass", "Dirt", "Stone", "Gold Ore", "Iron Ore", "Diamond Ore", "Water", "Log", "Leaf", "Birch Plank", "TNT"]
# spritesMiddle = ["leftBed", "rightBed", "Brewing Stand", "Cactus", "Ladder", "LeftBoat", "RightBoat", "LeftSpider", "RightSpider",  "HumanBottom", "HumanTop"]
# spritesBottom = ["Pickaxe", "Sword", "Shovel", "Axe"]
# spriteDict = {}

#Setting up new (16x16) Sprites
blocks = spriteSheet
SpritesBlankPeople = ["Straight","Down", "Up"]
SpritesWeapons = ["Torch", "Torch Down", "Torch Up",
                  "Diamond Pickaxe", "Diamond Pickaxe Down", "Diamond Pickaxe Up", 
                  "Knife", "Knife Down", "Knife Up",
                  "Iron Pickaxe", "Iron Pickaxe Down", "Iron Pickaxe Up",
                  "Iron Sword", "Iron Sword Down", "Iron Sword Up"]
SpritesPlatform = ["Ladder", "Platform", "Door", "Small Portal"]
SpritesPeople = ["Ninja", "Ninja Crouch", "Bow Staff Ninja", "Angel",
                 "High Res Ninja", "High Res Ninja Down", "High Res Ninja Up"] 
                #  "High Res Ninja Torch", "High Res Ninja Torch Down", "High Res Ninja Torch Up",
                #  "Blank High Res Ninja", "Blank High Res Ninja Down", "Blank High Res Ninja Up"]
SpritesDecoration = ["Window","Brick","Fire", "Netherack", "Nether Portal", "Obsidian", "Chest", "Item Frame"]
SpritesTerrain = ["Grass", "Dirt", "Grass Connector", "Stone", "Iron Ore", "Diamond Ore", "Gold Ore", "Emerald Ore", "Wood Plank", "Stone Brick", "Mossy Cobblestone"]
spriteDict = {}

#Setting up sprites for the big sprite sheet
#Scanning the sprite sheet and sets each sprite to a dict valuale 
#Corresponding to the sprite name from sprites

for i in range(0, len(SpritesBlankPeople)):
    scanned = scanArea(blocks, (i*pixelRatio, pixelRatio*5), pixelRatio, pixelRatio)
    spriteDict[SpritesBlankPeople[i]] = scanned

for i in range(0, len(SpritesWeapons)):
    scanned = scanArea(blocks, (i*pixelRatio, pixelRatio*4), pixelRatio, pixelRatio)
    spriteDict[SpritesWeapons[i]] = scanned



for i in range(0, len(SpritesPlatform)):
    scanned = scanArea(blocks, (i*pixelRatio, pixelRatio*3), pixelRatio, pixelRatio)
    spriteDict[SpritesPlatform[i]] = scanned

for i in range(0, len(SpritesPeople)):
    scanned = scanArea(blocks, (i*pixelRatio, pixelRatio*2), pixelRatio, pixelRatio)
    spriteDict[SpritesPeople[i]] = scanned

for i in range(0, len(SpritesDecoration)):
    scanned = scanArea(blocks, (i*pixelRatio, pixelRatio), pixelRatio, pixelRatio)
    spriteDict[SpritesDecoration[i]] = scanned

for i in range(0, len(SpritesTerrain)):
    scanned = scanArea(blocks, (i*pixelRatio, 0), pixelRatio, pixelRatio)
    spriteDict[SpritesTerrain[i]] = scanned

sprites = []
#Adds each sprite to the sprite list
for i, sprite in enumerate(spriteDict):
    # if sprite not in SpritesWeapons and sprite not in SpritesBlankPeople:
    sprites.append(sprite)

# #Use this if want to use background that isnt blank
from copy import deepcopy
# predefinedSquare = deepcopy(spriteDict["Stone Brick"])
# for sprite in spriteDict:
#     if sprite != "Ninja" and "High Res Ninja" not in sprite: 
#         Change = spriteDict[sprite]
#         ToLookOver = deepcopy(predefinedSquare)
#         addToScreenWithoutColor(ToLookOver, Change, newBlack, 0, 0)
#         spriteDict[sprite] = ToLookOver
# spriteDict["Stone Brick"] = predefinedSquare

spriteDict["Ninja"] = spriteDict["High Res Ninja"]

# del spriteDict["High Res Ninja"]
#ITEM SET UP
#Setting up the 8x8 sprite sheet for items in game
itemHeight = 8
itemWidth = 8
#Getting the 8x8 sprite sheet for items in game
items = itemsTools.getPixel(0)
replaceItemPixel = items.getPixel(items.getWidth()-1, 0)
items.replacePixels(replaceItemPixel, backgroundColor)
items = items.getImage()
itemsDict = {}
#Naming items in game
itemsNames = []


#Setting up (8x8) sprites
ItemsLevels = ["Heart","Experience Orb", "Wings", "Ninja", "Mana Orb", "Gold Coin"]
ItemsDecorations = ["Window", "Ladder", "Platform", "Door", "Small Portal", "Fire", "Chest", "Item Frame", "Item Frame Check"]
ItemsBlocks = ["Dirt", "Stone", "Grass", "Grass Connector", "Brick", "Obsidian","Nether Portal", "Netherack", "Wood Plank"]
ItemsOres = ["Diamond Ore", "Iron Ore", "Gold Ore", "Emerald Ore", "Stone Brick", "Mossy Cobblestone"]
ItemsTools = ["Diamond Pickaxe", "Wood Sword", "Diamond Pic", "Flint 'n Steel"]
ItemsItems = ["Diamond", "Iron Ingot", "Gold Ingot", "Emerald"]

#Scanning the 8x8 sprite sheet and setting each sprite to a dict value
#Corresponding to the sprite name from itemsNames
for i in range(0, len(ItemsDecorations)):
    itemsNames.append(ItemsDecorations[i])
    itemsDict[ItemsDecorations[i]] = scanArea(items, (i*itemWidth, 3*itemHeight), itemHeight, itemWidth)

for i in range(0, len(ItemsBlocks)):
    itemsNames.append(ItemsBlocks[i])
    itemsDict[ItemsBlocks[i]] = scanArea(items, (i*itemWidth, 2*itemHeight), itemHeight, itemWidth)

for i in range(0, len(ItemsOres)):
    itemsNames.append(ItemsOres[i])
    itemsDict[ItemsOres[i]] = scanArea(items, (i*itemWidth, itemHeight), itemHeight, itemWidth)

for i in range(0, len(ItemsTools)):
    itemsNames.append(ItemsTools[i])
    itemsDict[ItemsTools[i]] = scanArea(items, (i*itemWidth, 0), itemHeight, itemWidth)

#Add non building blocks towards the end of the list
for i in range(0, len(ItemsLevels)):
    itemsNames.append(ItemsLevels[i])
    itemsDict[ItemsLevels[i]] = scanArea(items, (i*itemWidth, 4*itemHeight), itemHeight, itemWidth)

#Add items to the end of the list
for i in range(0, len(ItemsItems)):
    itemsNames.append(ItemsItems[i])
    itemsDict[ItemsItems[i]] = scanArea(items, (i*itemWidth, 5*itemHeight), itemHeight, itemWidth)

#See how many items are in the sprite blocks
AmountOfItemsInSpriteDict = 0
for i, spriteName in enumerate(sprites):
    if spriteName in itemsNames:
        AmountOfItemsInSpriteDict += 1



#LARGE SPRITE SHEET SET UP
#Setting up character sprites
#Setting up the 24x16 sprite sheet for the character

# characters = people.getPixel(0)
# replaceCharacterPixel = characters.getPixel(0, 0)
# characters.replacePixels(replaceCharacterPixel, backgroundColor)
# characters = characters.getImage()
# spriteDict["Ninja"] = characters






#gets the black background color from asperite sprite sheet
# newBlack = getColor(spriteDict[SpriteBigTools[2]], (0, 0))
# print(f"{newBlack}Color:")
# time.sleep(1)
spriteDict["Background"] = predefinedSquare
#Defining types of sprites that are in the background, as in can pass through on fall
backgroundSprites = ["Small Portal", "Fire", "Chest"]
#Creating background sprites that are in the background such that you can walk through them
SpritesInBackground = [predefinedSquare]
for backgroundSprite in backgroundSprites:
    SpritesInBackground.append(spriteDict[backgroundSprite])
    SpritesInBackground.append(mirror(spriteDict[backgroundSprite]))
#blocks a character can climb
climbing = ["Ladder", "Platform"]
#Blocks a charcter can pass through
passThrough = [predefinedSquare, "Background", "Ladder", "Nether Portal", "Platform", "Door", "Small Portal", "Fire","Chest"]
Angel = spriteDict["Angel"]
Ninja = spriteDict["Ninja"]
Chest = {}

#ANIMATION SPRITES
portalsOnScreen = {
    
}

#creating function to add numbers to screen starting from any area
def addNumToScreen(Scene, num, col, row):
    stringNum = str(num)
    listOfReplacementNums = []
    ColRow = []
    for char in stringNum:
        #adds all the places that were drawn over
        ColRow.append([col, row])
        listOfReplacementNums.append(addToScreenWithoutColor(Scene, numbersDict[int(char)], newBlack, col, row)[0])
        col += numbersWidth
    return [listOfReplacementNums, ColRow]

#create function to add letters to screen starting from any area
spriteBlack = getColorFromAnsi(spriteBlack)
# print(f"{spriteBlack}Color:\n\n\n\n")
# time.sleep(5)

#A function that takes a string and adds the correspinding sprite letters to screen
#Example "{1}Hello World{r}" prints a red "Hello World" with a reset color at the end of the string
def addLetter(Scene, letter : str, color, col, row):
    foundColor = 3
    listOfReplacementLetters = []
    ColRow = []
    colStart = col
    originalColor = color
    isReset = False
    for i, char in enumerate(letter):
        #adds all the places that were drawn over
        if foundColor < 3:
            # color = originalColor
            foundColor += 1
            continue
        if isReset:
            color = originalColor
            isReset = False
        if char.upper() == "I":
            col -= lettersWidth - int(lettersWidth/2) - 1
        if char == "\n":
            row -= lettersHeight + 1
            col = colStart - lettersWidth - 1
        else:
            ColRow.append([col, row])
            if letter[i] == "{" and letter[i+1] in "0123456789" and letter[i+2] == "}":
                color = colorsDict[int(letter[i+1])]
                i += 3
                try:
                    char = letter[i]
                except: break
                foundColor = 0
            if letter[i] == "{" and letter[i+1] in "r" and letter[i+2] == "}":
                color = colorsDict['r']
                i += 3
                try:
                    char = letter[i]
                except: break
                foundColor = 0
                isReset = True
            if char != "\n":
                letterSprite = changeRGB(lettersDict[char.upper()], spriteBlack, color)
                # color = originalColor
            else:
                row -= lettersHeight + 1
                col = colStart - lettersWidth - 1
                letterSprite = square(lettersHeight, lettersWidth, backgroundColor)
            #Add the letter and what it wrote over to the list and screen
            listOfReplacementLetters.append(addToScreenWithoutColor(Scene, letterSprite, newBlack, col, row)[0])
        if char.upper() == "I":
            col += lettersWidth - int(lettersWidth/2) - 6
        if char == "'":
            col += lettersWidth - 5
        else:
            col += lettersWidth + 1
    return [listOfReplacementLetters, ColRow]

#Creates a function to add points depending on the area scanned
def calculateScore(scannedArea):
    if scannedArea in spriteDict.values():
        return 100
    else:
        return 0
    
#create a function that runs a clock in the background with threading
# def clock():
#     global points
#     while True:
#         time.sleep(1)
#         points += 1
# #Starts the clock
# import threading
# t = threading.Thread(target=clock)
# t.start()
    






#create dictionary of length of spriteDict and set each sprite to a number
MapMaker = dict()
for i, sprite in enumerate(spriteDict):
    MapMaker[i] = sprite






#IMPORTANG GAME MECHANICS FOR STARTING POSITION
# #Starting position for moving sprite
r = 4*pixelRatio
c = 4*pixelRatio

#Initializes backup for pressing 'z' to get back to previous screen
drawnOver = Scene

#Setting up color palleteSelection or sprite pallete
palleteSelection = [rainbow, rainbow_bright, spriteDict, itemsDict]
pallateStart = 2
# initliazes pallet
Pallete = palleteSelection[pallateStart]

#Initializes the current color and border color of pallete for blocks
currentColor = palleteSelection[0][0]
borderColor = palleteSelection[0][0]
defaultBorder = grey
border = []
Stored = []



#Start screen with sprite not blocksw
erase = False
#Mode for drawing in colors or sprite blocks, Set false to star with sprites
colorMode = False
# Sets length of modulus when getting pallete
if colorMode:
    mod = len(Pallete)
else:
    mod = len(sprites)
#Pallete start Color for grabbing index of sprite or blocks (VERY IMPORTANT)
rc = 0

#Sets the starting sprite to Ninja
while sprites[rc%mod] != "Ninja":
    rc += 1
rc = rc%mod
#Start screen with sprite Ninja on certain area
Stored = addToScreenWithoutColor(Scene, Pallete[sprites[rc%mod]], newBlack, c, r)
overwriteSpot = Pallete[sprites[rc%mod]]



previousNumber = 0
#Creating a function to display inventory
def displayInventory(Scene, inventory : list, col, row):
    listofReplacementItems = []
    ColRow = []
    perimeterSize = 2
    perimeterColor = white
    changeColor = white
    for item in inventory:
        # listofReplacementItems.append(addToScreenWithoutColor(Scene, addPerimeter(itemsDict[item], inventoryPerimeterColor), newBlack, col, row)[0])
        # addToScreenWithoutColor(itemsDict[item], [f"{yellow} {}"]
        ColRow.append([col, row-2*perimeterSize])
        if Inventory[previousNumber] == item:
            changeColor = red
        else:
            changeColor = perimeterColor
        listofReplacementItems.append(addToScreenWithoutColor(Scene, createPermiter(itemsDict[item], perimeterSize, changeColor), newBlack, col, row-2*perimeterSize)[0])
        # listofReplacementItems.append(addToScreenWithoutColor(Scene, itemsDict[item], newBlack, col, row-1)[0])
        col += itemWidth + perimeterSize*2
        if col >= 16*(itemWidth + 2*perimeterSize):
            col = 0
            row -= (itemHeight + 2*perimeterSize)
    return [listofReplacementItems, ColRow]


# def printCurrentPos(row = r, col = c, color = Pallete[rc%mod], borderColor = Pallete[rc%mod], erase = False):
#     if erase == True:
#         erase = "On"
#     else:
#         erase = "Off"
#     print("Screen Height: ", sceneLength, " Screen Width: ", sceneWidth,  "  "*10, "\n",
#          "Current Position: ", "  "*10, "\n",
#           "Row: ", row, " Column: ", col, "  "*10, "\n",
#           "Current Color: ", color, "  ", reset, " "*10, "\n",
#           "Border Color: ", borderColor, "  ", reset, " "*10, "\n",
#           "Eraser: ", erase, "  "*10, "\n", flush = True)

# first = True

#Create a cache for checkForItem
#Store all rotations of the block and its flips as the key and the value as the name of the sprite
checkForItemCache = {}
#Checks all the rotations of the block and its flips to see if a spriteDict sprite is in the itemsDict and returns the key
def checkForItem(item : list, checkIfCollectible = False):
    #Checks if item is in cache and returns it
    item_tuple = tuple(tuple(row) for row in item)
    if item_tuple in checkForItemCache:
        nameOfItem = checkForItemCache[item_tuple]
        if checkIfCollectible:
            if nameOfItem in itemsDict:
                return nameOfItem
            else:
                return False
        return nameOfItem
    rotations = 0
    for key, value in spriteDict.items():
        for x in range(0, 8):
            if value == item:
                checkForItemCache[item_tuple] = key
                if checkIfCollectible:
                    if key in itemsDict:
                        return key
                    else:
                        return False
                return key
            item = rotate(item, 270)
            rotations += 1
            if rotations > 3:
                item = mirror(item)
                rotations = 0
    checkForItemCache[item_tuple] = False
    return False
def checkForItemPrevious(item, checkIfCollectible = False):
    rotations = 0
    for key, value in spriteDict.items():
        for x in range(0, 8):
            if value == item:
                if checkIfCollectible:
                    if key in itemsDict:
                        return key
                    else:
                        return False
                return key
            item = rotate(item, 270)
            rotations += 1
            if rotations > 3:
                item = mirror(item)
                rotations = 0
    return False


#Get cordinates depending on direction
def getDirection(Direction):
    col = 0
    row = 0
    if Direction == "Right":
        col += pixelRatio
    elif Direction == "Left":
        col -= pixelRatio
    elif Direction == "Up":
        row += pixelRatio
    elif Direction == "Down":
        row -= pixelRatio
    return [col, row]

#Select Block we are lloking at if in inventory
def selectBlockInInventory(Direction):
    colRow = getDirection(Direction)
    global rc
    global previousNumber
    global inventoryChange
    
    scanForBlock = scanArea(Scene, (c + colRow[0], r + colRow[1]), pixelRatio, pixelRatio)
    itemCheck = checkForItem(scanForBlock)
    if itemCheck in Inventory:
        previousNumber = Inventory.index(itemCheck)
        rc = previousNumber
        inventoryChange = True
        return itemCheck
    return None

def setUPUI(Scene):
    #SETTING UP STARTING UI AREA
    drawRectangle(Scene, rgb(0, 255, 255), (0, len(Scene)-pixelRatio*1 - itemHeight*1), (len(Scene[0]), len(Scene)))
    drawLine(Scene, black, (0, len(Scene)-pixelRatio*1-itemHeight-1), (len(Scene[0])-1, len(Scene)-pixelRatio*1-itemHeight-1))
    amount = 8
    for i in range(1, amount):
        addToScreenWithoutColor(Scene, itemsDict["Heart"], newBlack, sceneWidth - i*itemWidth, sceneLength - itemHeight-1)
        addToScreenWithoutColor(Scene, itemsDict["Experience Orb"], newBlack, sceneWidth - i*itemWidth, sceneLength - 2*itemHeight-1)
        addToScreenWithoutColor(Scene, itemsDict["Mana Orb"], newBlack, sceneWidth - i*itemWidth, sceneLength - 3*itemHeight-1)
        addToScreenWithoutColor(Scene, itemsDict["Gold Coin"], newBlack, sceneWidth - i*itemWidth - (amount-1)*itemWidth, sceneLength - 3*itemHeight-1)
    switchedSprite = False

#Moving Scene like checkPortal
def moveScene(Scene, Stored, Direction):
    global Chunk
    global sideBySideView
    global chunkPosition
    global inventoryChange
    global changedWorld
    global portalsOnScreen
    global overwriteSpot
    global c
    global r

    # if currentWorld > 0 and currentWorld < amountOfWorlds - 1:
    #     worldToTravel[currentWorld] = [[item for item in sublist] for sublist in Scene]
    #     addToScreen(Scene, Stored[0], c, r)
    #     if Direction == "Right":
    #         currentWorld += 1
    #         c = 0
    #     elif Direction == "Left":
    #         currentWorld -= 1
    #         c = sceneWidth - pixelRatio
    # else:
    #     return    
    ChunkChange = [0, 0]
    previousC = c
    previousR = r
    if Direction == "Right":
        if Chunk[0] < worldWidth - 1:
            chunkPosition[tuple(Chunk)] = [[item for item in sublist] for sublist in Scene]
            ChunkChange[0] += 1
            addToScreen(Scene, Stored[0], c, r)
            c = 0
        else:
            return Stored
    elif Direction == "Left":
        if Chunk[0] > 0:
            chunkPosition[tuple(Chunk)] = [[item for item in sublist] for sublist in Scene]
            ChunkChange[0] -= 1
            addToScreen(Scene, Stored[0], c, r)
            c = sceneWidth - pixelRatio
        else:
            return Stored
    elif Direction == "Up":
        if Chunk[1] > 0:
            chunkPosition[tuple(Chunk)] = [[item for item in sublist] for sublist in Scene]
            ChunkChange[1] -= 1
            #To place blocks below you possible
            if not keys.is_q_pressed():
                addToScreen(Scene, Stored[0], c, r)
            r = 0
        else:
            addToScreen(Scene, overwriteSpot, c, r)
            return Stored
    elif Direction == "Down":
        if Chunk[1] < worldHeight - 1:
            chunkPosition[tuple(Chunk)] = [[item for item in sublist] for sublist in Scene]
            ChunkChange[1] += 1
            addToScreen(Scene, Stored[0], c, r)
            r = sceneLength - globalDisplacement - pixelRatio
        else:
            return Stored
    else:
        return Stored
    # inventoryChange = True
    # changedWorld = True
    ChunkChange[0] += Chunk[0]
    ChunkChange[1] += Chunk[1]
    chunkToScan = scanArea(chunkPosition[tuple(ChunkChange)], (0,0), sceneLength-globalDisplacement, sceneWidth)
    checkBlock = scanArea(chunkToScan, (c, r), pixelRatio, pixelRatio)
    checkBlockItem = checkForItem(checkBlock)
    #If block below is not a background block or pass through, then return 
    if not keys.is_e_pressed():
        if not (checkBlockItem in climbing and Direction == "Down" and keys.is_s_pressed()):
            if not (checkBlockItem in climbing and Direction == "Up" and keys.is_w_pressed()):
                    if (checkBlockItem not in passThrough and checkBlockItem != "Background") or (checkBlockItem in climbing):
                        c = previousC
                        r = previousR
                        addToScreen(Scene, overwriteSpot, c, r)
                        return Stored
    #otherwise continue
    Chunk = ChunkChange
    if overwriteSpot == False:
        overwriteSpot = spriteDict["Ninja"]
    addToScreen(Scene, chunkToScan, 0, 0)
    # setUPUI(Scene)
    if keys.is_e_pressed():
        # rowCol = getDirection(Direction)
        addToScreen(Scene, predefinedSquare, c, r)
    if Direction == "Right":
        # keys.clear_pressed_keys()
        overwriteSpot = spriteDict["High Res Ninja"]
    elif Direction == "Left":
        overwriteSpot = mirror(spriteDict["High Res Ninja"])
    Direction = Direction
    Stored = addToScreenWithoutColor(Scene, overwriteSpot, newBlack, c, r)
    portalsOnScreen = {}
    scanForAnimationSprite(Scene, pixelRatio)
    printScreen(Scene)
    return Stored



#Create a function to chekc interaction with portal
def checkPortal(Scene, itemToCheck, c, r):
    if not erase and not colorMode and itemToCheck == "Small Portal" and isSpriteNinja:
        addToScreen(Scene, Stored[0], c, r)
        #Saves current screen to world
        global currentWorld
        global worldToTravel
        global inventoryChange
        global changedWorld
        global portalsOnScreen
        global overwriteSpot
        worldToTravel[currentWorld] = [[item for item in sublist] for sublist in Scene]
        inventoryChange = True
        changedWorld = True
        # worldToTravel[currentWorld] = copy.deepcopy(Scene)
        currentWorld += 1
        #Go back to original world
        currentWorld = currentWorld%amountOfWorlds
        #Add the new world to the screen
        if overwriteSpot == False:
            overwriteSpot = spriteDict["Ninja"]
        addToScreenWithColor(Scene, overwriteSpot, newBlack, c, r)
        printScreen(Scene)
        time.sleep(1)
        addToScreen(Scene, worldToTravel[currentWorld], 0, 0)
        addToScreenWithoutColor(Scene, Stored[0], newBlack, c, r)
        #Resets the portal on screen
        portalsOnScreen = {}
        scanForAnimationSprite(Scene, pixelRatio)
        addToScreenWithoutColor(Scene, overwriteSpot, newBlack, c, r)
        printScreen(Scene)
        # print("Current World: ", currentWorld, "                    ")

#CReate a function to move charcter down if it is on a background color of predefinedSquare
def checkGravity(Scene, blockBelow, Stored, c, r, pixelRatio, overwritespot):
    #Checks if blockBewlow is a predefinedSquare and if it is not a ladder (a block that the character can hold onto)
    itemCheck = checkForItem(Stored[0])
    if itemCheck not in climbing:
        if blockBelow in SpritesInBackground:
            # printScreen(Stored[0])
            # time.sleep(1)
            currentBlock = addToScreen(Scene, Stored[0], c, r)[0]
            r -= pixelRatio
            if overwritespot == False:
                overwritespot = spriteDict["Ninja"]
            Stored = addToScreenWithoutColor(Scene, overwritespot, newBlack, c, r)
            printScreen(Scene)
            time.sleep(0.1)
            return [r, Stored]
        elif r == 0 and Stored[0] == predefinedSquare:
            print(f"{red} Glitching out {reset}")
            drawn = addToScreen(Scene, Stored[0], c, r)[0]
            #Check if can move between scenes and move character
            previousR = r
            Stored = moveScene(Scene, Stored, "Down")
            if previousR != Stored[2]:
                r = Stored[2]
            else: 
                r = previousR
                
                addToScreenWithoutColor(Scene, drawn, newBlack, c, r)
            time.sleep(0.1)
    return [r, Stored]

#Starts the portal checker for animation
import threading
class CheckPortalThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.paused = threading.Event()
        self.paused.set()
        self.stop_flag = False

    def run(self):
        while not self.stop_flag:
            self.paused.wait()
            time.sleep(1)
            self.checkPortal()
    
    def pause(self):
        self.paused.clear()
    
    def resume(self):
        self.paused.set()

    #     while not self.stop_flag:
    #         time.sleep(1)
    #         self.checkPortal()

    def stop(self):
        self.stop_flag = True
    # def unstop(self):
    #     self.stop_flag = False
    #     self.run()

    def checkPortal(self):
        # Your existing checkPortal code here, using self.portalsOnScreen
        if not self.stop_flag:
            change = False
            for key, value in list(portalsOnScreen.items()):
                if (c, r) != key:
                    change = True
                    portalsOnScreen[key] = [mirror(value[0]), portalsOnScreen[key][1]]
                    #Deciding if i want to overide background
                    addToScreen(Scene, portalsOnScreen[key][1], key[0], key[1])
                    addToScreenWithoutColor(Scene, portalsOnScreen[key][0], newBlack, key[0], key[1])
                    # addToScreenWithoutColor(Scene, portalsOnScreen[key][0], newBlack, key[0], key[1])
            # if change and not self.stop_flag: 
            #     # printScreen(Scene)
#Start threaqd (Has LAg)
# t = CheckPortalThread()
# t.start()
# print("Started Portal Thread")

#If want to play with micro blocks uncomment
# pixelRatio = 8
# spriteDict = itemsDict
# sprites = itemsNames
# Scene = screen(pixelRatio*height*scale, pixelRatio*width*scale, backgroundColor)
isJumping = False
Holding = "Iron Pickaxe"
#Add names of sprites that will be animated by flipping them
animatingSprites = ["Small Portal", "Fire"]
#Check if any of the animating sprites are on screen
def scanForAnimationSprite(Scene, pixelRatio):
    global portalsOnScreen
    i, j = 0, 0
    while i < len(Scene) - pixelRatio - itemHeight - 1:
        while j < len(Scene[i]):
            blocksScanned = scanArea(Scene, (j, i), pixelRatio, pixelRatio)
            #Checks if block is an animation sprite
            typeOfBlock = checkForItem(blocksScanned)
            if typeOfBlock in animatingSprites:
                portalsOnScreen[(j, i)] = [blocksScanned, predefinedSquare]
            j += pixelRatio
        i += pixelRatio
        j = 0

#Check if any of the animating sprites are on screen
scanForAnimationSprite(Scene, pixelRatio)

switchedSprite = None
setUPUI(Scene)

#Adds every item in game to inventory (temporary)
# Inventory = ["Stone"]
Inventory = []
for item in itemsDict.keys():
    if item != "Wings" and item in spriteDict and item != "Ninja" and item not in SpritesWeapons and item not in SpritesBlankPeople:
        Inventory.append(item)
    inventoryChange = True
lastInventory = Inventory
#VARIABLE TO HOLD INVENTORY AND WHAT IT DREW OVER WHEN PLACING
# InventoryDrawnOver = displayInventory(Scene, Inventory, 0, sceneLength - itemHeight)
InventoryDrawnOver = [[]]
#when a change of inventory happens, set to true
inventoryChange = True

#Adding points
numDrawnOver = addNumToScreen(Scene, points, 17*pixelRatio-pixelRatio, 14*pixelRatio+1)
addLetter(Scene, "Points:", yellow, 14*pixelRatio-pixelRatio, 14*pixelRatio)
# for item in itemsDict.keys():
#     if item != "Wings":
#         Inventory.append(item)
    # inventoryChange = True





# Start keyboard listener for game
keys = MyKeyListener()
listener = keyboard.Listener(
    on_press=keys.on_press,
    on_release=keys.on_release
)
listener.start()
previousNumber = 0
Direction = "Right"
isSpriteNinja = True
# addLetter(Scene, "Tab:shift to select items", yellow, 0, 13*pixelRatio+1)
#GAME LOOP
# Start of engine
while not keys.is_esc_pressed():


    #Pause the game
    if keys.is_p_pressed() and keys.is_shift_pressed():
        keys.keys_pressed.discard(all)
        t.pause()
        lettersAdded = addLetter(Scene, "PAUSED", red, 10*pixelRatio-pixelRatio, 13*pixelRatio+1)
        printScreen(Scene)
        time.sleep(0.5)
        while not keys.is_p_pressed() or not keys.is_shift_pressed():
            if keys.is_esc_pressed():
                break
            # time.sleep(0.1)
        for i, sprite in enumerate(lettersAdded[0]):
            addToScreen(Scene, sprite, lettersAdded[1][i][0], lettersAdded[1][i][1])
        printScreen(Scene)
        t.resume()
        time.sleep(0.1)

    #Inventory updates
    if lastInventory != Inventory or inventoryChange or switchedSprite:
        itemRow = sceneLength - itemHeight
        itemCol = 0
        #Sort by name
        # Inventory.sort()
        for i, sprite in enumerate(InventoryDrawnOver[0]):
            #Replaces what inventory drew over before
            addToScreen(Scene, sprite, InventoryDrawnOver[1][i][0], InventoryDrawnOver[1][i][1])
        #adds new inventory to screen
        InventoryDrawnOver = displayInventory(Scene, Inventory, 0, sceneLength - itemHeight)
        printScreen(Scene)
        lastInventory = Inventory
        if switchedSprite:
            # time.sleep(0.3)
            switchedSprite = False
        inventoryChange = False


    # Checking gravity by looking at block below
    if not erase and isSpriteNinja and not colorMode:
        #PRevents from fsalling immediately if have momentum fro moving left or right
        if not (isJumping > 0 and isJumping < 3 and (keys.is_d_pressed() or keys.is_a_pressed())):
            #Resets left and right movement momentum if keys are pressed from second expression
            if isJumping > 0:
                isJumping = 0
            if r > 0:
                blockBelow = scanArea(Scene, (c, r - pixelRatio), pixelRatio, pixelRatio)
                #Check blocks below to see if can fall
                results = checkGravity(Scene, blockBelow, Stored, c, r, pixelRatio, overwriteSpot)
                previousR = r
                if previousR != results[0]:
                    r = results[0]
                    Stored = results[1]
                    if switchedSprite:
                        switchedSprite = False
                    #Checks if block is a portal to transfer dimensions
                    checkPortal(Scene, checkForItem(Stored[0]), c, r)
                    #allows continous falling of block (might change)
                    if "Wings" not in Inventory:
                        continue
                    else:
                        #Resets left and right movement while falling if on block, prevents glitch where cant double jump
                        if scanArea(Scene, (c, r - pixelRatio), pixelRatio, pixelRatio) not in SpritesInBackground:
                            isJumping = 0
                        #If on air allows to move left or right with wings, we have Movement of two blocks with wings
                        else:
                            isJumping = 2
            else:
                addToScreen(Scene, Stored[0], c, r)
                Stored = moveScene(Scene, Stored, "Down")
                # isJumping = 0
    #Replaces current ninja sprite if has wings
    if "Wings" in Inventory and spriteDict["Ninja"] != Angel and not colorMode and not erase:
        spriteDict["Ninja"] = Angel
        overwriteSpot = Angel
        addToScreen(Scene, Stored[0], c, r)
        addToScreenWithoutColor(Scene, Angel, newBlack, c, r)
        printScreen(Scene)
    #Replaces current ninja sprite if does not have wings
    elif "Wings" not in Inventory and spriteDict["Ninja"] == Angel and not colorMode and not erase:
        spriteDict["Ninja"] = Ninja
        overwriteSpot = Ninja
        addToScreen(Scene, Stored[0], c, r)
        addToScreenWithoutColor(Scene, Ninja, newBlack, c, r)
        printScreen(Scene)
    #Scoreboard updates if points change
    if lastPoints != points or changedWorld:
        if not changedWorld:
            for i, sprite in enumerate(numDrawnOver[0]):
                #Replaces what numbers drew over before
                addToScreen(Scene, sprite, numDrawnOver[1][i][0], numDrawnOver[1][i][1])
            changedWorld = False
            #adds new number to screen
            # addLetter(Scene, "PAUSED", red, 10*pixelRatio-pixelRatio, 13*pixelRatio+1)
            numDrawnOver = addNumToScreen(Scene, points, numDrawnOver[1][0][0], numDrawnOver[1][0][1])
            printScreen(Scene)
            lastPoints = points
        else:
            changedWorld = False
    

    #Block Selection Tool to cycle between using different blocks with shift and tab
    numberPressed = keys.get_pressed_number()
    if numberPressed != False or ((keys.is_tab_pressed() or keys.is_shift_pressed()) and not numberPressed and not erase):
        if not colorMode:
            lenInventory = len(Inventory)
            if lenInventory == 0:
                continue
            # Direction = False
            if numberPressed == '0':
                rc = lenInventory - 1
                previousNumber = rc
            elif numberPressed == False:
                if keys.is_tab_pressed(): 
                    rc  = (previousNumber + 1)%(AmountOfItemsInSpriteDict-1)
                    # Goes to beginning of list if pressing shift and already on last item
                    if rc >= lenInventory:
                        rc = 0
                else:
                    #Goes to end of list if pressing shift and already on first item
                    if previousNumber == 0:
                        rc = lenInventory - 1
                    else:
                        rc = (previousNumber - 1)%(AmountOfItemsInSpriteDict-1)
                previousNumber = rc
            else:
                rc = int(numberPressed)-1
                previousNumber = rc
            if erase:
                erase = False
            # Checks if inventory item is valid sprite that can be placed
            blockName = Inventory[previousNumber]  
            if blockName in spriteDict.keys() and not isSpriteNinja:
                addToScreen(Scene, Stored[0], c, r)
                while sprites[rc%mod] != blockName:
                    rc+=1
                toAdd = spriteDict[sprites[rc%mod]]
                Stored = addToScreenWithoutColor(Scene, toAdd, newBlack, c, r)
                overwriteSpot = toAdd
            inventoryChange = True
            isSpriteNinja = True
        else:
            if keys.is_tab_pressed():
                rc = (rc+1)%mod
            else:
                rc = (rc-1)%mod
            if erase:
                erase = False
            addToScreen(Scene, Stored[0], c, r)
            addToScreen(Scene, square(pixelRatio, pixelRatio, Pallete[rc%mod]), c, r)
            # printScreen(Scene)
            # time.sleep(0.1)
        printScreen(Scene)
        # time.sleep(0.05)
        keys.keys_pressed.discard(all)

    #Adds random item to inventory
    if keys.is_j_pressed() and "Wings" not in Inventory:
        # newItem = itemsNames[random.randint(0, len(itemsNames)-1)]
        Inventory.append("Wings")
        inventoryChange = True
        time.sleep(0.05)
        keys.keys_pressed.discard(all)

    #Pop last item in inventory
    elif keys.is_k_pressed() and "Wings" in Inventory:
        if Inventory != []:
            Inventory.pop()
            inventoryChange = True
            time.sleep(.05)
        keys.keys_pressed.discard(all)


    #Clears the screen and saves the current screen to last replacement
    if keys.is_c_pressed() and keys.is_ctrl_pressed() and Stored != []:
        if not Stored == []:
            addToScreen(Scene, Stored[0], c, r)
        portalsOnScreen = {}
        drawnOver = clearScreen(Scene, backgroundColor)
        clear()
        printScreen(Scene)
        Stored = []
        erase = True
        time.sleep(.1)
    #undoes clear screen
    if keys.is_z_pressed() and not drawnOver == [] and keys.is_ctrl_pressed():
        for i, row in enumerate(Scene):
            for j, col in enumerate(row):
                Scene[i][j] = drawnOver[i][j]
        drawnOver = []
        scanForAnimationSprite(Scene, pixelRatio)
        printScreen(Scene)
        time.sleep(.1)

    
    # Placing the block, super crucial
    if (keys.is_q_pressed()) and ((not keys.is_w_pressed() and not keys.is_d_pressed() and not keys.is_a_pressed() and not keys.is_s_pressed() and not keys.is_space_pressed()) or not isSpriteNinja):
        if colorMode:
            if erase:
                if Stored == []:    
                    Stored = addToScreen(Scene, square(pixelRatio, pixelRatio, Pallete[rc%mod]), c, r)
                else:
                    addToScreen(Scene, Stored[0], c, r)
            Stored = addToScreen(Scene, square(pixelRatio, pixelRatio, Pallete[rc%mod]), c, r)
        else:
            if erase:
                if Stored == []: 
                    Stored = addToScreenWithoutColor(Scene, spriteDict[sprites[rc%mod]], newBlack, c, r)
                else:
                    addToScreen(Scene, Stored[0], c, r)
                    addToScreenWithoutColor(Scene, spriteDict[sprites[rc%mod]], newBlack, c, r)
                overwriteSpot = spriteDict[sprites[rc%mod]]
            else:
                if isSpriteNinja:
                    if len(Inventory) > 0:
                        try:
                            cToChange = c
                            rToChange = r
                            if Direction == "Right" and c < sceneWidth - pixelRatio:
                                cToChange = c + pixelRatio
                                # addToScreen(Scene, spriteDict[Inventory[previousNumber]], c + pixelRatio, r)
                            elif Direction == "Left" and c > 0:
                                cToChange = c - pixelRatio
                                # addToScreen(Scene, spriteDict[Inventory[previousNumber]], c - pixelRatio, r)
                            elif Direction == "Down" and r > 0:
                                rToChange = r - pixelRatio
                                # addToScreen(Scene, spriteDict[Inventory[previousNumber]], c, r - pixelRatio)
                            elif Direction == "Up" and r < sceneLength - 3*pixelRatio:
                                rToChange = r + pixelRatio
                            if cToChange != c or rToChange != r:
                                checkBlock = scanArea(Scene, (cToChange, rToChange), pixelRatio, pixelRatio)
                                #place block if no block is there
                                if checkBlock == predefinedSquare:
                                    addToScreenWithoutColor(Scene, spriteDict[Inventory[previousNumber]], newBlack, cToChange, rToChange)
                                    if Inventory[previousNumber] in animatingSprites:
                                        portalsOnScreen[(cToChange, rToChange)] = [spriteDict[Inventory[previousNumber]], predefinedSquare]
                                #Checking interaction items
                                else:
                                    #checking for itemFrame
                                    addToScreenWithColor(checkBlock, itemsDict["Item Frame Check"], newBlack, 4, 4)
                                    addToScreenWithoutColor(checkBlock, itemsDict["Item Frame Check"], newBlack, 4, 4)
                                    checkItem = checkForItem(checkBlock)
                                    if checkItem == "Item Frame":
                                        addToScreenWithoutColor(Scene, itemsDict["Item Frame Check"], newBlack, cToChange+4, rToChange+4)
                                        addToScreenWithoutColor(Scene, itemsDict[Inventory[previousNumber]], newBlack, cToChange+4, rToChange+4)
                        except:
                            print(f"{red} Error: {reset} {Inventory[previousNumber]} not in spriteDict")
                            pass
                else:
                    previousBlock = Stored[0]
                    compareCurrentBlock = checkForItem(spriteDict[sprites[rc%mod]])
                    if compareCurrentBlock in animatingSprites:
                        portalsOnScreen[(c, r)] = [spriteDict[sprites[rc%mod]], previousBlock]
                    currentThing = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
                    Stored = [currentThing, c, r] 
        if erase:
            erase = False
        if not border == [] and colorMode:
            border = addBorderToArea(Scene, (c, r), pixelRatio, pixelRatio, Pallete[rc%mod], defaultBorder)
        if not isSpriteNinja:
            Spot = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
        printScreen(Scene)        
        time.sleep(.1)
        keys.keys_pressed.discard(all)


    

    #Select block in inventory depending on block we are looking at
    if keys.is_c_pressed() and not erase and not keys.is_ctrl_pressed():
        selectBlockInInventory(Direction)

    if keys.is_z_pressed() and not erase and not keys.is_ctrl_pressed():
        #Cyclying through items in inventory
        if Holding == "Diamond Pickaxe":
            Holding = "Torch"
        elif Holding == "Torch":
            Holding = "Knife"
        elif Holding == "Knife":
            Holding = "Iron Pickaxe"
        elif Holding == "Iron Pickaxe":
            Holding = "Iron Sword"
        elif Holding == "Iron Sword":
            Holding = "Diamond Pickaxe"

        #Seeting the different sprites and direction to hold a weapon by pasting it on the empty person sprite
        torchHolder = addToScreenWithoutColor(deepcopy(spriteDict["Straight"]), spriteDict[f"{Holding}"], newBlack, 0, 0, True)
        spriteDict["High Res Ninja"] = torchHolder
        torchHolderDown = addToScreenWithoutColor(deepcopy(spriteDict["Down"]), spriteDict[f"{Holding} Down"], newBlack, 0, 0, True)
        spriteDict["High Res Ninja Down"] = torchHolderDown
        torchHolderUp = addToScreenWithoutColor(deepcopy(spriteDict["Up"]), spriteDict[f"{Holding} Up"], newBlack, 0, 0, True)
        spriteDict["High Res Ninja Up"] = torchHolderUp
        spriteDict["Ninja"] = torchHolder
        
        #have to add part so it doesnt reset direction
        overwriteSpot = torchHolder
        Direction = "Right"

        addToScreen(Scene, Stored[0], c, r)
        addToScreenWithoutColor(Scene, spriteDict["High Res Ninja"], newBlack, c, r)
        printScreen(Scene)
        time.sleep(0.1)

    #Chest interaction
    if keys.is_i_pressed():
        checkItem = checkForItem(Stored[0])
        if checkItem == "Chest":
            if (c, r) in Chest:
                Inventory = Chest[(c, r)]
                inventoryChange = True
                del Chest[(c, r)]
            else:
                Chest[(c, r)] = Inventory
                Inventory = []
                inventoryChange = True
                previousNumber = 0
            time.sleep(0.1)
            keys.keys_pressed.discard(all)
        else:
            selectBlockInInventory(Direction)
        #     keys.keys_pressed.discard(all)
        # elif checkItem == "Item Frame":
        #     itemFrame = spriteDict["Item Frame"]
        #     addToScreenWithoutColor(itemFrame, itemsDict[Inventory[previousNumber]], newBlack, 4, 4)
        #     Stored[0] = itemFrame
    #Changing to ninja
    if keys.is_space_pressed() and not Stored == [] and (sprites[rc%mod] != "Ninja" or erase or colorMode):
        erase = False
        if colorMode:
            colorMode = False
        # else:
        #     switchedSprite = False
        addToScreen(Scene, Stored[0], c, r)
        addToScreenWithoutColor(Scene, spriteDict["Ninja"], newBlack, c, r)
        Direction = "Right"
        isSpriteNinja = True
        while (sprites[rc%mod] != "Ninja"):
            rc+=1
        rc = rc%mod
        overwriteSpot = spriteDict["Ninja"]
        printScreen(Scene)
        # time.sleep(.1)


    #changing color pallete
    if keys.is_u_pressed():
        overwriteSpot = False
        mod = len(palleteSelection[1])
        pallateStart+=1
        Pallete = palleteSelection[pallateStart%2]
        if not colorMode:
            addToScreen(Scene, square(pixelRatio, pixelRatio, Pallete[rc%mod]), c, r)
        colorMode = True
        #changs from rainbow palleteSelection to sprite palleteSelection
        scaned = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
        colorScanned = changeRGB(scaned, currentColor, Pallete[(rc)%mod])
        currentColor = Pallete[(rc)%mod]
        borderColor = Pallete[rc%mod]

        addToScreen(Scene, colorScanned, c, r)
        printScreen(Scene)
        time.sleep(0.2)

    #Changes pallets to sprite blocks
    if keys.is_y_pressed() and colorMode: # or first:
        if erase == True:
            erase = False
        overwriteSpot = False
        isSpriteNinja = False
        colorMode = False
        scannedArea = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
        Pallete = palleteSelection[2]
        mod = len(sprites)
        # Checks if not on background color. If not, then it will add the block to the screen
        # if first:
        #     while sprites[rc%mod] != "Ninja":
        #         rc+=1
        #     first = False
        #     inventoryChange = True
        if not scannedArea == predefinedSquare: 
            addToScreen(Scene, Stored[0], c, r)
        addToScreenWithoutColor(Scene, spriteDict[sprites[rc%mod]], newBlack, c, r)
        overwriteSpot = spriteDict[sprites[rc%mod]]
        printScreen(Scene)
        
    #moving blocks around
    #Up and Down
    if keys.is_w_pressed() and r < sceneLength - 3*pixelRatio  and not Stored == [] and isJumping < 1:
        
        # Add this if using sprite taller than pixelRatio
        # addToScreen(Scene, Stored[0], Stored[1], Stored[2])
        if Direction != "Up" and isSpriteNinja and not colorMode:
            addToScreen(Scene, Stored[0], c, r)
            if Direction == "Left" or Direction == "Down":
                if overwriteSpot == mirror(spriteDict["High Res Ninja Down"]):
                    overwriteSpot = mirror(spriteDict["High Res Ninja Up"])
                elif overwriteSpot == spriteDict["High Res Ninja Down"]:
                    overwriteSpot = spriteDict["High Res Ninja Up"]
                else:
                    overwriteSpot = mirror(spriteDict["High Res Ninja Up"])
            else:
                overwriteSpot = spriteDict["High Res Ninja Up"]
            addToScreenWithoutColor(Scene, overwriteSpot, newBlack, c, r)
            printScreen(Scene)
            Direction = "Up"
            continue
        #To place blocks below if trying to jump and press q
        blockAbove = scanArea(Scene, (c, r + pixelRatio), pixelRatio, pixelRatio)
        itemToCheck = checkForItem(blockAbove)
        if keys.is_q_pressed() and (blockAbove == predefinedSquare or itemToCheck in passThrough) and not erase and Stored[0] == predefinedSquare and isSpriteNinja:
            if r < sceneLength - pixelRatio*3: 
                addToScreen(Scene, Stored[0], c, r)
                Stored = addToScreenWithoutColor(Scene, overwriteSpot, newBlack, c, r+pixelRatio)
                printScreen(Scene)
                # time.sleep(0.1)
                addToScreenWithoutColor(Scene, spriteDict[Inventory[previousNumber]], newBlack, c, r)
                if Inventory[previousNumber] in animatingSprites:
                    portalsOnScreen[(c, r+pixelRatio)] = [spriteDict[Inventory[previousNumber]], predefinedSquare]
                r += pixelRatio
                printScreen(Scene)
                continue


        if (blockAbove == predefinedSquare) or (itemToCheck in passThrough) or erase or (not isSpriteNinja and Pallete == palleteSelection[2]) or colorMode:
            if overwriteSpot == False:
                Spot = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
            else:
                Spot = overwriteSpot
            addToScreen(Scene, Stored[0], Stored[1], Stored[2])
            r += pixelRatio
            if blockAbove == predefinedSquare and not isSpriteNinja:
                Stored = addToScreen(Scene, Spot, c, r)
                overwriteSpot = False
            else:
                overwriteSpot = Spot
                Stored = addToScreenWithoutColor(Scene, Spot, newBlack, c, r)
            printScreen(Scene)
        keys.keys_pressed.discard(all)
        if isSpriteNinja: 
            isJumping = 1
        #Checks if block is a portal to transfer dimensions
        checkPortal(Scene, itemToCheck, c, r)
        keys.keys_pressed.discard(all)
    #Moves Down
    elif keys.is_s_pressed() and r > 0 and not Stored == []:
        blockDown = scanArea(Scene, (c, r - pixelRatio), pixelRatio, pixelRatio)
        itemToCheck = checkForItem(blockDown)
        # isSpriteNinja = sprites[rc%mod] == "Ninja"
        if Direction != "Down" and isSpriteNinja and not colorMode:
            addToScreen(Scene, Stored[0], c, r)
            if Direction == "Left" or Direction == "Up":
                if overwriteSpot == mirror(spriteDict["High Res Ninja Up"]):
                    overwriteSpot = mirror(spriteDict["High Res Ninja Down"])
                elif overwriteSpot == spriteDict["High Res Ninja Up"]:
                    overwriteSpot = spriteDict["High Res Ninja Down"]
                else:
                    overwriteSpot = mirror(spriteDict["High Res Ninja Down"])
            else:
                overwriteSpot = spriteDict["High Res Ninja Down"]
            addToScreenWithoutColor(Scene, overwriteSpot, newBlack, c, r)
            printScreen(Scene)
            Direction = "Down"
            continue
        if (blockDown == predefinedSquare) or (itemToCheck in passThrough) or erase or (not isSpriteNinja and Pallete == palleteSelection[2]) or colorMode:
            if overwriteSpot == False:
                Spot = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
            else:
                Spot = overwriteSpot
            addToScreen(Scene, Stored[0], Stored[1], Stored[2])
            r -= pixelRatio
            if blockDown == predefinedSquare and not isSpriteNinja:
                Stored = addToScreen(Scene, Spot, c, r)
                overwriteSpot = False
            else:
                overwriteSpot = Spot
                Stored = addToScreenWithoutColor(Scene, Spot, newBlack, c, r)
            printScreen(Scene)
        checkPortal(Scene, itemToCheck, c, r)
        keys.keys_pressed.discard(all)
    #Left and Right
    if keys.is_d_pressed() and c < len(Scene[0]) - pixelRatio and not Stored == [] or (keys.is_d_pressed() and isJumping > 0 and isJumping < 3 and c < len(Scene[0]) - pixelRatio):
        #RTotates character to face right
        if Direction != "Right" and isSpriteNinja and not colorMode:
            # keys.clear_pressed_keys()
            addToScreen(Scene, Stored[0], c, r)
            if Direction == "Down" or Direction == "Up":
                overwriteSpot = spriteDict["High Res Ninja"]
            else:
                overwriteSpot = mirror(overwriteSpot)
            addToScreenWithoutColor(Scene, overwriteSpot, newBlack, c, r)
            if isJumping == 0:
                printScreen(Scene)
            Direction = "Right"
            continue

        if keys.is_q_pressed() and c < sceneWidth - pixelRatio and isSpriteNinja:
            checkForBackground = scanArea(Scene, (c + pixelRatio, r-pixelRatio), pixelRatio, pixelRatio)
            if checkForBackground == predefinedSquare:
                #Animate player placing like erase
                addToScreen(Scene, Stored[0], c, r)
                addToScreenWithoutColor(Scene, spriteDict["High Res Ninja Down"], newBlack, c, r)
                printScreen(Scene)
                # time.sleep(0.1)
                addToScreenWithoutColor(Scene, overwriteSpot, newBlack, c, r)
                #Placing block
                addToScreenWithoutColor(Scene, spriteDict[Inventory[previousNumber]], newBlack, c+pixelRatio, r-pixelRatio)
                if Inventory[previousNumber] in animatingSprites:
                    portalsOnScreen[(cToChange, rToChange)] = [spriteDict[Inventory[previousNumber]], predefinedSquare]
                printScreen(Scene)
                time.sleep(0.1)
        #Attempt to break corner block
        # elif keys.is_e_pressed() and keys.is_s_pressed() and c < sceneWidth - pixelRatio and r > 0 and isSpriteNinja:
        #     checkForBackground = scanArea(Scene, (c + pixelRatio, r-pixelRatio), pixelRatio, pixelRatio)
        #     if checkForBackground != predefinedSquare:
        #         addToScreen(Scene, Stored[0], c, r)
        #         addToScreenWithoutColor(Scene, spriteDict["High Res Ninja Up"], newBlack, c, r)
        #         printScreen(Scene)
        #         addToScreenWithoutColor(Scene, overwriteSpot, newBlack, c, r)
        #         #Erasing blocks
        #         erasedBlock = addToScreen(Scene, predefinedSquare, c+pixelRatio, r-pixelRatio)
        #         itemToCheck = checkForItem(erasedBlock[0])
        #         if itemToCheck in spriteDict and itemToCheck not in Inventory:
        #             Inventory.append(itemToCheck)
        #             inventoryChange = True
        #         printScreen(Scene)
        #         time.sleep(0.1)
        #         continue


            # continue
        # Add this if using sprite wider than pixelRatio
        # addToScreen(Scene, Stored[0], Stored[1], Stored[2])
        # isSpriteNinja = sprites[rc%mod] == "Ninja"
        if Direction != "Right" or Direction == "Right" or (isJumping > 0 and isJumping < 3):
            blockToRight = scanArea(Scene, (c + pixelRatio, r), pixelRatio, pixelRatio)
            itemToCheck = checkForItem(blockToRight)
            if (blockToRight == predefinedSquare) or (itemToCheck in passThrough) or erase or (not isSpriteNinja and Pallete == palleteSelection[2]) or colorMode:
                if overwriteSpot == False:
                    Spot = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
                else:
                    Spot = overwriteSpot
                addToScreen(Scene, Stored[0], Stored[1], Stored[2])
                c += pixelRatio
                if blockToRight == predefinedSquare and not isSpriteNinja:
                    Stored = addToScreen(Scene, Spot, c, r)
                    overwriteSpot = False
                else:
                    
                    overwriteSpot = Spot
                    Stored = addToScreenWithoutColor(Scene, Spot, newBlack, c, r)
                printScreen(Scene)
                if isJumping > 0:
                    isJumping += 1
                if isJumping > 3:
                    isJumping = 0
            else:
                isJumping = 0
            #Checks if block is a portal to transfer dimensions
            checkPortal(Scene, itemToCheck, c, r)
        # keys.clear_pressed_keys()
        keys.keys_pressed.discard(all)
    elif keys.is_a_pressed() and c > 0 and not Stored == [] or (keys.is_a_pressed() and isJumping > 0 and isJumping < 3 and c > 0):
        #RTotates character to face left
        if Direction != "Left" and isSpriteNinja and not colorMode:
            # keys.clear_pressed_keys()
            addToScreen(Scene, Stored[0], c, r)
            if Direction == "Down" or Direction == "Up":
                overwriteSpot = mirror(spriteDict["High Res Ninja"])
            else:
                overwriteSpot = mirror(overwriteSpot)
            addToScreenWithoutColor(Scene, overwriteSpot, newBlack, c, r)
            if isJumping == 0:
                printScreen(Scene)
            Direction = "Left"
            continue
        #Place block to left and below if running and pressing q
        if keys.is_q_pressed() and c > 0 and isSpriteNinja:
            checkForBackground = scanArea(Scene, (c - pixelRatio, r-pixelRatio), pixelRatio, pixelRatio)
            if checkForBackground == predefinedSquare:
                #Animate player placing like erase
                addToScreen(Scene, Stored[0], c, r)
                addToScreenWithoutColor(Scene, mirror(spriteDict["High Res Ninja Down"]), newBlack, c, r)
                printScreen(Scene)
                addToScreenWithoutColor(Scene, overwriteSpot, newBlack, c, r)
                # time.sleep(0.1)
                addToScreenWithoutColor(Scene, spriteDict[Inventory[previousNumber]], newBlack, c-pixelRatio, r-pixelRatio)
                if Inventory[previousNumber] in animatingSprites:
                    portalsOnScreen[(cToChange, rToChange)] = [spriteDict[Inventory[previousNumber]], predefinedSquare]
                printScreen(Scene)
            # continue
        # isSpriteNinja = sprites[rc%mod] == "Ninja"
        if Direction != "Left" or Direction == "Left" or isJumping > 0 and isJumping < 3:
            blockToLeft = scanArea(Scene, (c - pixelRatio, r), pixelRatio, pixelRatio)
            itemToCheck = checkForItem(blockToLeft)
            #Check if valid block to go through
            if (blockToLeft == predefinedSquare) or (itemToCheck in passThrough) or erase or (not isSpriteNinja and Pallete == palleteSelection[2]) or colorMode:
                if overwriteSpot == False:
                    Spot = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
                else:
                    Spot = overwriteSpot
                addToScreen(Scene, Stored[0], Stored[1], Stored[2])
                c -= pixelRatio
                if blockToLeft == predefinedSquare and not isSpriteNinja:
                    Stored = addToScreen(Scene, Spot, c, r)
                    overwriteSpot = False
                else:
                    overwriteSpot = Spot
                    Stored = addToScreenWithoutColor(Scene, Spot, newBlack, c, r)
                printScreen(Scene)
                if isJumping > 0:
                    isJumping += 1
                if isJumping > 3:
                    isJumping = 0
            else:
                isJumping = 0
            #Checks if block is a portal to transfer dimensions
            checkPortal(Scene, itemToCheck, c, r)
        keys.keys_pressed.discard(all)
    else:
        isJumping = 0
    #Moving between the whole world not portal travel
    if (keys.is_a_pressed() and c == 0) or (keys.is_d_pressed() and c == sceneWidth - pixelRatio) or (keys.is_w_pressed() and r == sceneLength - globalDisplacement - pixelRatio) or (keys.is_s_pressed() and r == 0):
            blockBelow = scanArea(Scene, (c, r - pixelRatio), pixelRatio, pixelRatio)
            if blockBelow != predefinedSquare or Stored[0] in climbing:
                addToScreen(Scene, Stored[0], c, r)
                direction = ""
                if keys.is_w_pressed(): 
                    direction = "Up"
                    if keys.is_q_pressed() and Stored[0] == predefinedSquare:
                        addToScreenWithoutColor(Scene, spriteDict[Inventory[previousNumber]], newBlack, c, r)
                elif keys.is_s_pressed(): direction = "Down"
                elif keys.is_a_pressed(): direction = "Left"
                elif keys.is_d_pressed(): direction = "Right"
                
                if Direction != direction:
                    if isSpriteNinja and not colorMode:
                        if direction == "Right":
                            overwriteSpot = spriteDict["High Res Ninja"]
                        elif direction == "Left":
                            overwriteSpot = mirror(spriteDict["High Res Ninja"])
                        elif direction == "Down":
                            if Direction == "Left":
                                overwriteSpot = mirror(spriteDict["High Res Ninja Down"])
                            else:
                                overwriteSpot = spriteDict["High Res Ninja Down"]
                        elif direction == "Up":
                            if Direction == "Left" or overwriteSpot == mirror(spriteDict["High Res Ninja Down"]):
                                overwriteSpot = mirror(spriteDict["High Res Ninja Up"])
                            else:
                                overwriteSpot = spriteDict["High Res Ninja Up"]
                        Direction = direction
                        addToScreen(Scene, Stored[0], c, r)
                        addToScreenWithoutColor(Scene, overwriteSpot, newBlack, c, r)
                        printScreen(Scene)
                        time.sleep(.1)
                        continue
                # Check movement between chunks
                Stored = moveScene(Scene, Stored, direction)
                # Direction = "Left"
                isJumping = 0
                if keys.is_q_pressed():
                    scanBlockBelow = scanArea(Scene, (c, r - pixelRatio), pixelRatio, pixelRatio)
                    if scanBlockBelow == predefinedSquare:
                        addToScreenWithoutColor(Scene, spriteDict[Inventory[previousNumber]], newBlack, c, r-pixelRatio)
                        if Inventory[previousNumber] in animatingSprites:
                            portalsOnScreen[(c, r-pixelRatio)] = [spriteDict[Inventory[previousNumber]], predefinedSquare]
                        printScreen(Scene)

    
    #Rotates block
    if keys.is_x_pressed() and not Stored == [] and not erase and not colorMode:
        # If player is looking certain way, then rotate that block
        if isSpriteNinja:
            rScan = 0
            cScan = 0
            if Direction == "Right":
                cScan = pixelRatio
            elif Direction == "Left":
                cScan = -pixelRatio
            elif Direction == "Down":
                rScan = -pixelRatio
            elif Direction == "Up":
                rScan = pixelRatio
            scannedArea = scanArea(Scene, (c + cScan, r + rScan), pixelRatio, pixelRatio)
            if scannedArea != predefinedSquare:
                addToScreen(Scene, rotate(scannedArea, 270), c + cScan, r + rScan)
                printScreen(Scene)
                time.sleep(.1)
        
        else:
            #Allows flipping current sprite
            if overwriteSpot == False:
                overwriteSpot = rotate(spriteDict[sprites[rc%mod]], 270)
            else:
                overwriteSpot = rotate(overwriteSpot, 270)
            # currentBlock = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
            addToScreen(Scene, Stored[0], c, r)
            addToScreenWithoutColor(Scene, overwriteSpot, newBlack, c, r)
            printScreen(Scene)
            time.sleep(.2)
    # Flips block
    if keys.is_f_pressed() and not Stored == [] and not erase and not colorMode:
        if isSpriteNinja:
            rScan = 0
            cScan = 0
            if Direction == "Right":
                cScan = pixelRatio
            elif Direction == "Left":
                cScan = -pixelRatio
            elif Direction == "Down":
                rScan = -pixelRatio
            elif Direction == "Up":
                rScan = pixelRatio
            scannedArea = scanArea(Scene, (c + cScan, r + rScan), pixelRatio, pixelRatio)
            if scannedArea != predefinedSquare:
                addToScreen(Scene, mirror(scannedArea), cScan + c, rScan + r)
                printScreen(Scene)
                time.sleep(.1)
        else:    
            if overwriteSpot == False:
                overwriteSpot = mirror(spriteDict[sprites[rc%mod]])
            else:
                overwriteSpot = mirror(overwriteSpot)
            addToScreen(Scene, Stored[0], c, r)
            addToScreenWithoutColor(Scene, overwriteSpot, newBlack, c, r)
            printScreen(Scene)
            time.sleep(.2)
    #Erases border outline
    elif keys.is_b_pressed() and borderColor == defaultBorder and not Stored == [] and not erase and colorMode:
        addToScreen(Scene, square(pixelRatio,pixelRatio, Pallete[rc%mod]), c, r)
        border = []
        printScreen(Scene)
        borderColor = Pallete[rc%mod]
        overwriteSpot = False
        time.sleep(.1)
    #adds border outline
    elif keys.is_b_pressed() and not Stored == [] and not erase and colorMode:
        printScreen(Scene)
        border = addBorderToArea(Scene, (c, r), pixelRatio, pixelRatio, Pallete[rc%mod], defaultBorder)
        overwriteSpot = False
        borderColor = defaultBorder
        printScreen(Scene)
        time.sleep(.1)

    #Erases block
    if keys.is_e_pressed() and not Stored == [] and not (isSpriteNinja and keys.is_d_pressed() and keys.is_a_pressed()):
        # if isSpriteNinja and (Direction == "Right" or Direction == "Left"):
        #     if c >= len(Scene[0]) - pixelRatio or c <= 0:
        #         continue
        
        # overwriteSpot = False
        # Erases background of scene in order to prepare the white outline
        if Stored[0] != predefinedSquare and erase == True and not isSpriteNinja:
            points += 100
            checkItem = checkForItem(Stored[0], True)
            if checkItem != False:
                if checkItem not in Inventory and checkItem in itemsDict.keys():
                    Inventory.append(checkItem)
                    inventoryChange = True
        #starts to create new scene to create a box with white outline
        borderingBackground = square(pixelRatio + 2, pixelRatio + 2, yellow)
        addToScreen(borderingBackground, predefinedSquare, 1, 1)
        addBorderToColor(borderingBackground, yellow, backgroundColor, white)
        # gets the box with white outline
        borderCreation = scanArea(borderingBackground, (1, 1), pixelRatio, pixelRatio)
        
        #Uses overwriteSpot to overwrite the moving block feature which scans current block to just take the white block
        if not isSpriteNinja:
            overwriteSpot = borderCreation
        if erase == False and not isSpriteNinja:
            #Restores background to orignal content
            addToScreen(Scene, Stored[0], c, r)
            addToScreenWithoutColor(Scene, borderCreation, backgroundColor, c, r)
            Stored = [Stored[0], c, r]
        else:

            #If already in eraser mode and block is erased, then it will add background color to the scene
            #Checks Objecrs in the scene to see if it is an item that has an animation
            
            if isSpriteNinja:
                if Direction == "Right":
                    if c >= len(Scene[0]) - pixelRatio:
                        continue
                    addToScreen(Scene, Stored[0], c, r)
                    addToScreenWithoutColor(Scene, spriteDict["High Res Ninja Up"], newBlack, c, r)
                    printScreen(Scene)
                    time.sleep(.1)
                    addToScreenWithoutColor(Scene, spriteDict["High Res Ninja"], newBlack, c, r)
                    c += pixelRatio
                elif Direction == "Left":
                    if c <= 0:
                        continue
                    addToScreen(Scene, Stored[0], c, r)
                    addToScreenWithoutColor(Scene, mirror(spriteDict["High Res Ninja Up"]), newBlack, c, r)
                    printScreen(Scene)
                    time.sleep(.1)
                    addToScreenWithoutColor(Scene, mirror(spriteDict["High Res Ninja"]), newBlack, c, r)
                    c -= pixelRatio
                elif Direction == "Down":
                    if r <= 0:
                        continue
                    addToScreen(Scene, Stored[0], c, r)
                    if overwriteSpot == spriteDict["High Res Ninja Down"]:
                        addToScreenWithoutColor(Scene, spriteDict["High Res Ninja"], newBlack, c, r)
                    else:
                        addToScreenWithoutColor(Scene, mirror(spriteDict["High Res Ninja"]), newBlack, c, r)
                    printScreen(Scene)
                    time.sleep(.1)
                    addToScreen(Scene, Stored[0], c, r)
                    addToScreenWithoutColor(Scene, overwriteSpot, newBlack, c, r)
                    r -= pixelRatio
                elif Direction == "Up":
                    if r >= sceneLength - 3*pixelRatio:
                        continue
                    addToScreen(Scene, Stored[0], c, r)
                    if overwriteSpot == spriteDict["High Res Ninja Up"]:
                        addToScreenWithoutColor(Scene, spriteDict["High Res Ninja"], newBlack, c, r)
                    else:
                        addToScreenWithoutColor(Scene, mirror(spriteDict["High Res Ninja"]), newBlack, c, r)
                    printScreen(Scene)
                    time.sleep(.1)
                    addToScreen(Scene, Stored[0], c, r)
                    addToScreenWithoutColor(Scene, overwriteSpot, newBlack, c, r)
                    r += pixelRatio
            else:
                addToScreen(Scene, Stored[0], c, r)
                Stored = [predefinedSquare, c, r]
            
            checkIfPortal = addToScreen(Scene, predefinedSquare, c, r)
            itemToCheck = checkForItem(checkIfPortal[0])
            if itemToCheck in animatingSprites:
                del portalsOnScreen[(c, r)]
            #Make elif if dont want to collect animation sprites
            if itemToCheck != False and itemToCheck != "Background":
                points += 100
                if itemToCheck not in Inventory and itemToCheck in itemsDict.keys():
                    Inventory.append(itemToCheck)
                    inventoryChange = True
            # Stored = [predefinedSquare, c, r]
            if isSpriteNinja:
                if Direction == "Right":
                    c -= pixelRatio
                elif Direction == "Left":
                    c += pixelRatio
                elif Direction == "Down":
                    r += pixelRatio
                elif Direction == "Up":
                    r -= pixelRatio 
            
        if not isSpriteNinja:
            #Adds the white outline to the scene
            addToScreenWithoutColor(Scene, borderCreation, backgroundColor, c, r)

            erase = True
        printScreen(Scene)
        # time.sleep(.08)

    #changing colors with Pallete
    elif keys.is_t_pressed() and not erase:
        rc+=1
        if colorMode:
            scaned = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
            colorScanned = changeRGB(scaned, currentColor, Pallete[(rc)%mod])
            currentColor = Pallete[(rc)%mod]
            #Draws rgb if in colorMode not block sprites`
            addToScreen(Scene, colorScanned, c, r)
        else:
            addToScreen(Scene, Stored[0], c, r)
            addToScreenWithoutColor(Scene, spriteDict[sprites[rc%mod]], newBlack, c, r)
            overwriteSpot = spriteDict[sprites[rc%mod]]
            #Causes inventory to change border color around selected sprite
            switchedSprite = True
        isSpriteNinja = False
        printScreen(Scene)
        if not borderColor == defaultBorder and colorMode:
            borderColor = Pallete[rc%mod]
        if not switchedSprite:
            time.sleep(.3)
    elif keys.is_r_pressed() and not erase:
        rc-=1
        if colorMode:
            scaned = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
            colorScanned = changeRGB(scaned, currentColor, Pallete[(rc)%mod])
            currentColor = Pallete[(rc)%mod]
            #Draws rgb if in colorMode not block sprites
            addToScreen(Scene, colorScanned, c, r)
        else:
            addToScreen(Scene, Stored[0], c, r)
            addToScreenWithoutColor(Scene, spriteDict[sprites[rc%mod]], newBlack, c, r)
            overwriteSpot = spriteDict[sprites[rc%mod]]
            #Causes inventory to change border color around selected sprite
            switchedSprite = True
        isSpriteNinja = False
        printScreen(Scene)
        if not borderColor == defaultBorder and colorMode:
            borderColor = Pallete[rc%mod]
        if not switchedSprite:
            time.sleep(.3)
    keys.keys_pressed.discard(all)
t.stop()
portalsOnScreen = {}





# Show cursor
sys.stdout.write("\033[?25h" + reset)
# time.sleep(0.5)
#Create a screen, then add text to it.
saveScrene = screen(sceneLength, sceneWidth, cyan)
# addToScreen(saveScrene, backgrounds.getPixelImage(1), 0, 0)
#Where to place the text
LetterCol = int(sceneWidth/5)
LetterRow = int(sceneLength/1.3)
LetterColor = black
overwrite = addLetter(saveScrene, "Save current Game or Restart?\n{1}'R'{r} to {1}Restart{r}!\n{2}'S'{r} to {2}Save{r}!", LetterColor,  LetterCol, LetterRow)
keys.keys_pressed.discard(all)
printScreen(saveScrene)
# time.sleep(0.5)
while not keys.is_s_pressed():
    if keys.is_r_pressed():
        portalsOnScreen = {}
        itemCol = LetterCol
        itemRow = LetterRow
        for i, sprite in enumerate(overwrite[0]):
            #Replaces what inventory drew over before
            addToScreen(saveScrene, sprite, overwrite[1][i][0], overwrite[1][i][1])
        addLetter(saveScrene, "{1}Restarting...{r}", green, LetterCol, LetterRow)
        printScreen(saveScrene)
        #If dont want to be saved remove the files
        if os.path.exists("Scene.txt"):
            os.remove("Scene.txt")
        if os.path.exists("Inventory.txt"):
            os.remove("Inventory.txt")
        if os.path.exists("Points.txt"):
            os.remove("Points.txt")
        keys.keys_pressed.discard(all)
        #call the program again
        time.sleep(1)
        # t.stop()
        os.system('python3 blocks.py')
        # sys.exit()

for i, sprite in enumerate(overwrite[0]):
    addToScreen(saveScrene, sprite, overwrite[1][i][0], overwrite[1][i][1])
addLetter(saveScrene, "{2}Saved{r}!", LetterColor, LetterCol, LetterRow)
printScreen(saveScrene)

#Save the scene to a file to be loaded later
if Stored != []:
    addToScreen(Scene, Stored[0], c, r)
saveScene(Scene, "Scene.txt", True)
saveScene(Inventory, "Inventory.txt", False)
saveScene([str(points)], "Points.txt", False)
saveScene(InventoryDrawnOver[0], "DrawnOver.txt", True)
saveScene(InventoryDrawnOver[1], "IndexOfDrawnOver.txt", False)
# saveScene(InventoryDrawnOver, "Points.txt", False)
keys.keys_pressed.discard(all)
#Stop the thread
# t.stop()
#Exit the program
sys.exit()

