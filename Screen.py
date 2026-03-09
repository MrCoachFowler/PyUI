class Screen:

    def __init__(self, window, colorRGB):
        self.surface = window.screen
        self.elements = []
        self.color = colorRGB
        self.state = {}
        self.waitForNextFrame = 0

    def elementsToDisplay(self):
        #override this with the elements to render
        #attach the elements as a list to the screen object
        #example:
        #self.elements = [
            #Button(),
            #Label()
        #]
        pass


    def display(self, screenDims):
        self.elementsToDisplay()
        for e in self.elements:
            e.adjustToScreenSize(screenDims)
            e.display(self.surface)
        
        
