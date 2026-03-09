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
    
    def wasHovered(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        return False
    
    def display(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def onClick(self, screen):
        print("You've clicked a useless page element")

    def onHover(self, screen):
        pass

    def notHovered(self, screen):
        pass

    def adjustToScreenSize(self, screenDims):
        #call on screen size adjust event?
        #https://www.pygame.org/docs/ref/display.html#:~:text=If%20the%20display%20is%20set,the%20window%20must%20be%20redrawn.
        self.rect = convertPercentRectToScreenRect(self.percentRect, screenDims)

class Rectangle(PageElement):
    def __init__(self, centerXY, width, height, color):
        super().__init__(centerXY, width, height, color)

    def display(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Line(PageElement):
    def __init__(self, bottomLeftCoord, topRightCoord, color=(0,0,0), pixelWidth=3):
        centerXY = ( (bottomLeftCoord[0] + topRightCoord[0]) / 2, (bottomLeftCoord[1] + topRightCoord[1]) / 2)
        width = topRightCoord[0] - bottomLeftCoord[0]
        height = topRightCoord[1] - bottomLeftCoord[1]
        super().__init__(centerXY, width, height, color)
        self.pixelWidth = pixelWidth

    def wasClicked(self, clickLoc): #disable clicking on lines for now...
        pass

    def display(self, surface):
        pygame.draw.line(surface, self.color, self.rect.bottomleft, self.rect.topright, self.pixelWidth)

class Ellipse(PageElement):
    def __init__(self, centerXY, width, height, color=(255,255,255)):
        super().__init__(centerXY, width, height, color)

    def display(self, surface):
        pygame.draw.ellipse(surface, self.color, self.rect)

    def onClick(self, screen):
        pass #disable click by default

class Shape(PageElement):
    def __init__(self, centerXY, width, height, points, color=(255,255,255)):
        super().__init__(centerXY, width, height, color)
        self.scalablePoints = []
        for p in points:
            scalableX = (p[0] - 50)/100
            scalableY = (p[1] - 50)/100
            self.scalablePoints.append((scalableX, scalableY))

    def adjustToScreenSize(self, screenDims):
        super().adjustToScreenSize(screenDims)
        self.points = []
        center = getCenterFromRect(self.rect)
        for p in self.scalablePoints:
            pX = p[0] * self.rect.width + center[0]
            pY = -p[1] * self.rect.height + center[1]
            self.points.append((pX, pY))
            
    def display(self, surface):
        pygame.draw.polygon(surface, self.color, self.points)

    def onClick(self, screen):
        pass #disable clicking by default

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

    def onHover(self, screen):
        pass

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
        pass #disable for images by default

class Label(PageElement):
    def __init__(self, centerXY, width, height, text, fontSize=14, textColorRGB=(0,0,0), backColorRGB=False):
        super().__init__(centerXY, width, height, None)
        self.text = text
        self.fontSize = fontSize
        self.textColorRGB = textColorRGB
        self.backColorRGB = backColorRGB

        #create font object to render text
        

    def display(self, surface):
        if self.backColorRGB:
            pygame.draw.rect(surface, self.backColorRGB, self.rect)
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


    


        
    
