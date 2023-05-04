import pyxel

class Board:
    def __init__(self, bag):
        self.matrix = [["" for i in range(10)] for i in range(16)] 
        self.bag = bag    

    def draw(self):
        offsetx = 60
        offsety = 20
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                pyxel.rectb(offsetx+4*j, offsety+4*i, 4, 4, 13)

    def update(self):
        pass
