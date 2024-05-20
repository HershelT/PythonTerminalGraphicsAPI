#ONLY IMPORT I NEED IS drawing.py
#Demo

from drawing import *
from keyboardListener import *

#initliaze a screen size
LightsaberScene = screen(35, 50, black)
leftLightsaber = screen(23, 20, black)
rightLightsaber = screen(23, 20, black)

rainbow = rainbow_bright
#Drawing Lightsaber
drawThickLine(leftLightsaber, rainbow[0], (1,1), (20,20), 3)
#draw hilt
drawThickLine(leftLightsaber, silver, (1,1), (5,5), 3)
#Draw the button
drawSetSquare(leftLightsaber, green, (5,5), 1)




drawThickLine(rightLightsaber, rainbow[3], (20,1), (1,20), 3)
drawThickLine(rightLightsaber, silver, (20,1), (15,6), 3)
drawSetSquare(rightLightsaber, red, (17,6), 1)

#lightsaber Rotation
# leftLightsaber = rotateRight(leftLightsaber)
# rightLightsaber = rotateRight(rightLightsaber)

#changes hilt color of left lughtsaber
# changeAllRGB(leftLightsaber, green, yellow)


#adding lightsabers to the scene
addToScreen(LightsaberScene, rightLightsaber, 20, 0)
addToScreenOnColor(LightsaberScene,leftLightsaber, black, 0, 0)


clear()

#lightsaber animation values
lc = 0
rc = 3
# addBorderToColor(LightsaberScene, black, rainbow[(lc)%7], white)
# addBorderToColor(LightsaberScene, black, rainbow[(rc)%7], white)

addBorder(LightsaberScene, rainbow[(rc)%7], white)
addBorder(LightsaberScene, rainbow[(lc)%7], white)


blocks = getBlocks(LightsaberScene, (0,0), (19, 19), 3, 3)
# clear()
# for block in blocks:
#     printScreen(block[2])
#     time.sleep(.5)
#     print(len(blocks))
#     clear()
#can use blocks for rotation and other things and for drawing on the screen
newScene = screen(100, 100, black)
listnew = []
for block in blocks:
    listnew.append(block[2])
i= 0
y = -20
#Rotation demomnstrations
# drawLineCustom(newScene, (40,20), (50, 10), listnew)
# printScreen(newScene)

# time.sleep(3)


x = 0
printScreen(LightsaberScene)
#lightsaber animation
keys = MyKeyListener()
listener = keyboard.Listener(
    on_press=keys.on_press,
    on_release=keys.on_release
)
listener.start()
r = 20
c = 20
Stored = []
while not keys.check_keys():
    if keys.is_c_pressed():
        clearScreen(LightsaberScene, black)
        printScreen(LightsaberScene)
        time.sleep(.1)
    if keys.is_q_pressed():
        r = 20
        c = 20
        Stored = addToScreen(LightsaberScene, square(5, 5), c, r)
        printScreen(LightsaberScene)
        time.sleep(.5)
    # if keys.is_z_pressed():
    #     r = 20
    #     c = 20
    #     time.sleep(.5)
    #     keys.keys_pressed.discard(all)

    if keys.is_i_pressed():
        print("r: ", r, " c: ", c)
        print("Screen Height: ", len(LightsaberScene), " Screen Width: ", len(LightsaberScene[0]) )
        time.sleep(0.5)
        keys.keys_pressed.discard(all)

    #moving block around
    #Up and Down
    if keys.is_w_pressed() and r < len(LightsaberScene) - 5 and not Stored == []: 
        Spot = scanArea(LightsaberScene, (c, r), 5, 5)
        addToScreen(LightsaberScene, Stored[0], Stored[1], Stored[2])
        r += 5
        Stored = addToScreen(LightsaberScene, Spot, c, r)
        printScreen(LightsaberScene)
        time.sleep(0.5)
        keys.keys_pressed.discard(all)
    if keys.is_s_pressed() and r > 0 and not Stored == []:
        Spot = scanArea(LightsaberScene, (c, r), 5, 5)
        addToScreen(LightsaberScene, Stored[0], Stored[1], Stored[2])
        r -= 5
        Stored = addToScreen(LightsaberScene, Spot, c, r)
        printScreen(LightsaberScene)
        time.sleep(0.5)
        keys.keys_pressed.discard(all)
    #Left and Right
    if keys.is_d_pressed() and c < len(LightsaberScene[0]) and not Stored == []: 
        Spot = scanArea(LightsaberScene, (c, r), 5, 5)
        addToScreen(LightsaberScene, Stored[0], Stored[1], Stored[2])
        c += 5
        Stored = addToScreen(LightsaberScene, Spot, c, r)
        printScreen(LightsaberScene)
        time.sleep(0.5)
        keys.keys_pressed.discard(all)
    if keys.is_a_pressed() and c > 0 and not Stored == []: 
        Spot = scanArea(LightsaberScene, (c, r), 5, 5)
        addToScreen(LightsaberScene, Stored[0], Stored[1], Stored[2])
        r += 0
        c -= 5
        Stored = addToScreen(LightsaberScene, Spot, c, r)
        printScreen(LightsaberScene)
        time.sleep(0.5)
        keys.keys_pressed.discard(all)


        
    if keys.is_t_pressed():
        replaceRGB(LightsaberScene, rainbow[rc%7], rainbow[(rc+1)%7])
        replaceRGB(LightsaberScene, rainbow[lc%7], rainbow[(lc+1)%7])
        lc+=1
        rc+=1
        # addBorderToColor(LightsaberScene, black, rainbow[(lc)%7], white)
        # addBorderToColor(LightsaberScene, black, rainbow[(rc)%7], white)
        printScreen(LightsaberScene)
        time.sleep(.1)
    if keys.is_r_pressed():
        replaceRGB(LightsaberScene, rainbow[rc%7], rainbow[(rc-1)%7])
        replaceRGB(LightsaberScene, rainbow[lc%7], rainbow[(lc-1)%7])
        lc-=1
        rc-=1
        # addBorderToColor(LightsaberScene, black, rainbow[(lc)%7], white)
        # addBorderToColor(LightsaberScene, black, rainbow[(rc)%7], white)
        printScreen(LightsaberScene)
        time.sleep(.1)


while x < 100:
    printScreen(LightsaberScene)
    time.sleep(.1)
    replaceRGB(LightsaberScene, rainbow[rc%7], rainbow[(rc+1)%7])
    replaceRGB(LightsaberScene, rainbow[lc%7], rainbow[(lc+1)%7])



    # x+=1
    # lc+=1
    # rc+=1
