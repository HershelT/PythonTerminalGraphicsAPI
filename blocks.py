from drawing import *
sys.path.insert(0, 'ImageReader')
from keyboardListener import *
backgroundColor = cyan

#replacing all sprites to have same background color
newBlack = toolsBig.getPixel(0)
# newBlack.setPixel(0, 0, backgroundColor)
colorNew = newBlack.getPixel(0, 0)
newBlack.replacePixels(colorNew, backgroundColor)
spriteSheet = newBlack.getImage()

#Sets newBlack as the go to background color
newBlack = newBlack.getPixel(0, 0)
newBlack = getColorFromAnsi(newBlack)



#initliaze a screen size
backgroundColor = newBlack
pixelRatio = 16
Scene = screen(pixelRatio*10, pixelRatio*14, backgroundColor)




# Clear screen and prints it
clear()
printScreen(Scene)

# Hide cursor
sys.stdout.write("\033[?25l")






#Setting up sprites
sprites = ["Grass", "Dirt", "Stone", "Gold Ore", "Iron Ore", "Diamond Ore", "Water", "Log", "Leaf", "Birch Plank", "TNT"]
spritesBottom = ["leftBed", "rightBed", "Brewing Stand", "Cactus", "Ladder", "LeftBoat", "RightBoat", "LeftSpider", "RightSpider",  "HumanBottom", "HumanTop"]
SpritesTool = ["Pickaxe", "Sword", "Shovel", "Axe"]
spriteDict = {}

# toolsBig.getPixel(0).replacePixels(newBlack, backgroundColor)
# spriteSheet = toolsBig.getPixel(0)
# spriteSheet = spriteSheet.replacePixels(newBlack, backgroundColor)
blocks = spriteSheet
spritesBigTop = ["Ninja"]
SpriteBigTools = ["Sword", "Poke Bowl", "Shield"]
SpritesBigBlocks = ["Grass"]
spriteBigDict = {}

# newBlack = toolsBig.getPixel(0).getPixel(0, 0)
# print(reset)
# print(f"{newBlack}Color:")
# time.sleep(1)



sprites = spritesBigTop
spritesBottom = SpriteBigTools
SpritesTool = SpritesBigBlocks
spriteDict = spriteBigDict





#Scanning the sprite sheet and sets each sprite to a dict valuale 
#Corresponding to the sprite name from sprites
for i in range(0, len(sprites)):
    scanned = scanArea(blocks, (i*pixelRatio, pixelRatio*2), pixelRatio, pixelRatio)
    spriteDict[sprites[i]] = scanned

for i in range(0, len(spritesBottom)):
    scanned = scanArea(blocks, (i*pixelRatio, pixelRatio), pixelRatio, pixelRatio)
    spriteDict[spritesBottom[i]] = scanned

for i in range(0, len(SpritesTool)):
    scanned = scanArea(blocks, (i*pixelRatio, 0), pixelRatio, pixelRatio)
    spriteDict[SpritesTool[i]] = scanned



#gets the black background color from asperite sprite sheet
# newBlack = getColor(spriteDict[SpriteBigTools[2]], (0, 0))
# print(f"{newBlack}Color:")
# time.sleep(1)




#Prints each sprite to the screen
start = 0
partition = 8
j = 0
for i, sprite in enumerate(spriteDict):
    if i %partition == 0 and not i == 0:
        j = 0
        start += pixelRatio
    if i == 3:
        # addToScreen(Scene, spriteDict[sprite], j*pixelRatio, start)
        addToScreenWithoutColor(Scene, spriteDict[sprite], rgb(0, 175, 0), j*pixelRatio, start)
        addToScreenWithoutColor(Scene, spriteDict[sprite], rgb(0, 95, 0), j*pixelRatio + pixelRatio, start)
        addToScreenWithoutColor(Scene, spriteDict[sprite], rgb(0, 135, 0), j*pixelRatio + pixelRatio*2, start)
    else:
        addToScreenWithoutColor(Scene, spriteDict[sprite], red, j*pixelRatio, start)
    j+=1

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

drawnOver = []
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
addToScreenWithoutColor(Scene, spriteDict[SpriteBigTools[2]], newBlack, 16, 0)
printScreen(Scene)

#Where block gets created
r = sceneLength-pixelRatio
c = 0
overwriteSpot = False

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
    
# Start of engine
while not keys.check_keys():
    #Clears the screen
    if keys.is_c_pressed():
        drawnOver = clearScreen(Scene, backgroundColor)
        clear()
        printScreen(Scene)
        # printCurrentPos(r, c, Pallete[rc%mod], borderColor, erase)
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
    elif keys.is_q_pressed():
        if colorMode:
            # if not Stored == []:
            #     addToScreen(Scene, Stored[0], Stored[1], Stored[2])
                # r = sceneLength-pixelRatio
                # c = 0
            # border = addBorderToArea(Scene, (c, r), pixelRatio, pixelRatio, Pallete[rc%mod], defaultBorder)
            Stored = addToScreen(Scene, square(pixelRatio, pixelRatio, Pallete[rc%mod]), c, r)
        else:
            currentThing = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
            Stored = [currentThing, c, r]  
        if erase == True:
            Stored = [square(pixelRatio,pixelRatio, backgroundColor), c, r]
            erase = False
        if not border == [] and colorMode:
            border = addBorderToArea(Scene, (c, r), pixelRatio, pixelRatio, Pallete[rc%mod], defaultBorder)
        Spot = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
        
        printScreen(Scene)
        # printCurrentPos(r, c, Pallete[rc%mod], borderColor, erase)
        time.sleep(.1)
        keys.keys_pressed.discard(all)

    elif keys.is_o_pressed():
        if colorMode:
            # if not Stored == []:
            #     addToScreen(Scene, Stored[0], Stored[1], Stored[2])
                # r = sceneLength-pixelRatio
                # c = 0
            # border = addBorderToArea(Scene, (c, r), pixelRatio, pixelRatio, Pallete[rc%mod], defaultBorder)
            Stored = addToScreen(Scene, square(pixelRatio, pixelRatio, Pallete[rc%mod]), c, r)
        else:
            addToScreen(Scene, spriteDict[sprites[rc%mod]], c, r)
            Stored =  [spriteDict[sprites[rc%mod]], c, r]
            # addToScreen(Scene, Stored[0], c, r)
        if erase == True:
            Stored = [square(pixelRatio,pixelRatio, backgroundColor), c, r]
            erase = False
        if not border == [] and colorMode:
            border = addBorderToArea(Scene, (c, r), pixelRatio, pixelRatio, Pallete[rc%mod], defaultBorder)
        Spot = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
        
        printScreen(Scene)
        # printCurrentPos(r, c, Pallete[rc%mod], borderColor, erase)
        time.sleep(.1)
        keys.keys_pressed.discard(all)

    #information about location of block and size of screen
    elif keys.is_i_pressed():
        printScreen(Scene)
        # printCurrentPos(r, c, Pallete[rc%mod], borderColor, erase)
        time.sleep(.1)
        keys.keys_pressed.discard(all)
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
        # printCurrentPos(r, c, currentColor, borderColor, erase )
        time.sleep(0.2)
    #Changes pallets to sprite blocks
    if keys.is_y_pressed() and colorMode:
        if erase == True:
            erase = False
        overwriteSpot = False
        colorMode = False
        Pallete = palletes[2]
        mod = len(sprites)
        # Checks if not on background color. If not, then it will add the block to the screen
        if not scanArea(Scene, (c, r), pixelRatio, pixelRatio) == square(pixelRatio, pixelRatio, backgroundColor):
            addToScreen(Scene, Stored[0], c, r)
        addToScreenWithoutColor(Scene, spriteDict[sprites[rc%mod]], newBlack, c, r)
        printScreen(Scene)
        # printCurrentPos(r, c, currentColor, borderColor, erase )



            


    #moving block around
    #Up and Down
    if keys.is_w_pressed() and r < sceneLength - pixelRatio and not Stored == []:
        if overwriteSpot == False:
            Spot = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
        else:
            Spot = overwriteSpot
        addToScreen(Scene, Stored[0], Stored[1], Stored[2])
        r += pixelRatio
        if scanArea(Scene, (c, r), pixelRatio, pixelRatio) == square(pixelRatio, pixelRatio, backgroundColor):
            # print("Black")
            # time.sleep(0.1)
            Stored = addToScreen(Scene, Spot, c, r)
            overwriteSpot = False
        else:
            # print("Color!")
            # time.sleep(0.1)
            overwriteSpot = Spot
            Stored = addToScreenWithoutColor(Scene, Spot, newBlack, c, r)
        printScreen(Scene)
        # printCurrentPos(r, c, Pallete[rc%mod], borderColor, erase )
        # time.sleep(.1)
        keys.keys_pressed.discard(all)
    elif keys.is_s_pressed() and r > 0 and not Stored == []:
        if overwriteSpot == False:
            Spot = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
        else:
            Spot = overwriteSpot
        addToScreen(Scene, Stored[0], Stored[1], Stored[2])
        r -= pixelRatio
        if scanArea(Scene, (c, r), pixelRatio, pixelRatio) == square(pixelRatio, pixelRatio, backgroundColor):
            # print("Black")
            # time.sleep(0.1)
            Stored = addToScreen(Scene, Spot, c, r)
            overwriteSpot = False
        else:
            # print("Color!")
            # time.sleep(0.1)
            overwriteSpot = Spot
            Stored = addToScreenWithoutColor(Scene, Spot, newBlack, c, r)
        printScreen(Scene)
        # printCurrentPos(r, c, Pallete[rc%mod], borderColor, erase)
        # time.sleep(.1)
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
            # print("Black")
            # time.sleep(0.1)
            Stored = addToScreen(Scene, Spot, c, r)
            overwriteSpot = False
        else:
            # print("Color!")
            # time.sleep(0.1)
            overwriteSpot = Spot
            Stored = addToScreenWithoutColor(Scene, Spot, newBlack, c, r)
        printScreen(Scene)
        # printCurrentPos(r, c, Pallete[rc%mod], borderColor, erase)
        # time.sleep(.1)
        keys.keys_pressed.discard(all)
    elif keys.is_a_pressed() and c > 0 and not Stored == []:
        if overwriteSpot == False:
            Spot = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
        else:
            Spot = overwriteSpot
        addToScreen(Scene, Stored[0], Stored[1], Stored[2])
        # r += 0
        c -= pixelRatio
        if scanArea(Scene, (c, r), pixelRatio, pixelRatio) == square(pixelRatio, pixelRatio, backgroundColor):
            # print("Black")
            # time.sleep(0.1)
            Stored = addToScreen(Scene, Spot, c, r)
            overwriteSpot = False
        else:
            # print("Color!")
            # time.sleep(0.1)
            overwriteSpot = Spot
            Stored = addToScreenWithoutColor(Scene, Spot, newBlack, c, r)
        printScreen(Scene)
        # printCurrentPos(r, c, Pallete[rc%mod], borderColor, erase)
        # time.sleep(.1)
        keys.keys_pressed.discard(all)

    #Rotates block
    if keys.is_x_pressed() and not Stored == [] and not erase:
        currentBlock = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
        addToScreen(Scene, rotate(currentBlock, 270), c, r)
        printScreen(Scene)
        time.sleep(.2)


    #Erases border outline
    elif keys.is_b_pressed() and borderColor == defaultBorder and not Stored == [] and not erase and colorMode:
        addToScreen(Scene, square(pixelRatio,pixelRatio, Pallete[rc%mod]), c, r)
        border = []
        printScreen(Scene)
        borderColor = Pallete[rc%mod]
        # printCurrentPos(r, c, Pallete[rc%mod], borderColor, erase)
        time.sleep(.1)
    #adds border outline
    elif keys.is_b_pressed() and not Stored == [] and not erase and colorMode:
        printScreen(Scene)
        # addBorder(Scene, Pallete[rc%mod], grey)
        border = addBorderToArea(Scene, (c, r), pixelRatio, pixelRatio, Pallete[rc%mod], defaultBorder)
        # addToScreen(Scene, bordered, c, r)
        borderColor = defaultBorder
        # printCurrentPos(r, c, Pallete[rc%mod], borderColor, erase)
        # print(f"Previous Scan: {c, r} to {c+pixelRatio, r+pixelRatio}",  "  "*10)
        printScreen(Scene)
        time.sleep(.1)

    #Erases block
    if keys.is_e_pressed() and not Stored == []:
        overwriteSpot = False
        addToScreen(Scene, square(pixelRatio, pixelRatio, backgroundColor), c, r)
        borderingBackground = square(pixelRatio + 2, pixelRatio + 2, yellow)
        addToScreen(borderingBackground, square(pixelRatio, pixelRatio, backgroundColor), 1, 1)
        addBorderToColor(borderingBackground, yellow, backgroundColor, white)
        borderCreation = scanArea(borderingBackground, (1, 1), pixelRatio, pixelRatio)
        addToScreenWithoutColor(Scene, borderCreation, backgroundColor, c, r)
        erase = True
        Stored = [square(pixelRatio, pixelRatio, backgroundColor), c, r]
        printScreen(Scene)
        # printCurrentPos(r, c, Pallete[rc%mod], borderColor, erase)
        time.sleep(.1)


        # # addToScreen(Scene, square(pixelRatio, pixelRatio, newBlack), c, r)
        # bordered = addBorderToArea(Scene, (c, r), pixelRatio, pixelRatio, newBlack, white, False)
        # # Get the ASCII code color from the string
        # erase = True
        # Stored = [square(pixelRatio, pixelRatio, backgroundColor), c, r]
        # printScreen(Scene)
        # # printCurrentPos(r, c, Pallete[rc%mod], borderColor, erase)
        # time.sleep(.1)

        

    #changing colors with Pallete
    elif keys.is_t_pressed() and not erase:
        rc+=1
        if colorMode:
            scaned = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
            colorScanned = changeRGB(scaned, currentColor, Pallete[(rc)%mod])
            currentColor = Pallete[(rc)%mod]
            # FormerPallete = Pallete
            #Draws rgb if in colorMode not block sprites`
            addToScreen(Scene, colorScanned, c, r)
        else:
            addToScreen(Scene, Stored[0], c, r)
            addToScreenWithoutColor(Scene, spriteDict[sprites[rc%mod]], newBlack, c, r)
            overwriteSpot = spriteDict[sprites[rc%mod]]
        printScreen(Scene)
        if not borderColor == defaultBorder and colorMode:
            borderColor = Pallete[rc%mod]
        # printCurrentPos(r, c, currentColor, borderColor, erase)
        time.sleep(.3)
    elif keys.is_r_pressed() and not erase:
        rc-=1
        if colorMode:
            scaned = scanArea(Scene, (c, r), pixelRatio, pixelRatio)
            colorScanned = changeRGB(scaned, currentColor, Pallete[(rc)%mod])
            currentColor = Pallete[(rc)%mod]
            # FormerPallete = Pallete
            #Draws rgb if in colorMode not block sprites
            addToScreen(Scene, colorScanned, c, r)
        else:
            addToScreen(Scene, Stored[0], c, r)
            addToScreenWithoutColor(Scene, spriteDict[sprites[rc%mod]], newBlack, c, r)
            overwriteSpot = spriteDict[sprites[rc%mod]]

        printScreen(Scene)
        if not borderColor == defaultBorder and colorMode:
            borderColor = Pallete[rc%mod]
        # printCurrentPos(r, c, currentColor, borderColor, erase)
        time.sleep(.3)








# Show cursor
sys.stdout.write("\033[?25h" + reset)