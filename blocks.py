# import sys, os
# import copy
# current_script_path = os.path.dirname(os.path.abspath(__file__))

# parent_directory = os.path.dirname(current_script_path)

# sys.path.insert(0, parent_directory)

from drawing import *
sys.path.insert(0, './ImageReader')
from keyboardListener import *
resizeWindow()
clear()
backgroundColor = rgb(0, 255, 255)
# backgroundColor = black

#Setting up nether to align with background color
netherLevelIndex = 3
netherLevel = backgroundBig.getPixel(netherLevelIndex)
netherLevel.replacePixels(netherLevel.getPixel(0, 0), backgroundColor)
netherLevel = netherLevel.getImage()
#replacing all sprites to have same background color, as well as background color
chooseBackgroundIndex = 2
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
#initliaze a inventory
#ITem perimeter color
inventoryPerimeterColor = white
Inventory = ["Diamond Pickaxe"]
lastInventory = Inventory
#check if Scene.txt exists and if it does, then it will load the scene
if os.path.exists("Scene.txt"):
    Scene = getScene("Scene.txt")
    Inventory = getScene("Inventory.txt")[0]
    points = getScene("Points.txt")[0]
    # InventoryDrawnOver = getScene("Points")[1]
    points = int(points[0])

    # print(f"{yellow}Inventory: {Inventory} {reset}")
    # print(f"{yellow}Points: {points} {reset}")
    # print(isinstance(Inventory, list))
    # time.sleep(0.25)

else:
    # print(f"{blue} New Game {reset}")
    Scene = screen(pixelRatio*height*scale, pixelRatio*width*scale, backgroundColor)
    #Add predetermined background
    addToScreen(Scene, backgroundBig, 0, 0)
    # InventoryDrawnOver = displayInventory(Scene, Inventory, 0, sceneLength - itemHeight)
    # time.sleep(0.25)
sceneLength = len(Scene)
sceneWidth = len(Scene[0])

#Setting up world travel and dimensions
changedWorld = False
overWorld = backgroundBig
netherWorld = netherLevel
currentWorld = 0
worldToTravel = {
    0: Scene,
    1: netherWorld
}
amountOfWorlds = len(worldToTravel)



# Clear screen and prints it
# clear()
# printScreen(Scene)

# Hide cursor
sys.stdout.write("\033[?25l")
print("\033[?25l", flush=True)



replace = numbers.getPixel(0)
replacePixel = replace.getPixel(0, 0)
replace.replacePixels(replacePixel, backgroundColor)


numbers = replace.getImage()
numbersHeight = 7
numbersWidth = 5
numbersDict = {}
for i in range(0, 11):
    numbersDict[i] = scanArea(numbers, (i*numbersWidth, 0),numbersHeight, numbersWidth)

replace = letters.getPixel()
replacePixel = replace.getPixel(0, 0)
replace.replacePixels(replacePixel, backgroundColor)

letters = replace.getImage()
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
spritesBigTop = ["Ninja", "Ninja Crouch", "Bow Staff Ninja", "Angel"]
SpriteBigTools = ["Sword", "Poke Bowl", "Portal", "Small Weapons"]
SpritesBigBlocks = ["Grass", "Dirt", "Grass Connector", "Window","Stone", "Iron Ore", "Diamond Ore", "Gold Ore", "Emerald Ore", 
                    "Brick","Obsidian","Nether Portal", "Ladder", "Platform", "Door", "Small Portal", "Netherack", "Fire"]
spriteBigDict = {}

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
ItemsLevels = ["Heart","Experience Orb"]
ItemsDecorations = ["Window", "Ladder", "Platform", "Wings", "Door", "Small Portal"]
ItemsBlocks = ["Dirt", "Stone", "Grass", "Grass Connector", "Brick", "Obsidian", "Ninja", "Nether Portal", "Emerald Ore", "Gold Ore", "Netherack"]
ItemsOres = ["Diamond Ore", "Iron Ore", "Gold Ore", "Emerald Ore"]
ItemsTools = ["Diamond Pickaxe", "Wood Sword", "Diamond Pic", "Flint 'n Steel"]

#Scanning the 8x8 sprite sheet and setting each sprite to a dict value
#Corresponding to the sprite name from itemsNames
for i in range(0, len(ItemsLevels)):
    itemsNames.append(ItemsLevels[i])
    itemsDict[ItemsLevels[i]] = scanArea(items, (i*itemWidth, 4*itemHeight), itemHeight, itemWidth)
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


#Setting up sprites for the big sprite sheet
spritesTop = spritesBigTop
spritesMiddle = SpriteBigTools
spritesBottom = SpritesBigBlocks
spriteDict = spriteBigDict





#Scanning the sprite sheet and sets each sprite to a dict valuale 
#Corresponding to the sprite name from sprites
for i in range(0, len(spritesTop)):
    scanned = scanArea(blocks, (i*pixelRatio, pixelRatio*2), pixelRatio, pixelRatio)
    spriteDict[spritesTop[i]] = scanned

for i in range(0, len(spritesMiddle)):
    scanned = scanArea(blocks, (i*pixelRatio, pixelRatio), pixelRatio, pixelRatio)
    spriteDict[spritesMiddle[i]] = scanned

for i in range(0, len(spritesBottom)):
    scanned = scanArea(blocks, (i*pixelRatio, 0), pixelRatio, pixelRatio)
    spriteDict[spritesBottom[i]] = scanned

sprites = []
#Adds each sprite to the sprite list
for i, sprite in enumerate(spriteDict):
    sprites.append(sprite)

#gets the black background color from asperite sprite sheet
# newBlack = getColor(spriteDict[SpriteBigTools[2]], (0, 0))
# print(f"{newBlack}Color:")
# time.sleep(1)


#Blocks a charcter can pass through
passThrough = [predefinedSquare, "Ladder", "Nether Portal", "Platform", "Door", "Small Portal", "Fire"]
Angel = spriteDict["Angel"]
Ninja = spriteDict["Ninja"]



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
def addLetterToScreen(Scene, letter : str, color, col, row):
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
    



#Creating a function to display inventory
def displayInventory(Scene, inventory : list, col, row):
    listofReplacementItems = []
    ColRow = []
    for item in inventory:
        # listofReplacementItems.append(addToScreenWithoutColor(Scene, addPerimeter(itemsDict[item], inventoryPerimeterColor), newBlack, col, row)[0])
        # addToScreenWithoutColor(itemsDict[item], [f"{yellow} {}"]
        ColRow.append([col, row])
        listofReplacementItems.append(addToScreenWithoutColor(Scene, itemsDict[item], newBlack, col, row)[0])
        col += itemWidth
        if col >= sceneWidth:
            col = 0
            row -= itemHeight
    return [listofReplacementItems, ColRow]

InventoryDrawnOver = displayInventory(Scene, Inventory, 0, sceneLength - itemHeight)



numDrawnOver = addNumToScreen(Scene, 0, 0, 0)
#create dictionary of length of spriteDict and set each sprite to a number
MapMaker = dict()
for i, sprite in enumerate(spriteDict):
    MapMaker[i] = sprite





#Setting up color palletes or sprite pallete
palletes = [rainbow, rainbow_bright, spriteDict, itemsDict]
pallateStart = 0
# initliazes pallet
Pallete = palletes[pallateStart]

#Mode for drawing in colors or sprite blocks
colorMode = True
# Sets length of modulus when getting pallete
if colorMode:
    mod = len(Pallete)
else:
    mod = len(sprites)










# Start keyboard listener
keys = MyKeyListener()
listener = keyboard.Listener(
    on_press=keys.on_press,
    on_release=keys.on_release
)
listener.start()
#Pallete start Color
rc = 0

#Initializes backup for pressing 'z' to get back to previous screen
drawnOver = Scene

currentColor = Pallete[rc%mod]
borderColor = Pallete[(rc)%mod]
defaultBorder = grey
border = []
Stored = []
erase = False
# for x in range(0, 8):
#     addBorderToArea(Scene, (0+x, 0+x), sceneLength-x, sceneWidth-x, backgroundColor, Pallete[x%mod])
# addBorderToArea(Scene, (1, 1), sceneLength-1, sceneWidth-1, backgroundColor, red)

# newBlack = rgb(0, 0, 0)
# print(f"{newBlack}Color:")
# time.sleep(1)
printScreen(Scene)
# first = True   
 



#Starting position for moving sprite
r = 4*pixelRatio
c = 4*pixelRatio
overwriteSpot = False
# Stored = [spriteDict["Ninja"], c, r]

def printCurrentPos(row = r, col = c, color = Pallete[rc%mod], borderColor = Pallete[rc%mod], erase = False):
    if erase == True:
        erase = "On"
    else:
        erase = "Off"
    print("Screen Height: ", sceneLength, " Screen Width: ", sceneWidth,  "  "*10, "\n",
         "Current Position: ", "  "*10, "\n",
          "Row: ", row, " Column: ", col, "  "*10, "\n",
          "Current Color: ", color, "  ", reset, " "*10, "\n",
          "Border Color: ", borderColor, "  ", reset, " "*10, "\n",
          "Eraser: ", erase, "  "*10, "\n", flush = True)

first = True
inventoryChange = False
#Checks all the rotations of the block and its flips to see if a spriteDict sprite is in the itemsDict and returns the key
def checkForItem(item, checkIfCollectible = False):
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


#Create a function to chekc interaction with portal
def checkPortal(Scene, itemToCheck, c, r):
    if not erase and not colorMode and itemToCheck == "Small Portal" and sprites[rc%mod] == "Ninja":
        addToScreen(Scene, Stored[0], c, r)
        #Saves current screen to world
        global currentWorld
        global worldToTravel
        global inventoryChange
        global changedWorld
        global portalsOnScreen
        worldToTravel[currentWorld] = [[item for item in sublist] for sublist in Scene]
        inventoryChange = True
        changedWorld = True
        # worldToTravel[currentWorld] = copy.deepcopy(Scene)
        currentWorld += 1
        #Go back to original world
        currentWorld = currentWorld%amountOfWorlds
        #Add the new world to the screen
        addToScreenWithColor(Scene, spriteDict["Ninja"], newBlack, c, r)
        printScreen(Scene)
        time.sleep(1)
        addToScreen(Scene, worldToTravel[currentWorld], 0, 0)
        addToScreenWithoutColor(Scene, Stored[0], newBlack, c, r)
        #Resets the portal on screen
        portalsOnScreen = {}
        scanForPortal(Scene, pixelRatio)
        addToScreenWithoutColor(Scene, spriteDict["Ninja"], newBlack, c, r)
        printScreen(Scene)
        print("Current World: ", currentWorld, "                    ")
#Defining types of sprites that are in the background, as in can pass through on fall
SpritesInBackground = [predefinedSquare, spriteDict["Small Portal"], spriteDict["Fire"], mirror(spriteDict["Small Portal"]), mirror(spriteDict["Fire"])]
#CReate a function to move charcter down if it is on a background color of predefinedSquare
def checkGravity(Scene, blockBelow, Stored, c, r, pixelRatio, overwriteSpot):
    #Checks if blockBewlow is a predefinedSquare and if it is not a ladder (a block that the character can hold onto)
    if blockBelow in SpritesInBackground and checkForItem(Stored[0]) not in ["Ladder"]:
        # printScreen(Stored[0])
        # time.sleep(1)
        currentBlock = addToScreen(Scene, Stored[0], c, r)[0]
        r -= pixelRatio
        Stored = addToScreenWithoutColor(Scene, spriteDict["Ninja"], newBlack, c, r)
        printScreen(Scene)
        time.sleep(0.1)
        return [r, Stored]
    return [r, Stored]

#Starts the portal checker for animation
import threading
class CheckPortalThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.stop_flag = False

    def run(self):
        while not self.stop_flag:
            time.sleep(1)
            self.checkPortal()

    def stop(self):
        self.stop_flag = True

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
t = CheckPortalThread()
t.start()
# print("Started Portal Thread")

#If want to play with micro blocks uncomment
# pixelRatio = 8
# spriteDict = itemsDict
# sprites = itemsNames
# Scene = screen(pixelRatio*height*scale, pixelRatio*width*scale, backgroundColor)
isJumping = False
for i in range(1, 4):
    addToScreenWithoutColor(Scene, itemsDict["Heart"], newBlack, sceneWidth - i*itemWidth, sceneLength - itemHeight-1)
    addToScreenWithoutColor(Scene, itemsDict["Experience Orb"], newBlack, sceneWidth - i*itemWidth, sceneLength - 2*itemHeight-2)

#Add names of sprites that will be animated by flipping them
animatingSprites = ["Small Portal", "Fire"]
#Check if any of the animating sprites are on screen
def scanForPortal(Scene, pixelRatio):
    global portalsOnScreen
    i, j = 0, 0
    while i < len(Scene):
        while j < len(Scene[i]):
            blocksScanned = scanArea(Scene, (j, i), pixelRatio, pixelRatio)
            #Checks if block is an animation sprite
            typeOfBlock = checkForItem(blocksScanned)
            if typeOfBlock in animatingSprites:
                portalsOnScreen[(j, i)] = [blocksScanned, predefinedSquare]
            j += pixelRatio
        i += pixelRatio
        j = 0


scanForPortal(Scene, pixelRatio)

# Start of engine
while not keys.is_esc_pressed():
    # Checking gravity by looking at block below
    if not erase and spriteDict[sprites[rc%mod]] == spriteDict["Ninja"] and not colorMode:
        #PRevents from fsalling immediately if have momentum fro moving left or right
        if not (isJumping > 0 and isJumping < 3 and (keys.is_d_pressed() or keys.is_a_pressed())):
            #To Preven moving side to side while falling, probably not needede as 
            if isJumping > 0:
                isJumping = 0
            blockBelow = scanArea(Scene, (c, r - pixelRatio), pixelRatio, pixelRatio)
            # if blockBelow == spriteDict["Platform"]:
            #     isJumping = 0
            #     # continue
            # Glitch where if wings in inventory then it will not stop on block
            results = checkGravity(Scene, blockBelow, Stored, c, r, pixelRatio, overwriteSpot)
            if r != results[0] or blockBelow == spriteDict["Fire"] or blockBelow == mirror(spriteDict["Fire"]):
                r = results[0]
                Stored = results[1]
                #Checks if block is a portal to transfer dimensions
                checkPortal(Scene, checkForItem(Stored[0]), c, r)
                #allows continous falling of block (might change)
                if "Wings" not in Inventory:
                    continue
                else:
                    #Resets left and right movement while falling if on block, prevents glitch where cant double jump
                    if scanArea(Scene, (c, r - pixelRatio), pixelRatio, pixelRatio) not in SpritesInBackground:
                    #     printScreen(scanArea(Scene, (c, r - pixelRatio), pixelRatio, pixelRatio))
                    #     time.sleep(1)
                          isJumping = 0
                    #If on air allows to move left or right with wings
                    #Movement of two blocks with wings
                    else:
                        isJumping = 2
            else:
                isJumping = 0
    if "Wings" in Inventory and spriteDict["Ninja"] != Angel and not colorMode and not erase:
        spriteDict["Ninja"] = Angel
        overwriteSpot = Angel
        addToScreen(Scene, Stored[0], c, r)
        addToScreenWithoutColor(Scene, Angel, newBlack, c, r)
        printScreen(Scene)
    elif "Wings" not in Inventory and spriteDict["Ninja"] == Angel and not colorMode and not erase:
        spriteDict["Ninja"] = Ninja
        overwriteSpot = Ninja
        addToScreen(Scene, Stored[0], c, r)
        addToScreenWithoutColor(Scene, Ninja, newBlack, c, r)
        printScreen(Scene)
    #Scoreboard updates
    if lastPoints != points or changedWorld:
        if not changedWorld:
            for i, sprite in enumerate(numDrawnOver[0]):
                #Replaces what numbers drew over before
                addToScreen(Scene, sprite, numDrawnOver[1][i][0], numDrawnOver[1][i][1])
        else:
            changedWorld = False
        #adds new number to screen
        numDrawnOver = addNumToScreen(Scene, points, 0, 0)
        printScreen(Scene)
        lastPoints = points
    #Inventory updates
    if lastInventory != Inventory or inventoryChange:
        itemRow = sceneLength - itemHeight
        itemCol = 0
        #Sort by name
        Inventory.sort()
        for i, sprite in enumerate(InventoryDrawnOver[0]):
            #Replaces what inventory drew over before
            addToScreen(Scene, sprite, InventoryDrawnOver[1][i][0], InventoryDrawnOver[1][i][1])
            # itemCol += 1
            # #If itemCol is greater than sceneWidth, then it will go to next row
            # if itemCol*itemWidth >= sceneWidth:
            #     itemCol = 0
            #     itemRow -= itemHeight
        #adds new inventory to screen
        InventoryDrawnOver = displayInventory(Scene, Inventory, 0, sceneLength - itemHeight)
        printScreen(Scene)
        lastInventory = Inventory
        inventoryChange = False
    
    if keys.is_j_pressed():
        #add a random item from the itemsDict to the inventory
        Inventory.append(itemsNames[random.randint(0, len(itemsNames)-1)])
        inventoryChange = True
        time.sleep(.05)
        keys.keys_pressed.discard(all)
    elif keys.is_m_pressed():
        Inventory.append("Wings")
        inventoryChange = True
        time.sleep(.05)
        keys.keys_pressed.discard(all)

    if keys.is_i_pressed():
        print(f"{purple}Inventory: {Inventory}{reset}")
        print(f"{blue}Portals: {portalsOnScreen}{reset}")
        time.sleep(.1)
        keys.keys_pressed.discard(all)

    if keys.is_k_pressed():
        if Inventory != []:
            Inventory.pop()
            inventoryChange = True
        time.sleep(.05)
        keys.keys_pressed.discard(all)




    #Clears the screen
    if keys.is_c_pressed():
        if not Stored == []:
            addToScreen(Scene, Stored[0], c, r)
        drawnOver = clearScreen(Scene, backgroundColor)
        clear()
        printScreen(Scene)
        Stored = []
        erase = True
        portalsOnScreen = {}
        time.sleep(.1)
    #undoes clear screen
    if keys.is_z_pressed() and not drawnOver == []:
        for i, row in enumerate(Scene):
            for j, col in enumerate(row):
                Scene[i][j] = drawnOver[i][j]
        drawnOver = []
        scanForPortal(Scene, pixelRatio)
        printScreen(Scene)
        time.sleep(.1)
        
    # Placing the block, super crucial
    elif keys.is_q_pressed() or first:
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
        Spot = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
        printScreen(Scene)        
        time.sleep(.1)
        keys.keys_pressed.discard(all)

    #information about location of block and size of screen
    #Work on later for other feature as it is deprecated can do other information
    # elif keys.is_i_pressed():
    #     printScreen(Scene)
    #     time.sleep(.1)
    #     keys.keys_pressed.discard(all)
    
    #Changing to ninja
    if keys.is_space_pressed() and not Stored == []:
        erase = False
        if colorMode:
            colorMode = False
        addToScreen(Scene, Stored[0], c, r)
        addToScreenWithoutColor(Scene, spriteDict["Ninja"], newBlack, c, r)
        while (sprites[rc%mod] != "Ninja"):
            rc+=1
        rc = rc%mod
        overwriteSpot = spriteDict["Ninja"]
        printScreen(Scene)
        # time.sleep(.1)


    #changing color pallete
    if keys.is_p_pressed():
        overwriteSpot = False
        mod = 7
        pallateStart+=1
        Pallete = palletes[pallateStart%2]
        if not colorMode:
            addToScreen(Scene, square(pixelRatio, pixelRatio, Pallete[rc%mod]), c, r)
        colorMode = True
        #changs from rainbow palletes to sprite palletes
        scaned = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
        colorScanned = changeRGB(scaned, currentColor, Pallete[(rc)%mod])
        currentColor = Pallete[(rc)%mod]
        borderColor = Pallete[rc%mod]

        addToScreen(Scene, colorScanned, c, r)
        printScreen(Scene)
        time.sleep(0.2)

    #Changes pallets to sprite blocks
    if keys.is_y_pressed() and colorMode or first:
        if erase == True:
            erase = False
        overwriteSpot = False
        colorMode = False
        scannedArea = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
        Pallete = palletes[2]
        mod = len(sprites)
        # Checks if not on background color. If not, then it will add the block to the screen
        if not scannedArea == predefinedSquare: 
            addToScreen(Scene, Stored[0], c, r)
        addToScreenWithoutColor(Scene, spriteDict[sprites[rc%mod]], newBlack, c, r)
        if first:
            first = False
        overwriteSpot = spriteDict[sprites[rc%mod]]
        printScreen(Scene)
        
    #moving blocks around
    #Up and Down
    if keys.is_w_pressed() and r < sceneLength - pixelRatio and not Stored == [] and isJumping < 1:
        blockAbove = scanArea(Scene, (c, r + pixelRatio), pixelRatio, pixelRatio)
        # blockBelow = scanArea(Scene, (c, r - pixelRatio), pixelRatio, pixelRatio)
        # if blockBelow in SpritesInBackground:
        #     continue
        itemToCheck = checkForItem(blockAbove)
        isSpriteNinja = sprites[rc%mod] == "Ninja"
        if (blockAbove == predefinedSquare) or (itemToCheck in passThrough) or erase or (not isSpriteNinja and Pallete == palletes[2]) or colorMode:
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
    #Moves Down
    elif keys.is_s_pressed() and r > 0 and not Stored == []:
        blockDown = scanArea(Scene, (c, r - pixelRatio), pixelRatio, pixelRatio)
        itemToCheck = checkForItem(blockDown)
        isSpriteNinja = sprites[rc%mod] == "Ninja"
        if (blockDown == predefinedSquare) or (itemToCheck in passThrough) or erase or (not isSpriteNinja and Pallete == palletes[2]) or colorMode:
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
        blockToRight = scanArea(Scene, (c + pixelRatio, r), pixelRatio, pixelRatio)
        itemToCheck = checkForItem(blockToRight)
        isSpriteNinja = sprites[rc%mod] == "Ninja"
        if (blockToRight == predefinedSquare) or (itemToCheck in passThrough) or erase or (not isSpriteNinja and Pallete == palletes[2]) or colorMode:
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
        keys.keys_pressed.discard(all)
    elif keys.is_a_pressed() and c > 0 and not Stored == [] or (keys.is_a_pressed() and isJumping > 0 and isJumping < 3 and c > 0):
        blockToLeft = scanArea(Scene, (c - pixelRatio, r), pixelRatio, pixelRatio)
        itemToCheck = checkForItem(blockToLeft)
        isSpriteNinja = sprites[rc%mod] == "Ninja"
        #Check if valid block to go through
        if (blockToLeft == predefinedSquare) or (itemToCheck in passThrough) or erase or (not isSpriteNinja and Pallete == palletes[2]) or colorMode:
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
    #Rotates block
    if keys.is_x_pressed() and not Stored == [] and not erase and not colorMode and sprites[rc%mod] != "Ninja":
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
    if keys.is_e_pressed() and not Stored == []:
        overwriteSpot = False
        # Erases background of scene in order to prepare the white outline
        if Stored[0] != predefinedSquare and erase == True:
            points += 100
            checkItem = checkForItem(Stored[0], True)
            if checkItem != False:
                Inventory.append(checkItem)
                inventoryChange = True
        #starts to create new scene to create a box with white outline
        borderingBackground = square(pixelRatio + 2, pixelRatio + 2, yellow)
        addToScreen(borderingBackground, predefinedSquare, 1, 1)
        addBorderToColor(borderingBackground, yellow, backgroundColor, white)
        # gets the box with white outline
        borderCreation = scanArea(borderingBackground, (1, 1), pixelRatio, pixelRatio)
        #Restores background to orignal content
        addToScreen(Scene, Stored[0], c, r)
        #Uses overwriteSpot to overwrite the moving block feature which scans current block to just take the white block
        overwriteSpot = borderCreation
        if erase == False:
            addToScreen(Scene, Stored[0], c, r)
            # addToScreenWithoutColor(Scene, borderCreation, backgroundColor, c, r)
            Stored = [Stored[0], c, r]
        else:
            #If already in eraser mode and block is erased, then it will add background color to the scene
            #Checks Objecrs in the scene to see if it is an item that has an animation
            checkIfPortal = addToScreen(Scene, predefinedSquare, c, r)
            if checkForItem(checkIfPortal[0]) in animatingSprites:
                del portalsOnScreen[(c, r)]
            Stored = [predefinedSquare, c, r]
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
        printScreen(Scene)
        if not borderColor == defaultBorder and colorMode:
            borderColor = Pallete[rc%mod]
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

        printScreen(Scene)
        if not borderColor == defaultBorder and colorMode:
            borderColor = Pallete[rc%mod]
        time.sleep(.3)

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
overwrite = addLetterToScreen(saveScrene, "Save current Game or Restart?\n{1}'R'{r} to {1}Restart{r}!\n{2}'S'{r} to {2}Save{r}!", LetterColor,  LetterCol, LetterRow)
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
        addLetterToScreen(saveScrene, "{1}Restarting...{r}", green, LetterCol, LetterRow)
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
addLetterToScreen(saveScrene, "{2}Saved{r}!", LetterColor, LetterCol, LetterRow)
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

