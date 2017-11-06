# Jake McGhee

def getPic():
    """ prompts a user to pick a file to be converted to a JES picture """
    
    return makePicture(pickAFile())

# Warm Up

def copyToLarger():
    """ makes a copy of an image """

    source = getPic()
    width = getWidth(source)
    height = getHeight(source)
    copy = makeEmptyPicture(width+200, height+200)
    for x in range (0, width):
        for y in range (0, height):
            color = getColor(getPixel(source, x, y))
            setColor(getPixel(copy, x+100, y+100), color)
    show(copy)
    return copy
    
    
# Problem 1
    
def pyCopy(source, target, targetX, targetY):
    """ makes a copy of an image """

    for x in range (0, getWidth(source)):
        for y in range (0, getHeight(source)):
            color = getColor(getPixel(source, x, y))
            setColor(getPixel(target, x+targetX, y+targetY), color)
    show(target)
    return target
    

# Problem 2

def makeCollage():

    canvas = makeEmptyPicture(3300, 2550)
    pic1 = makePicture('C:\\Users\\Jake\\Desktop\\School\\CST 205\\lab5\\jaguar.jpg')
    
    copyToTarget(pic1, canvas, getWidth(canvas)/2 - getWidth(pic1), getHeight(canvas)/2 - getHeight(pic1))
    pic1 = mirror_horizontal(pic1)
    copyToTarget(pic1, canvas, getWidth(canvas)/2, getHeight(canvas)/2 - getHeight(pic1))
    pic1 = mirror_vertical(pic1)
    copyToTarget(pic1, canvas, getWidth(canvas)/2, getHeight(canvas)/2)
    pic1 = mirror_horizontal(pic1)
    copyToTarget(pic1, canvas, getWidth(canvas)/2 - getWidth(pic1), getHeight(canvas)/2 - getHeight(pic1))
    
    writePictureTo(canvas,'C:\\Users\\Jake\\Desktop\\School\\CST 205\\lab5\\collage.jpg')
    return(canvas)
    
    
def makeGrid(x_grid_size, y_grid_size):
    pic = getPic()
    for y in range (0, getHeight(pic), getHeight(pic) / y_griz_size):
        for y in range (0, 
        

def mirror_horizontal(pic):
    width = getWidth(pic)
    height = getHeight(pic)
    canvas = makeEmptyPicture(width, height)
    for x in range(0, width):
        for y in range(0, height):
           color = getColor(getPixel(pic,x,y))
           copy = getPixel(canvas, width-1-x,y)
           setColor(copy,color)
    return(canvas)
    
def mirror_vertical(pic):
    width = getWidth(pic)
    height = getHeight(pic)
    canvas = makeEmptyPicture(width, height)
    for x in range(0, width):
        for y in range(0, height):
           color = getColor(getPixel(pic,x,y))
           copy = getPixel(canvas, x, height-1-y)
           setColor(copy,color)
    return(canvas)

def quadMirror_topLeft(pic):
    """ creates a mirror of an image using the top left quadrant of a picture"""
    
    # mirror left
    for x in range(0, getWidth(pic)/2):
        for y in range(0 , getHeight(pic)):
            color = getColor(getPixel(pic,x,y))
            copy = getPixel(pic, getWidth(pic)-1-x, y)
            setColor(copy, color)
            
    # mirror top
    for x in range(0, getWidth(pic)):
        for y in range(0 , getHeight(pic)/2):
            color = getColor(getPixel(pic,x,y))
            copy = getPixel(pic, x, getHeight(pic)-1-y)
            setColor(copy, color)  
            
    return(pic)
    
def copyToTarget(source, target, targetX, targetY):
    """ makes a copy of an image - same function as pyCopy except it does not show the result"""

    for x in range (0, getWidth(source)):
        for y in range (0, getHeight(source)):
            color = getColor(getPixel(source, x, y))
            setColor(getPixel(target, x+targetX, y+targetY), color)
    return target