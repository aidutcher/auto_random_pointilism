#! python3

# Program that generates paintings in MS Paint by randomly placing dots

import pyautogui
import random

pyautogui.PAUSE = 0.09

# Colors:
# Color window is 1640, 878 to 1869, 978

White = [1640, 878]
LightGrey = [1690, 878]
DarkGrey = [1733, 878]
Black = [1776, 878]
DarkRed = [1823, 878]
Red = [1869, 878]

Orange = [1640, 925]
Gold = [1690, 925]
LightYellow = [1733, 925]
Yellow = [1776, 925]
Lime = [1823, 925]
Green = [1869, 925]

Aqua = [1640, 978]
Turquoise = [1690, 978]
Indigo = [1733, 978]
Pink = [1776, 978]
Rose = [1823, 978]
Brown = [1869, 978]

# 1) Select brush
# Brush range = 1645, 253 to 1867, 326

Marker = [1645, 253]
CalligraphyPen = [1700, 253]
OilBrush = [1757, 253]
Watercolor = [1811, 253]
PixelPen = [1867, 253]

Pencil = [1645, 326]
Eraser = [1700, 326]
Crayon = [1757, 326]
SprayCan = [1811, 326]
Fill = [1867, 326]

Thickness = [1836, 411]

##    brushX = random.randint(1645, 1867)  # To determine a random brush
##    brushY = random.randint(253, 326)

##pyautogui.doubleClick(1645,253) # Select the brush

loopcount = 400 # Specify the number of brush strokes
i = 1

while i < 40:  # For painting in the first quadrant
    

# 2) Select color

    colorSelect = random.randint(1,5)  # Randomly select from among 5 colors

    if colorSelect == 1:  # Select first color
        pyautogui.doubleClick(White)

    elif colorSelect == 2:  # Select second color
        pyautogui.doubleClick(LightGrey)

    elif colorSelect == 3:  # Select third color
        pyautogui.doubleClick(DarkGrey)

    elif colorSelect == 4:  # Select fourth color
        pyautogui.doubleClick(Black)

    elif colorSelect == 5:  # Select fifth color
        pyautogui.doubleClick(LightGrey)

    thickness = random.randint(10, 100)  # Determine a random width for the brush
    
    pyautogui.doubleClick(1836, 411)  # Select the thickness field
    pyautogui.write(str(thickness))  # Set the width of the brush

# 3) Select a random point on the canvas
# At 100% the canvas is in range 120x, 330y to 1468x, 958y

    canvas1X = random.randint(120, 794) #Determine random X value in first quadrant
    canvas1Y = random.randint(330, 644)  #Determine random Y value first quadrant

    pyautogui.doubleClick(canvas1X, canvas1Y)  # Select the point on the canvas

    i += 1

while 40 <= i < 80:  # For painting in the second quadrant

    colorSelect = random.randint(1,5)  # Randomly select from among 5 colors

    if colorSelect == 1:  # Select first color
        pyautogui.doubleClick(White)

    elif colorSelect == 2:  # Select second color
        pyautogui.doubleClick(LightGrey)

    elif colorSelect == 3:  # Select third color
        pyautogui.doubleClick(DarkGrey)

    elif colorSelect == 4:  # Select fourth color
        pyautogui.doubleClick(Black)

    elif colorSelect == 5:  # Select fifth color
        pyautogui.doubleClick(LightGrey)

    thickness = random.randint(10, 100)  # Determine a random width for the brush
    
    pyautogui.doubleClick(1836, 411)  # Select the thickness field
    pyautogui.write(str(thickness))  # Set brush thickness

    canvas2X = random.randint(794, 1468) #Determine random X value in second quadrant
    canvas2Y = random.randint(330, 644)  #Determine random Y value in second quadrant

    pyautogui.doubleClick(canvas2X, canvas2Y)  # Place the point on the canvas

    i += 1

while 80 <= i < 120:  # For painting in the third quadrant

    colorSelect = random.randint(1,5)  # Randomly select from among 5 colors

    if colorSelect == 1:  # Select first color
        pyautogui.doubleClick(White)

    elif colorSelect == 2:  # Select second color
        pyautogui.doubleClick(LightGrey)

    elif colorSelect == 3:  # Select third color
        pyautogui.doubleClick(DarkGrey)

    elif colorSelect == 4:  # Select fourth color
        pyautogui.doubleClick(Black)

    elif colorSelect == 5:  # Select fifth color
        pyautogui.doubleClick(LightGrey)

    thickness = random.randint(10, 100)  # Determine a random width for the brush
    
    pyautogui.doubleClick(1836, 411)  # Select the thickness field
    pyautogui.write(str(thickness))

    canvas3X = random.randint(120, 794) #Determine random X value in third quadrant
    canvas3Y = random.randint(644, 958)  #Determine random Y value in third quadrant

    pyautogui.doubleClick(canvas3X, canvas3Y)  # Select the point on the canvas

    i += 1
    
while 120 <= i < 160:  # For painting in the fourth quadrant

    colorSelect = random.randint(1,5)  # Randomly select from among 5 colors

    if colorSelect == 1:  # Select first color
        pyautogui.doubleClick(White)

    elif colorSelect == 2:  # Select second color
        pyautogui.doubleClick(LightGrey)

    elif colorSelect == 3:  # Select third color
        pyautogui.doubleClick(DarkGrey)

    elif colorSelect == 4:  # Select fourth color
        pyautogui.doubleClick(Black)

    elif colorSelect == 5:  # Select fifth color
        pyautogui.doubleClick(LightGrey)

    thickness = random.randint(10, 100)  # Determine a random width for the brush
    
    pyautogui.doubleClick(1836, 411)  # Select the thickness field
    pyautogui.write(str(thickness))

    canvas4X = random.randint(794, 1468) #Determine random X value in third quadrant
    canvas4Y = random.randint(644, 958)  #Determine random Y value in third quadrant

    pyautogui.doubleClick(canvas4X, canvas4Y)  # Select the point on the canvas

    i += 1

while 160 <= i < loopcount: # Use the whole canvas 

    colorSelect = random.randint(1,5)  # Randomly select from among 5 colors

    if colorSelect == 1:  # Select first color
        pyautogui.doubleClick(White)

    elif colorSelect == 2:  # Select second color
        pyautogui.doubleClick(LightGrey)

    elif colorSelect == 3:  # Select third color
        pyautogui.doubleClick(DarkGrey)

    elif colorSelect == 4:  # Select fourth color
        pyautogui.doubleClick(Black)

    elif colorSelect == 5:  # Select fifth color
        pyautogui.doubleClick(Black)

    thickness = random.randint(10, 100)  # Determine a random width for the brush
    
    pyautogui.doubleClick(1836, 411)  # Select the thickness field
    pyautogui.write(str(thickness))

    canvasAX = random.randint(120, 1468) #Determine random X value in third quadrant
    canvasAY = random.randint(330, 958)  #Determine random Y value in third quadrant

    pyautogui.doubleClick(canvasAX, canvasAY)  # Select the point on the canvas

    i += 1

