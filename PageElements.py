from pygame import Rect
import pygame
from os import getcwd
from math import floor

class PageElement:
    def __init__(self, centerXY, width, height, colorRGB=(255,255,255)):
        self.percentRect = getRectFromCenter(centerXY, width, height)
        self.rect = Rect(0,0,0,0)
        self.color = colorRGB

    def wasClicked(self, clickLoc):
        if self.rect.collidepoint(clickLoc[0], clickLoc[1]):
            return True
        return False
    
    def display(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def onClick(self, screen):
        print("You've clicked a useless page element")

    def adjustToScreenSize(self, screenDims):
        #call on screen size adjust event?
        #https://www.pygame.org/docs/ref/display.html#:~:text=If%20the%20display%20is%20set,the%20window%20must%20be%20redrawn.
        self.rect = convertPercentRectToScreenRect(self.percentRect, screenDims)


class Button(PageElement):

    def __init__(self, centerXY, width, height, text, textColorRGB=(0,0,0), backColorRGB=(255,255,255)):
        super().__init__(centerXY, width, height, backColorRGB)
        # pygame.font.init()
        self.text = text
        self.textColorRGB = textColorRGB
        self.widthPerc = width
        self.heightPerc = height
        self.centerPerc = centerXY

        
    
    def onClick(self, screen):
        print("a ha! You've found a useless button. Great Work")
        print('The text on this button is: ' + self.text)

    def display(self, surface):
        font = pygame.font.Font('freesansbold.ttf', 14)
        textSurf = font.render(self.text, True, self.textColorRGB)
        #center the text in the box
        textRect = textSurf.get_rect()
        textRect.center = getCenterFromRect(self.rect)
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(textSurf, textRect)

class Image(PageElement):
    def __init__(self, centerXY, width, height, imagePath):
        super().__init__(centerXY, width, height)
        self.imagePath = imagePath

    def display(self, surface):
        img = pygame.image.load(self.imagePath)
        img = pygame.transform.scale(img, (self.rect[2], self.rect[3]))
        surface.blit(img, (self.rect[0], self.rect[1]))


    def onClick(self, screen):
        print("You've clicked a useless image")

class Label(PageElement):
    def __init__(self, centerXY, width, height, text, fontSize=14, textColorRGB=(0,0,0)):
        super().__init__(centerXY, width, height, None)
        self.text = text
        self.fontSize = fontSize
        self.textColorRGB = textColorRGB

        #create font object to render text
        

    def display(self, surface):
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf', self.fontSize)
        
        #identify center location of top label within given box
        textPieces = self.text.split("\n")
        horizMid = self.rect[0] + self.rect[2] / 2
        vertMid = self.rect[1] + self.rect[3] / 2
        vertTop = vertMid - self.fontSize * floor(len(textPieces)/2)
        if len(textPieces) % 2 == 0:
            vertTop += self.fontSize / 2

        #start to place lines of text
        textSurfs = []
        textRects = []
        for line in textPieces:
            textSurf = font.render(line, True, self.textColorRGB)
            #center the text in the box
            textRect = textSurf.get_rect()
            textRect.center = (horizMid, vertTop)
            vertTop += self.fontSize

            textSurfs.append(textSurf)
            textRects.append(textRect)

        for i in range(len(textSurfs)):
            surface.blit(textSurfs[i], textRects[i])


def convertPercentRectToScreenRect(percentRect, screenDims):
    #centerCoord is a tuple (x, y) ranging from (0, 0) to (100, 100)
    #x increases from left to right
    #y increases from bottom to top
    l = percentRect[0]/100 * screenDims[0]
    t = percentRect[1]/100 * screenDims[1]
    w = percentRect[2]/100 * screenDims[0]
    h = percentRect[3]/100 * screenDims[1]
    return Rect(l, t, w, h)

def getRectFromCenter(centerCoord, width, height):
    l = centerCoord[0] - width/2
    t = 100 - (centerCoord[1] + height/2)
    return Rect(l,t,width,height)

def getCenterFromRect(rect):
    centerX = rect[0] + rect[2]/2
    centerY = rect[1] + rect[3]/2
    return (centerX, centerY)


    


        
    