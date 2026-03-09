from PyUI.PageElements import *
from PyUI.Screen import Screen

class tScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (255, 255, 255))

    def elementsToDisplay(self):
        trianglePoints = [(50, 100), (0, 0), (100, 0)]
        starPoints = [
            (50.0, 90.0),
            (58.8191, 61.8083),
            (89.0211, 61.8034),
            (64.2705, 41.9577),
            (73.5114, 12.9443),
            (50.0, 30.0),
            (26.4886, 12.9443),
            (35.7295, 41.9577),
            (10.9789, 61.8034),
            (41.1809, 61.8083)
        ]
        trapezoidPoints = [
            (0,0),
            (33.3,100),
            (66.6,100),
            (100,0)
        ]
        self.elements = [
            Button((20, 80), 10, 10, "Hi", (255, 255,255), (0,0,0)),
            Button((20, 60), 10, 10, "Hi", (255, 255,255), (0,0,0)),
            Button((20, 40), 10, 10, "Hi", (255, 255,255), (0,0,0)),
            Button((20, 20), 10, 10, "Hi", (255, 255,255), (0,0,0)),

            Ellipse((50, 80), 30, 15, (0,0,0)),
            Ellipse((50, 60), 30, 15, (0,0,0)),
            Ellipse((50, 40), 30, 15, (0,0,0)),
            Ellipse((50, 20), 30, 15, (0,0,0)),

            Image((50, 80), 20, 20,     "./PyUI/Examples/hawk.png"),
            Image((50, 60), 20, 20,     "./PyUI/Examples/hawk.png"),
            Image((50, 40), 20, 20,   "./PyUI/Examples/hawk.png"),
            Image((50, 20), 20, 20,     "./PyUI/Examples/hawk.png"),

            Label((80, 80), 10, 10, "Hello World\nGoodBye World"),
            Shape((80,62), 10, 10, trianglePoints, (0,255,0)),
            Label((80, 60), 10, 10, "Go Hawks"),
            Shape((80, 40), 20, 20, starPoints, (0,255,0)),
            Label((80, 40), 10, 10, "Hello World\nGoodBye\nWorld"),
            Shape((80,20), 15, 15, trapezoidPoints, (0,255,0)),
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