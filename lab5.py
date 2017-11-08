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
    rows = 4
    cols = 4
    grid = makeGrid(canvas, rows, cols)
    
    #paint photo 1
    pic1 = makePicture('C:\\Users\\J.McGhee\\Documents\\Jake\\CST205\\lab5\\animals_hero_jaguars.jpg')
    pic1 = BnW(pic1)
    pic1 = copyPictureToFitGrid(pic1, canvas, rows, cols, 1000, 350)
    copyToTarget(pic1, canvas, grid[0][0][0], grid[0][0][1])
    pic1 = mirror_horizontal(pic1)
    copyToTarget(pic1, canvas, grid[0][3][0], grid[0][3][1])
    pic1 = mirror_vertical(pic1)
    copyToTarget(pic1, canvas, grid[3][3][0], grid[3][3][1])
    pic1 = mirror_horizontal(pic1)
    copyToTarget(pic1, canvas, grid[3][0][0], grid[3][0][1])
    print("photo 1 successful")
    
    #paint photo 2
    pic2 = makePicture('C:\\Users\\J.McGhee\\Documents\\Jake\\CST205\\lab5\\jaguar-900-retina.jpg')
    pic2 = copyPictureToFitGrid(pic2, canvas, rows, cols, 0, 100)
    copyToTarget(pic2, canvas, grid[0][1][0], grid[0][1][1])
    pic2 = mirror_horizontal(pic2)
    copyToTarget(pic2, canvas, grid[0][2][0], grid[0][2][1])
    print("photo 2 successful")
    
    #paint photo 3
    pic3 = makePicture('C:\\Users\\J.McGhee\\Documents\\Jake\\CST205\\lab5\\national-animal-of-brazil.jpg')
    pic3 = copyPictureToFitGrid(pic3, canvas, rows, cols, 300, 100)
    pic3 = mirror_vertical(pic3)
    copyToTarget(pic3, canvas, grid[3][2][0], grid[3][2][1])
    pic3 = mirror_horizontal(pic3)
    copyToTarget(pic3, canvas, grid[3][1][0], grid[3][1][1])
    print("photo 3 successful")
    
    #paint photo 4
    pic4 = makePicture('C:\\Users\\J.McGhee\\Documents\\Jake\\CST205\\lab5\\large-header-jaguar-Patrick-Meier-Jag-Water-Fullsize2.jpg')
    pic4 = copyPictureToFitGrid(pic4, canvas, rows, cols, 100, 200)
    pic4 = makeNegative(pic4)
    copyToTarget(pic4, canvas, grid[2][0][0], grid[2][0][1])
    print("photo 4 successful")
    
    #paint photo 5
    pic5 = makePicture('C:\\Users\\J.McGhee\\Documents\\Jake\\CST205\\lab5\\jaguar-wide-30858048.jpg')
    pic5 = copyPictureToFitGrid(pic5, canvas, rows, cols, 100, 100)
    copyToTarget(pic5, canvas, grid[1][0][0], grid[1][0][1])
    pic5 = mirror_horizontal(pic5)
    copyToTarget(pic5, canvas, grid[1][3][0], grid[1][3][1])
    print("photo 5 successful")
    
    #paint photo 6
    pic6 = makePicture('C:\\Users\\J.McGhee\\Documents\\Jake\\CST205\\lab5\\Panthera_onca_at_the_Toronto_Zoo_2.jpg')
    pic6 = copyPictureToFitGrid(pic6, canvas, rows, cols, 500, 0)
    copyToTarget(pic6, canvas, grid[1][1][0], grid[1][1][1])
    pic6 = mirror_horizontal(pic6)
    copyToTarget(pic6, canvas, grid[1][2][0], grid[1][2][1])
    pic6 = mirror_vertical(pic6)
    copyToTarget(pic6, canvas, grid[2][2][0], grid[2][2][1])
    pic6 = mirror_horizontal(pic6)
    copyToTarget(pic6, canvas, grid[2][1][0], grid[2][1][1])
    print("photo 6 successful")
    
    #paint photo 7
    pic7 = makePicture('C:\\Users\\J.McGhee\\Documents\\Jake\\CST205\\lab5\\jaguar-walking-branch.ngsversion.1461176495163.jpg')
    pic7 = copyPictureToFitGrid(pic7, canvas, rows, cols, 350, 0)
    pic7 = makeNegative(pic7)    
    pic7 = mirror_horizontal(pic7)
    copyToTarget(pic7, canvas, grid[2][3][0], grid[2][3][1])
    print("photo 7 successful")
    
    #paint center photo
    pic8 = makePicture('C:\\Users\\J.McGhee\\Documents\\Jake\\CST205\\lab5\\jaguar.jpg')
    pic8 = quadMirror_topLeft(pic8)
    copyToTarget(pic8, canvas, getWidth(canvas)/2 - getWidth(pic8)/2, getHeight(canvas)/2 - getHeight(pic8)/2)
    print("photo 8 successful")
   
    
    
     
    
    writePictureTo(canvas, 'C:\\Users\\J.McGhee\\Documents\\Jake\\CST205\\lab5\\collage.jpg')
    # writePictureTo(canvas,'C:\\Users\\Jake\\Desktop\\School\\CST 205\\lab5\\collage.jpg')
    
def copyToTarget(source, target, targetX, targetY):
    """ makes a copy of an image - same function as pyCopy except it does not show the result"""

    for x in range (0, getWidth(source)):
        for y in range (0, getHeight(source)):
            color = getColor(getPixel(source, x, y))
            setColor(getPixel(target, x+targetX, y+targetY), color)
    return target  
    
def makeGrid(canvas, row, col):
    """ creates a m x n list containing the [x,y] locations on the grid where pictures should be drawn """

    grid = []
    i = -1
    for y in range (0, getHeight(canvas), getHeight(canvas) / col):
        grid.append([])
        i+=1
        for x in range (0, getWidth(canvas), getWidth(canvas) / row):
            grid[i].append([x,y])
    return grid
     
def copyPictureToFitGrid(pic, canvas, row, col, beginX, beginY):
    """ crops a picture so that it will fit on an m x n grid """
    
    # get size of the new picture
    width = getWidth(canvas) / row
    height = getHeight(canvas) / col
    
    #make sure picture is large enough to fit on the grid
    if getWidth(pic) < width:
        print("Error - image too small to fit on grid - %s" % pic) 
        return
    elif getHeight(pic) < height:
        print("Error - image too small to fit on grid - %s" % pic)
        return
    
    copy = makeEmptyPicture(width, height)
    
    # reduce size of the picture if it is significantly bigger than the grid size  
    while getWidth(pic) > width*2 and getHeight(pic) > height*2:
        pic = shrink(pic)
    
    # error check for out of bounds exception
    if getWidth(pic) - beginX < width:
         beginX = getWidth(pic) - width
    if getHeight(pic) - beginY < height:
         beginY = getHeight(pic) - height
        
    # paint new picture
    for x in range (0, width):
        for y in range (0, height):
            color = getColor(getPixel(pic, x+beginX, y+beginY))
            setColor(getPixel(copy, x, y), color)
    return copy
    
  
    

def shrink(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  canvas = makeEmptyPicture(width/2, height/2)
  for x in range (0, width-1, 2):
    for y in range (0, height-1, 2):
      color = getColor(getPixel(pic, x, y))
      setColor(getPixel(canvas, x/2, y/2), color)
  return canvas        
    

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

def makeNegative(pic):
    """ Makes a negative copy of an image """

    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        g = getGreen(p)
        b = getBlue(p)
        r = 255 - r
        g = 255 - g
        b = 255 - b
        setRed(p, r)
        setGreen(p, g)
        setBlue(p, b)
    return(pic)

def BnW(pic):
    """ Converts an image to gray-scale """
    
    pixels = getPixels(pic)
    for p in pixels:
        r = getRed(p)
        g = getGreen(p)
        b = getBlue(p)
        luminance = r*0.299 + g*0.587 + b*0.114
        setRed(p, luminance)
        setGreen(p, luminance)
        setBlue(p, luminance)
    return pic
    
    
