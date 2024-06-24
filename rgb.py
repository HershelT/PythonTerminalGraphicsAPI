from colors import reset, black
#Color manipulation functions for the screen


#Resets the screen by clearing it to a certain color, or default black
def clearScreen(screen, newColor = black):
    drawnOver = [[0 for x in range(len(screen[0]))] for y in range(len(screen))]
    for i, row in enumerate(screen):
        for j, col in enumerate(row):
            drawnOver[i][j] = screen[i][j]
            screen[i][j] = newColor + "  " + reset
    return drawnOver

    # return screen

#returns a colored list of a certain size
#Can be used for equality checks if wanting to dra over something
#Best used in conjuction with scanScreen
def coloredList(color, size):
    return [color + "  " + reset for i in range(size)]


#changes the rgb values of just one instance of object, by creating new object and returning it
#Uses are for when you want to modifyt something but dont want to change base case
def changeRGB(object, oldRGB, newRGB):
    newObject =  [["0" for x in range(len(object[0]))] for y in range(len(object))]
    for i, row in enumerate(object):
        for j, col in enumerate(row):
            if object[i][j] == oldRGB + "  " + reset or oldRGB in object[i][j]:
                newObject[i][j]= newRGB + "  " + reset
            else:
                newObject[i][j] = object[i][j]
    return newObject

#Changes the rgb values of all instances of the object
def replaceRGB(object, oldRGB, newRGB):
    for i, row in enumerate(object):
        for j, col in enumerate(row):
            if object[i][j] == oldRGB + "  " + reset or oldRGB in object[i][j]:
                object[i][j] = newRGB + "  " + reset
    return object

#Checks if a color is neighboring a certain color and changes it to another color
def addBorderToColor(object, neighbor, oldColor, newColor):
    for i, row in enumerate(object):
        for j, col in enumerate(row):
            if object[i][j] == oldColor + "  " + reset:
                if i > 0 and object[i-1][j] == neighbor + "  " + reset:
                    object[i][j] = newColor + "  " + reset
                elif i < len(object)-1 and object[i+1][j] == neighbor + "  " + reset:
                    object[i][j] = newColor + "  " + reset
                elif j > 0 and object[i][j-1] == neighbor + "  " + reset:
                    object[i][j] = newColor + "  " + reset
                elif j < len(object[0])-1 and object[i][j+1] == neighbor + "  " + reset:
                    object[i][j] = newColor + "  " + reset
    return object

#Does same thing as addBorderToColor but instead of checking for a neighboring color, it automaticall
#adds a border color if one its neighbors is not itself(old color). Also checks if neihgboring color is not equal to border color
def addBorder(object, oldColor, newColor):
    for i, row in enumerate(object):
        for j, col in enumerate(row):
            if object[i][j] == oldColor + "  " + reset:
                if i > 0 and object[i-1][j] != oldColor + "  " + reset and object[i-1][j] != newColor + "  " + reset:
                    object[i][j] = newColor + "  " + reset
                elif i < len(object)-1 and object[i+1][j] != oldColor + "  " + reset and object[i+1][j] != newColor + "  " + reset:
                    object[i][j] = newColor + "  " + reset
                elif j > 0 and object[i][j-1] != oldColor + "  " + reset and object[i][j-1] != newColor + "  "  + reset:
                    object[i][j] = newColor + "  " + reset
                elif j < len(object[0])-1 and object[i][j+1] != oldColor + "  " + reset and object[i][j+1] != newColor + "  " + reset:
                    object[i][j] = newColor + "  " + reset
    return object


#Adds a border to the perimeter of the object without checking for neighbors
#Useful for adding a border to the perimeter of an object (Best border function)
def addPerimeter(object, borderColor):
    for i, row in enumerate(object):
        for j, col in enumerate(row):
            if i == 0 or i == len(object)-1 or j == 0 or j == len(object[0])-1:
                object[i][j] = borderColor + "  " + reset
    return object



    