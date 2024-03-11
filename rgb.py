from colors import reset

#changes the rgb values of just one instance of object
def changeRGB(object, oldRGB, newRGB):
    newObject =  [["0" for x in range(len(object[0]))] for y in range(len(object))]
    for i, row in enumerate(object):
        for j, col in enumerate(row):
            if object[i][j] == oldRGB + "  " + reset:
                newObject[i][j]= newRGB + "  " + reset
            else:
                newObject[i][j] = object[i][j]
    return newObject

#Changes the rgb values of all instances of the object
def changeAllRGB(object, oldRGB, newRGB):
    for i, row in enumerate(object):
        for j, col in enumerate(row):
            if object[i][j] == oldRGB + "  " + reset:
                object[i][j] = newRGB + "  " + reset

