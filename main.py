import pyxel
from board import Board

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.board = Board(0)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.board.update

    def draw(self):
        self.board.draw()


App()
