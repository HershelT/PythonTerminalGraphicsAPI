#ONLY IMPORT I NEED IS drawing.py
from drawing import *


# Running main
clear()
#initialize a screen size
Scene = screen(35, 50, green)
# Scene = screen(Heart.getPixel(0).getLength()+50, Heart.getPixel(0).getWidth()+50)

# printScreen(Scene))

#make a couple Solid squares
squareBlue = square(5, 5, black)
squareRed = square(5,5, red)

#Creating a door with a handle object
door = hollowSquare(15, 8, white, bright_teal)
addToScreen(door, square(1,1, bright_orange), 5, 7)

#Creating a entrance object with the door object pasted in
entrance = screen(20, 20, white)
addToScreen(entrance, hollowSquare(18, 18, white, yellow), 1, 1)
addToScreen(entrance, door, 6, 2)

#Adding the entrance object the to scene
addToScreen(Scene, entrance, 12, 13)

#Make filled 3d outlines under the door
fillTrapezoid(Scene, bright_yellow, (5,11), (9, 15), (36, 15), (40, 11))

#Creating a multicolor Square Object using the New Set size Triangle feature
colorSquare = screen(11, 11)
drawUpTriangle(colorSquare, bright_purple, (5, 5), 6)
drawDownTriangle(colorSquare, rgb(23, 23, 23), (5, 5), 6)
drawLeftTriangle(colorSquare, blue, (5, 5), 6)
drawRightTriangle(colorSquare, red, (5, 5), 6)

drawSetSquare(colorSquare, bright_yellow, (5, 5), 1)

#Adding the multicolor square object to the scene
# addToScreen(Scene, colorSquare, 1, len(Scene) - len(colorSquare) -1)

drawPG(Scene, blue, 10, -6, (16, 8))
drawPG(Scene, yellow, 10, 6, (16, 8))

#TESTING LOADING IMAGES AND TRANSPOSING
# Heart.getPixel(0).flip()
# Heart.getPixel(0).transpose()
# addToScreen(Scene, Heart.getPixelImage(), len(Scene[0]) - Heart.getPixel(0).getWidth(), 0)

#TESTING DRAWING LARGE GAMEBOY WITH FAST PROCCESSING 
# addToScreen(Scene, GameBoy.getPixelMatrix(0), 0, 0)

##TESTING SHAPES AND LINE DRAWING
# fillTrapezoid(Scene, bright_black, (2, 7), (4, 9), (7 ,7), (15, 20)) 
# fillTrapezoid(Scene, bright_black, (7, 2), (9, 4), (7, 7), (9, 9))
# fillTrapezoid(Scene, green, (18, 2), (24, 8), (28, 2), (34, 8))

#Add squares to screen
#addToScreen(Scene, squareBlue, 2,2)

#TESTING LINE DRAWING TO DRAW OUTLINE OF CUBE
# drawLine(Scene, black, (2, 7), (4, 9))
# drawLine(Scene, black, (7, 7), (9, 9))
# drawLine(Scene, black, (7, 2), (9, 4))
# drawLine(Scene, black, (4, 9), (9, 9))
# drawLine(Scene, black, (9, 4), (9, 9))
# drawLine(Scene, yellow, (1,5), (5,1))

# drawTriangle(Scene, blue, (6, 6), (10, 10), (14, 6))


#print the screen
drawRectangle(Scene, rgb(170, 223, 2), (20, 10), (30, 15))
# clear()
# printScreen(Scene)

#TEST OF GRAPHICS ENGINE
#FAlLING Blocks and ROLLING HEART
j = 0
changeAllRGB(Scene, green, white)
while True:
    colorSquare = rotateRight(colorSquare)
    for i in range(0,3):
        Heart.getPixel(0).rotateRight()
    #Adding vertically moving squares
    # replaceSquare = addToScreen(Scene, changeRGB(colorSquare, red, rgb(178, 123, 23)), 1, (len(Scene) - len(colorSquare) - j)%len(Scene))
    # replaceSquare2 = addToScreen(Scene, changeRGB(colorSquare, blue, rgb(65, 123, 56)), 15, (len(Scene) - len(colorSquare) - j*2-5)%len(Scene))
    replaceSquare3 = addToScreen(Scene, flip(colorSquare), len(Scene[0])- len(colorSquare[0]) - j%len(Scene[0]), j%(len(Scene)))
    
    # replaceHeart = addToScreen(Scene, Heart.getPixelImage(0), len(Scene[0]) - Heart.getPixel(0).getWidth()-(j%len(Scene[0])), 0)
    # clear()
    printScreen(Scene)
    #Replacing the lines that were drawn over
    # addToScreen(Scene, replaceHeart[0], replaceHeart[1], replaceHeart[2])
    addToScreen(Scene, replaceSquare3[0], replaceSquare3[1], replaceSquare3[2])
    # addToScreen(Scene, replaceSquare[0], replaceSquare[1], replaceSquare[2])
    # addToScreen(Scene, replaceSquare2[0], replaceSquare2[1], replaceSquare2[2])

    time.sleep(0.1)
    j += 1
