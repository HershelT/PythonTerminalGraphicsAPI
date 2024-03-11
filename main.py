#All import
from imports import *
#imports colors
from colors import *
#importing my own matrix math file
from matrix import *
#importing image reader
sys.path.insert(0, 'ImageReader')
from ImageReader import *

#initializing a clear command
clear_command = 'cls' if os.name == 'nt' else 'clear'
def clear():
    os.system(clear_command)

#setting a screen size
def screen(length, width, filling = purple):
    filling += "  " + reset
    return [[filling for x in range(width)] for y in range(length)]

#Printing Base Scene to the console
def printScreen(screen, clear = True):
    # Create an off-screen buffer
    buffer = io.StringIO()

    for row in screen:
        # Write to the buffer instead of directly to the screen
        buffer.write(''.join(row) + '\n')

    if clear:
        sys.stdout.write('\033[?25l')
        # Move the cursor to the top of the terminal
        sys.stdout.write('\033[H\033[?25l')

    # Swap the buffer with the screen
    sys.stdout.write(buffer.getvalue())
    sys.stdout.flush()

    # Clear the buffer for the next frame
    buffer.close()
    sys.stdout.write('\033[?25h')
    sys.stdout.flush()

#Add lines to a screen screen at bottom left corner of drawing with (x, y)
def addToScreen(screen, obj, colIndex, rowIndex):
    for i, row in enumerate(obj):
        for j, str in enumerate(row):
            screen[len(screen) - (len(obj)+rowIndex)+i][colIndex+j] = str

#Bresenhams line drawing lgorithm
def bresenham(x1, y1, x2, y2):
  """
  Bresenham's line algorithm implementation in Python (improved)

  Args:
      x1: Starting x-coordinate
      y1: Starting y-coordinate
      x2: Ending x-coordinate
      y2: Ending y-coordinate

  Returns:
      list: List of pixel coordinates (x, y) for the line
  """
  dx = x2 - x1
  dy = y2 - y1

  # Handle special cases (vertical and horizontal lines)
  if dx == 0:
    for y in range(min(y1, y2), max(y1, y2) + 1):
      yield x1, y
    return
  elif dy == 0:
    for x in range(min(x1, x2), max(x1, x2) + 1):
      yield x, y1
    return

  # Steepness test for lines with slope between 0 and 1
  if abs(dy) > abs(dx) + abs(dx // 2):
    x1, y1, x2, y2 = y2, x2, y1, x1
    dx, dy = dy, dx

  # Use Bresenham's algorithm for non-special cases
  sign_x = 1 if dx > 0 else -1
  sign_y = 1 if dy > 0 else -1
  dx = abs(dx)
  dy = abs(dy)

  p = 2 * dy - dx
  x, y = x1, y1
  yield x, y
  for _ in range(dx):
    if p >= 0:
      y += sign_y
      p += 2 * (dy - dx)
    else:
      p += 2 * dy
    x += sign_x
    yield x, y


#Checks if a slope is within 0 and 1
def is_steep(dx, dy):
    return abs(dy) > abs(dx) + abs(dx // 2)

# Draws a line on the screen using the algorithm
def drawLine(screen, color, point1, point2):
    for x, y in bresenham(*point1, *point2):
        addToScreen(screen, square(1, 1, color), x, y)

#Create a parrallelogram
def fillTrapezoid(screen, color, point1, point2, point3, point4):#x1, x2, y2, x3, y3, x4, y4):
    firstParts = []
    secondParts = []
    #no matter which way user gives input, it will draw lines correcrtly
    if point2[1] < point1[1]:
      point2, point1 = point1, point2
    if point4[1] < point3[1]: 
      point4, point3 = point3, point4

    #Populates the lists with the (x,y) elements
    for x, y in bresenham(*point1, *point2):
        firstParts.append([x, y])
    for x2, y2 in bresenham(*point3, *point4):
        secondParts.append([x2, y2])
    
    #Gets length of lines
    First = len(firstParts)
    Second = len(secondParts) 
    # print(f"{First} {Second}")

    #checks 
    if First > len(secondParts):
         bigger = firstParts
    else:
        bigger = secondParts

    #Enumerates through the biggest list and maps elements from First->Second
    for i, ele in enumerate(bigger):
        firsts = i
        seconds = i
        
        #Checks if one list is bigger than other, then just draws all remainuing points from the last point in the list
        if i >= First: firsts = len(firstParts) - 1
        if i >= Second: seconds = len(secondParts) - 1

        #Checks if slope is between 0 and 1 so it flips the x and y axis to graph it correctly
        if is_steep(firstParts[firsts][0] - secondParts[seconds][0], firstParts[firsts][1] - secondParts[seconds][1]):
            drawLine(screen, color, (firstParts[firsts][1], firstParts[firsts][0]), (secondParts[seconds][1], secondParts[seconds][0]))
        else:
            drawLine(screen, color, (firstParts[firsts][0], firstParts[firsts][1]), (secondParts[seconds][0], secondParts[seconds][1]))
        # clear()
        # printScreen(screen)
        # print("Seconds: ", secondParts[seconds][0], secondParts[seconds][1])
        # print("First: ", firstParts[firsts][0], firstParts[firsts][1])
        # print(f"{firstParts}\n{secondParts}")
        # time.sleep(2)

#Draws an even parallogram with width (collumns) and length (rows) goes up and to the right
def drawPG(screen, color, width, length, point):
    point1 = (point[0], point[1])
    point2 = (point[0] + length, point[1]+length)
    point3 = (point[0] + width, point[1])
    point4 = (point[0] + length + width, point[1] + length)
    fillTrapezoid(screen, color, point1, point2, point3, point4)

#Draws any size three sided triangle
def drawTriangle(screen, color, point1, point2, point3):
  drawLine(screen, color, point1, point2)
  drawLine(screen, color, point2, point3)   
  drawLine(screen, color, point1, point3)
#Draws a square or rectangle
def square(length, width, color = bright_yellow):
    color += "  " + reset
    return [[color for x in range(width)] for y in range(length)]

#Draws a square with a inner color and a perimeter color
def hollowSquare(length, width, colorOuter = bright_yellow, colorInner = bright_white):
    colorOuter += "  " + reset
    colorInner += "  " + reset
    hSquare = [[colorInner for x in range(width)] for y in range(length)]
    for x in range(0, width):
        hSquare[0][x] = colorOuter
        hSquare[length-1][x] = colorOuter
    
    for y in range(0, len(hSquare)):
        hSquare[y][0] = colorOuter
        hSquare[y][len(hSquare[0])-1] = colorOuter
    return hSquare

#Draws a set size triangle at with top of triangle at center
def drawUpTriangle(screen, color, center, radius):
    for i in range(0, radius):
        drawLine(screen, color, (center[0]+i, center[1]-i), (center[0]-i, center[1]-i))

def drawRightTriangle(screen, color, center, radius):
    for i in range(0, radius):
        drawLine(screen, color, (center[0]-i, center[1]-i), (center[0]-i, center[1]+i))

def drawLeftTriangle(screen, color, center, radius):
    for i in range(0, radius):
        drawLine(screen, color, (center[0]+i, center[1]+i), (center[0]+i, center[1]-i))

def drawDownTriangle(screen, color, center, radius):
    for i in range(0, radius):
        drawLine(screen, color, (center[0]+i, center[1]+i), (center[0]-i, center[1]+i))



#Draws a set size square with bottom right corner being at center
def drawSetSquare(screen, color, center, length):
    addToScreen(screen, square(length, length, color), center[0], center[1])

# Running main
clear()
#initialize a screen size
Scene = screen(35, 70, green)
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
addToScreen(Scene, flip(entrance), 12, 13)

#Make filled 3d outlines under the door
fillTrapezoid(Scene, bright_yellow, (5,11), (9, 15), (36, 15), (40, 11))

#Creating a multicolor Square Object using the New Set size Triangle feature
colorSquare = screen(11, 11)
drawUpTriangle(colorSquare, bright_purple, (5, 5), 6)
drawDownTriangle(colorSquare, green, (5, 5), 6)
drawLeftTriangle(colorSquare, blue, (5, 5), 6)
drawRightTriangle(colorSquare, red, (5, 5), 6)

drawSetSquare(colorSquare, bright_yellow, (5, 5), 1)

#Adding the multicolor square object to the scene
addToScreen(Scene, colorSquare, 1, len(Scene) - len(colorSquare) -1)

drawPG(Scene, blue, 10, -6, (16, 8))
drawPG(Scene, yellow, 10, 6, (16, 8))

#Testing loading images
Heart.getPixel(0).flip()
# Heart.getPixel(0).transpose()
addToScreen(Scene, Heart.getPixelImage(), len(Scene[0]) - Heart.getPixel(0).getWidth(), 0)

# addToScreen(Scene, GameBoy.getPixelMatrix(0), 0, 0)

##TESTING SHAPES AND LINE DRAWING
# fillTrapezoid(Scene, bright_black, (2, 7), (4, 9), (7 ,7), (15, 20)) 
# fillTrapezoid(Scene, bright_black, (7, 2), (9, 4), (7, 7), (9, 9))
# fillTrapezoid(Scene, green, (18, 2), (24, 8), (28, 2), (34, 8))

#Add squares to screen
#addToScreen(Scene, squareBlue, 2,2)

#Draw outline of cube
# drawLine(Scene, black, (2, 7), (4, 9))
# drawLine(Scene, black, (7, 7), (9, 9))
# drawLine(Scene, black, (7, 2), (9, 4))
# drawLine(Scene, black, (4, 9), (9, 9))
# drawLine(Scene, black, (9, 4), (9, 9))
# drawLine(Scene, yellow, (1,5), (5,1))

# drawTriangle(Scene, blue, (6, 6), (10, 10), (14, 6))


#print the screen
clear()
printScreen(Scene)





