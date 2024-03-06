#All import
from imports import *
#imports colors
from colors import *

#initializing a clear command
clear_command = 'cls' if os.name == 'nt' else 'clear'
def clear():
    os.system(clear_command)

#setting a screen size
def screen(length, width, populated = purple):
    populated += "  " + reset
    return [[populated for x in range(width)] for y in range(length)]

#Printing Base Screen to the console
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

#Add lines to a screen screen
def addToScreen(screen, obj, rowIndex, colIndex):
    for i, row in enumerate(obj):
        for j, str in enumerate(row):
            screen[len(screen) - (len(obj)+rowIndex)+i][colIndex+j] = str

def drawLine(screen, x1, y1, x2, y2):
    m_new = 2 * (y2-y1)
    slope_error_new = m_new - x2+x1

    y = y1
    for x in range(x1, x2+1):
        # print("(", x, ",", y, ")\n")
        addToScreen(screen, square(1,1), y, x)
        #add slope error
        slope_error_new = slope_error_new + m_new

        #checks if slope erro reached limit
        if (slope_error_new > 0):
            y = y+1
            slope_error_new = slope_error_new - 2 * (x2 - x1)

#Create a square
def square(length, width, color = bright_yellow):
    color += "  " + reset
    return [[color for x in range(width)] for y in range(length)]





# Running main
clear()
#initialize a screen size
bigScreen = screen(16, 16)

#make a couple squares
squareBlue = square(15, 15, blue)
squareRed = square(9,9, red)

#draw a line to screen
drawLine(bigScreen, 0, 0, 15, 15)


#print the screen
printScreen(bigScreen)


