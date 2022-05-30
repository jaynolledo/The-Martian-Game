"""

Name: Jay Francis Nolledo
CSC 201
Programming Project 3

We all know Elon Musk, right? Many call him as the real-life Tony Stark.
Elon Musk is the CEO of Tesla & SpaceX and one of his main goal is to get
humans to our neighbor planet, Mars. In this game, Elon Musk fights
Martian aliens using his laser eyes. This graphic-based game was developed
using Python.


"""
from graphics import *
import time
import random
import math
NUM_LOSE = 10
NUM_WIN = 50
ALIEN_SPEED = 4
ELON_SPEED = 50
STALL_TIME = 0.05
LASER_SPEED = 10

# This function calculates the distance between two points using the distance formula
def distanceBetweenPoints(point1, point2):
    p1x = point1.getX()
    p1y = point1.getY()
    p2x = point2.getX()
    p2y = point2.getY()
    return math.sqrt((p1x - p2x)*(p1x - p2x) + (p1y - p2y) * (p1y - p2y))

# This function determines if two elements are close enough considering a certain threshhold
def isCloseEnough(Img1, Img2):
    threshold = Img1.getWidth() * 0.5 + Img2.getWidth() * 0.5
    distance = distanceBetweenPoints(Img1.getAnchor(), Img2.getAnchor())
    return distance < threshold

def moveAliens(alienList):
    for alien in alienList:
        alien.move(0,ALIEN_SPEED)

def addAlienToWindow(win):
    startX = random.randrange(50,650)
    startY = -40
    alien = Image(Point(startX, startY), "alien.gif")
    alien.draw(win)
    return alien

def addLaserToWindow(win, elon):
    startX = elon.getAnchor().getX()
    startY = elon.getAnchor().getY()
    laser = Image(Point(startX,startY), "laser.gif")
    laser.draw(win)
    return laser

# This function is responsible for the gameplay
def gameLoop(win, elon):
    alienList = []
    laserList = []
    score = 0
    scoreBoardLabel = Text(Point(600, 20), 'Score:').draw(win)
    scoreBoardLabel.setSize(16)
    scoreBoardLabel.setStyle('bold')
    scoreBoard = Text(Point(650, 20), '0').draw(win)
    scoreBoard.setSize(16)
    
    while score < NUM_WIN:
        if random.randrange(100) < 6:
            newAlien = addAlienToWindow(win)
            alienList.append(newAlien)
        
        keyPressed = win.checkKey()
        if keyPressed != '':
            if keyPressed == 'Up': # Makes elon shoot laser beams
                laser = addLaserToWindow(win, elon)
                laser.move(0,-LASER_SPEED)
                laserList.append(laser)
            elif keyPressed == 'Left': # Makes Elon move to the left
                elon.move(-ELON_SPEED,0)
            elif keyPressed == 'Right': # Makes Elon move to the right
                elon.move(ELON_SPEED,0)
                    
        moveAliens(alienList)
        
        for alien in alienList:
            if alien.getAnchor().getY() > 700:
                alien.undraw()
                alienList.remove(alien)
                score = score - 1
                scoreBoard.setText(str(score))
            # This if statement determines whether an alien got too close to Elon
            # If an alien got too close to Elon. The player loses and the program exits.
            if isCloseEnough(elon, alien):
                lose = lose + 1
                bground = Image(Point(350,350), "mars.gif")
                bground.draw(win)
                you_lose = Text(Point(333, 333),"The aliens got you. You lose!").draw(win)
                you_lose.setSize(36)
                you_lose.setStyle('bold')
                time.sleep(3)
                exit(-1)

               
            for laser in laserList:
                laser.move(0,-LASER_SPEED)
                if isCloseEnough(laser, alien):
                    alien.undraw()
                    alienList.remove(alien)
                    laser.undraw()
                    laserList.remove(laser)
                    score = score + 1
                    scoreBoard.setText(str(score))
                
        time.sleep(STALL_TIME)
        
    # Determines whether the player has killed enough aliens to win
    if score >= NUM_WIN:
        bg = Image(Point(350,350), "space.gif")
        bg.draw(win)
        you_lose = Text(Point(350, 350),"You killed enough aliens. You win!").draw(win)
        you_lose.setSize(36)
        you_lose.setStyle('bold')
        you_lose.setTextColor('orange')
        
    time.sleep(3)
    
# This class is used to display the instructions at the beginning of the game
class Instructions:
    
    def __init__(self, win):
        welcome = Text(Point(350, 120), 'Welcome to Martian!')
        welcome.setSize(36)
        welcome.setTextColor('orange')
        welcome.setStyle('bold')
        instruction = Text(Point(350, 320), 'Press the left/right arrow keys to make Elon move.\n Press the up arrow key to shoot.\n Shoot 50 aliens to win.\n You get a point deduction for each alien that escapes.\n If an alien gets you, you lose.')
        instruction.setSize(22)
        instruction2 = Text(Point(350, 500), 'Click anywhere on the window to continue.')
        instruction2.setSize(20)
        welcome.draw(win)
        instruction.draw(win)
        instruction2.draw(win)
        win.getMouse()
        welcome.undraw()
        instruction.undraw()
        instruction2.undraw()
    
def main():
    # setup the game 
    win = GraphWin("Martian", 700,700)
    win.setBackground("white")
    bg = Image(Point(350,350), "mars.gif")
    bg.draw(win)
    Instructions(win)

    elon = Image(Point(350,600), "elon.gif")
    elon.draw(win)

    gameLoop(win, elon)
    win.close()
    
if __name__ == "__main__":
    main()
    
