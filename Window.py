import pygame
from time import sleep

class Window:

    def __init__(self, title="Test App", colorRGB=False, customIconPath=False):
        pygame.init()
        self.screenDims = (800,600)
        self.screen = pygame.display.set_mode(self.screenDims, pygame.RESIZABLE)
        pygame.display.set_caption(title)
        if customIconPath:
            icon = pygame.image.load(customIconPath)
            pygame.display.set_icon(icon)
        self.color = (0, 0, 0)
        if customIconPath:
            icon = pygame.image.load(customIconPath)
            pygame.display.set_icon(icon)
        if colorRGB:
            self.color = colorRGB
        self.screen.fill(self.color)

    def setColor(self, colorRGB):
        self.screen.fill(colorRGB)

  
    def update(self, screenObj=False):
        if screenObj:
            self.screen.fill(screenObj.color)
            screenObj.display(self.screenDims)

        else:
            self.screen.fill(self.color)

        pygame.display.flip()

        if screenObj:
            if screenObj.waitForNextFrame:
                sleep(screenObj.waitForNextFrame)
                screenObj.waitForNextFrame  = 0

    def checkForInput(self, screen):
        #check for inputs
        for event in pygame.event.get():
            #handle various inputs
            ##quit type    
            if event.type == pygame.QUIT: 
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                clickLoc = pygame.mouse.get_pos()
                for e in screen.elements[::-1]:
                    if e.wasClicked(clickLoc):
                        e.onClick(screen)
                        return
                    
            if event.type == pygame.VIDEORESIZE:
                self.screenDims = self.screen.get_size()

    def checkForHover(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        for e in screen.elements[::-1]:
            if pygame.mouse.get_focused() != False:
                if e.wasHovered(mouse_pos):
                    e.onHover(screen)
                else:
                    e.notHovered(screen)
                    return


                    
