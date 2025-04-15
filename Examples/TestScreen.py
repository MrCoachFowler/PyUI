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

            Image((50, 80), 20, 20,     "./PyUI/Examples/hawk.png"),
            Image((50, 60), 20, 20,     "./PyUI/Examples/hawk.png"),
            Image((50, 40), 20, 20,   "./PyUI/Examples/hawk.png"),
            Image((50, 20), 20, 20,     "./PyUI/Examples/hawk.png"),

            Label((80, 80), 10, 10, "Hello World\nGoodBye World"),
            Label((80, 60), 10, 10, "Go Hawks"),
            Label((80, 40), 10, 10, "Hello World\nGoodBye\nWorld"),
            Label((80, 20), 10, 10, "Welp"),

            Rectangle((50, 95), 100, 10, (10,255,20)),
            Rectangle((50, 5), 100, 10, (10,255,20)),
            Rectangle((5, 50), 10, 100, (10,255,20)),
            Rectangle((95, 50), 10, 100, (10,255,20)),

            Line((5, 5), (5, 95), (0,0,0), 4),
            Line((5, 5), (95, 5), (0,0,0), 4),
            Line((5, 95), (95, 95), (0,0,0), 4),
            Line((95, 5), (95, 95), (0,0,0), 4)
        ]