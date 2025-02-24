from pygame import Rect
import pygame
from os import getcwd
from math import floor

class PageElement:
    def __init__(self, topLeftLoc, width, height, colorRGB=(255,255,255)):
        self.rect = Rect(topLeftLoc[0], topLeftLoc[1], width, height)
        self.color = colorRGB

    def wasClicked(self, clickLoc):
        if self.rect.collidepoint(clickLoc[0], clickLoc[1]):
            return True
        return False
    
    def display(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def onClick(self, screen):
        print("You've clicked a useless page element")


class Button(PageElement):

    def __init__(self, topLeftLoc, width, height, text, textColorRGB=(0,0,0), backColorRGB=(255,255,255)):
        super().__init__(topLeftLoc, width, height, backColorRGB)
        # pygame.font.init()
        self.text = text
        font = pygame.font.Font('freesansbold.ttf', 14)
        self.textSurf = font.render(self.text, True, textColorRGB)
        #center the text in the box
        textRect = self.textSurf.get_rect()
        textRect.center = (self.rect[0] + width / 2, self.rect[1] + height / 2)
        self.textRect = textRect
    
    def onClick(self, screen):
        print("a ha! You've found a useless button. Great Work")
        print('The text on this button is: ' + self.text)

    def display(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.textSurf, self.textRect)

class Image(PageElement):
    def __init__(self, topLeftLoc, width, height, imagePath):
        super().__init__(topLeftLoc, width, height)
        self.imagePath = imagePath

    def display(self, surface):
        img = pygame.image.load(self.imagePath)
        img = pygame.transform.scale(img, (self.rect[2], self.rect[3]))
        surface.blit(img, (self.rect[0], self.rect[1]))


    def onClick(self, screen):
        print("You've clicked a useless image")

class Label(PageElement):
    def __init__(self, topLeftLoc, width, height, text, fontSize=14, textColorRGB=(0,0,0)):
        super().__init__(topLeftLoc, width, height, None)

        #create font object to render text
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf', fontSize)
        
        
        #identify center location of top label within given box
        textPieces = text.split("\n")
        horizMid = self.rect[0] + width / 2
        vertMid = self.rect[1] + height / 2
        vertTop = vertMid - fontSize * floor(len(textPieces)/2)
        if len(textPieces) % 2 == 0:
            vertTop += fontSize / 2

        #start to place lines of text
        self.textSurfs = []
        self.textRects = []
        for line in textPieces:
            textSurf = font.render(line, True, textColorRGB)
            #center the text in the box
            textRect = textSurf.get_rect()
            textRect.center = (self.rect[0] + width / 2, vertTop)
            vertTop += fontSize

            self.textSurfs.append(textSurf)
            self.textRects.append(textRect)

    def display(self, surface):
        for i in range(len(self.textSurfs)):
            surface.blit(self.textSurfs[i], self.textRects[i])

        
    