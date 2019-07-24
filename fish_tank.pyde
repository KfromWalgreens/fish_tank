from random import *
startX = 350
startY = 350
redf = 255
greenf = 255
bluef = 255

def setup():
    size(600,600)
    background(41, 171, 204)
    frameRate(20)
    
def fish(startX, startY, redf, greenf, bluef):
    c = 0
    while c < 10: 
        startX += randint(-220, 220)
        startY += randint(-220, 220)
        redf += randint(-250, 150)
        greenf += randint(-220, 250)
        bluef += randint(-250, 150)
        if c % 2 == 0: 
            fill(redf, greenf, bluef)
            triangle(startX, startY,startX + 70, startY - 50, startX, startY - 100)
            triangle(startX - 30, startY - 20,startX, startY - 50, startX - 30, startY - 80)
            fill(0)
            triangle(startX + 30, startY - 20,startX, startY - 50, startX + 30, startY - 80)
            ellipse(startX + 50, startY - 50, startX/35, startY/35)
        else:  
            fill(redf, greenf, bluef)
            triangle(startX, startY,startX - 70, startY - 50, startX, startY - 100)
            triangle(startX + 30, startY - 20,startX, startY - 50, startX + 30, startY - 80)
            fill(0)
            triangle(startX - 30, startY - 20,startX, startY - 50, startX - 30, startY - 80)
            ellipse(startX - 50, startY - 50, startX/35, startY/35)
    
        # startX += randint(-220, 220)
        # startY += randint(-220, 220)
        # redf += randint(-250, 150)
        # greenf += randint(-220, 250)
        # bluef += randint(-250, 150)
        c += 1
def draw():
    background(41, 171, 204) 
    fish(startX, startY, redf, greenf, bluef)

    
        
    
