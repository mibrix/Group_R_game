from Game import Game
from Board import Board

class GameAdaptor:

    def __init__(self):
        self.rules : str = "Rules: Game starts with so called initial phase..."
        self.piecesLeftPlayer1 : int = 12
        self.piecesLeftPlayer2 : int = 12
        self.board = Board()
        self.game = Game(self.board)
        self.representationOfBoard: dict[str, tuple[str, list[str]]] = self.board.boardRepresentation

    def notify(self, message : str):
        print(message)

    def play(self, move : str):
        True