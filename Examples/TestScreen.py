from PyUI.PageElements import *
from PyUI.Screen import Screen

class tScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (255, 255, 255))

    def elementsToDisplay(self):
        self.elements = [
            Button((20, 80), 10, 10, "Hi", (255, 255,255), (0,0,0)),
            Button((20, 60), 10, 10, "Hi", (255, 255,255), (0,0,0)),
            Button((20, 40), 10, 10, "Hi", (255, 255,255), (0,0,0)),
            Button((20, 20), 10, 10, "Hi", (255, 255,255), (0,0,0)),

            Image((50, 80), 10, 10, "./hawk.jpeg"),
            Image((50, 60), 10, 10, "./hawk.jpeg"),
            Image((50, 50), 100, 100, "./hawk.jpeg"),
            Image((50, 20), 10, 10, "./hawk.jpeg"),

            Label((80, 80), 10, 10, "Hello World\nGoodBye World"),
            Label((80, 60), 10, 10, "Hello WorldGoodBye World"),
            Label((80, 40), 10, 10, "Hello World\nGoodBye\nWorld"),
            Label((80, 20), 10, 10, "Welp")
        ]