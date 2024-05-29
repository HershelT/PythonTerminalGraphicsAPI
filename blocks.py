from drawing import *
sys.path.insert(0, 'ImageReader')
from keyboardListener import *
backgroundColor = rgb(0, 95, 135)
# backgroundColor = black

#replacing all sprites to have same background color
newBlack = toolsBig.getPixel(0)
colorNew = newBlack.getPixel(0, 0)
newBlack.replacePixels(colorNew, backgroundColor)
spriteSheet = newBlack.getImage()

#Sets newBlack as the go to background color
newBlack = newBlack.getPixel(0, 0)
newBlack = getColorFromAnsi(newBlack)



#initliaze a screen size
backgroundColor = newBlack
pixelRatio = 16
height = 12
width = 16
scale = 1
Scene = screen(pixelRatio*height*scale, pixelRatio*width*scale, backgroundColor)




# Clear screen and prints it
clear()
printScreen(Scene)

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

#creating function to add numbers to screen starting from any area
def addNumToScreen(Scene, num, col, row):
    stringNum = str(num)
    listOfReplacement = []
    for char in stringNum:
        #adds all the places that were drawn over
        listOfReplacement.append(addToScreenWithoutColor(Scene, numbersDict[int(char)], newBlack, col, row)[0])
        col += numbersWidth
    return [listOfReplacement, col, row]





#Setting up sprites
spritesTop = ["Grass", "Dirt", "Stone", "Gold Ore", "Iron Ore", "Diamond Ore", "Water", "Log", "Leaf", "Birch Plank", "TNT"]
spritesMiddle = ["leftBed", "rightBed", "Brewing Stand", "Cactus", "Ladder", "LeftBoat", "RightBoat", "LeftSpider", "RightSpider",  "HumanBottom", "HumanTop"]
spritesBottom = ["Pickaxe", "Sword", "Shovel", "Axe"]
spriteDict = {}

#Adding sprites as new ones get drawn
blocks = spriteSheet
spritesBigTop = ["Ninja", "Ninja Crouch", "Bow Staff Ninja"]
SpriteBigTools = ["Sword", "Poke Bowl", "Shield"]
SpritesBigBlocks = ["Grass", "Dirt", "Grass Connector", "Window","Stone"]
spriteBigDict = {}


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



#gets the black background color from asperite sprite sheet
# newBlack = getColor(spriteDict[SpriteBigTools[2]], (0, 0))
# print(f"{newBlack}Color:")
# time.sleep(1)

addToScreen(Scene, backgroundBig.getPixelImage(0), 0, 0)
numDrawnOver = addNumToScreen(Scene, 0, 0, 0)
#create dictionary of length of spriteDict and set each sprite to a number
MapMaker = dict()
for i, sprite in enumerate(spriteDict):
    MapMaker[i] = sprite




sprites = []
#Adds each sprite to the sprite list
for i, sprite in enumerate(spriteDict):
    sprites.append(sprite)
#Setting up color palletes or sprite pallete
palletes = [rainbow, rainbow_bright, spriteDict]
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
sceneLength = len(Scene)
sceneWidth = len(Scene[0])
# for x in range(0, 8):
#     addBorderToArea(Scene, (0+x, 0+x), sceneLength-x, sceneWidth-x, backgroundColor, Pallete[x%mod])
# addBorderToArea(Scene, (1, 1), sceneLength-1, sceneWidth-1, backgroundColor, red)

# newBlack = rgb(0, 0, 0)
# print(f"{newBlack}Color:")
# time.sleep(1)
printScreen(Scene)
# first = True    
#Where block gets created
r = sceneLength-pixelRatio
c = 0
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

lastPoints = 0
points = 0

# Start of engine
while not keys.check_keys():
    #Scoreboard updates
    if lastPoints != points:
        for i, sprite in enumerate(numDrawnOver[0]):
            #Replaces what numbers drew over before
            addToScreen(Scene, sprite, i*numbersWidth, numDrawnOver[2])
        #adds new number to screen
        numDrawnOver = addNumToScreen(Scene, points, 0, 0)
        printScreen(Scene)
        lastPoints = points
    
    #Clears the screen
    if keys.is_c_pressed():
        if not Stored == []:
            addToScreen(Scene, Stored[0], c, r)
        drawnOver = clearScreen(Scene, backgroundColor)
        clear()
        printScreen(Scene)
        Stored = []
        time.sleep(.1)
    #undoes clear screen
    if keys.is_z_pressed() and not drawnOver == []:
        for i, row in enumerate(Scene):
            for j, col in enumerate(row):
                Scene[i][j] = drawnOver[i][j]
        drawnOver = []
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
        if not scannedArea == square(pixelRatio, pixelRatio, backgroundColor): 
            addToScreen(Scene, Stored[0], c, r)
        addToScreenWithoutColor(Scene, spriteDict[sprites[rc%mod]], newBlack, c, r)
        if first:
            first = False
        overwriteSpot = spriteDict[sprites[rc%mod]]
        printScreen(Scene)
        
    #moving blocks around
    #Up and Down
    if keys.is_w_pressed() and r < sceneLength - pixelRatio and not Stored == []:
        if overwriteSpot == False:
            Spot = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
        else:
            Spot = overwriteSpot
        addToScreen(Scene, Stored[0], Stored[1], Stored[2])
        r += pixelRatio
        if scanArea(Scene, (c, r), pixelRatio, pixelRatio) == square(pixelRatio, pixelRatio, backgroundColor):
            Stored = addToScreen(Scene, Spot, c, r)
            overwriteSpot = False
        else:
            overwriteSpot = Spot
            Stored = addToScreenWithoutColor(Scene, Spot, newBlack, c, r)
        printScreen(Scene)
        # time.sleep(.1)
        keys.keys_pressed.discard(all)
    #Moves Down
    elif keys.is_s_pressed() and r > 0 and not Stored == []:
        if overwriteSpot == False:
            Spot = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
        else:
            Spot = overwriteSpot
        addToScreen(Scene, Stored[0], Stored[1], Stored[2])
        r -= pixelRatio
        if scanArea(Scene, (c, r), pixelRatio, pixelRatio) == square(pixelRatio, pixelRatio, backgroundColor):
            Stored = addToScreen(Scene, Spot, c, r)
            overwriteSpot = False
        else:
            overwriteSpot = Spot
            Stored = addToScreenWithoutColor(Scene, Spot, newBlack, c, r)
        printScreen(Scene)

        keys.keys_pressed.discard(all)
    #Left and Right
    elif keys.is_d_pressed() and c < len(Scene[0]) - pixelRatio and not Stored == []:
        if overwriteSpot == False:
            Spot = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
        else:
            Spot = overwriteSpot
        addToScreen(Scene, Stored[0], Stored[1], Stored[2])
        c += pixelRatio
        if scanArea(Scene, (c, r), pixelRatio, pixelRatio) == square(pixelRatio, pixelRatio, backgroundColor):
            Stored = addToScreen(Scene, Spot, c, r)
            overwriteSpot = False
        else:
            overwriteSpot = Spot
            Stored = addToScreenWithoutColor(Scene, Spot, newBlack, c, r)
        printScreen(Scene)

        keys.keys_pressed.discard(all)
    elif keys.is_a_pressed() and c > 0 and not Stored == []:
        if overwriteSpot == False:
            Spot = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
        else:
            Spot = overwriteSpot
        addToScreen(Scene, Stored[0], Stored[1], Stored[2])
        c -= pixelRatio
        if scanArea(Scene, (c, r), pixelRatio, pixelRatio) == square(pixelRatio, pixelRatio, backgroundColor):
            Stored = addToScreen(Scene, Spot, c, r)
            overwriteSpot = False
        else:
            overwriteSpot = Spot
            Stored = addToScreenWithoutColor(Scene, Spot, newBlack, c, r)
        printScreen(Scene)

        keys.keys_pressed.discard(all)

    #Rotates block
    if keys.is_x_pressed() and not Stored == [] and not erase:
        currentBlock = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
        addToScreen(Scene, rotate(currentBlock, 270), c, r)
        printScreen(Scene)
        time.sleep(.2)
    # Flips block
    if keys.is_f_pressed() and not Stored == [] and not erase:
        currentBlock = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
        addToScreen(Scene, mirror(currentBlock), c, r)
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
        if Stored[0] != square(pixelRatio, pixelRatio, backgroundColor) and erase == True:
            points += 100
        #starts to create new scene to create a box with white outline
        borderingBackground = square(pixelRatio + 2, pixelRatio + 2, yellow)
        addToScreen(borderingBackground, square(pixelRatio, pixelRatio, backgroundColor), 1, 1)
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
            addToScreen(Scene, square(pixelRatio, pixelRatio, backgroundColor), c, r)
            Stored = [square(pixelRatio, pixelRatio, backgroundColor), c, r]
        #Adds the white outline to the scene
        addToScreenWithoutColor(Scene, borderCreation, backgroundColor, c, r)

        erase = True
        printScreen(Scene)
        time.sleep(.05)

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








# Show cursor
sys.stdout.write("\033[?25h" + reset)