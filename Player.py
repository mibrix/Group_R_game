from Board import Board

class Player:

    def __init__(self, playerIdx : int, color : str, board : Board()):
        self.playerIdx = playerIdx
        self.numberOfPieces : int = 12
        self.color = color
        self.board = board

    def play(self, initialPosition : str, moveTo : str) -> str:
        return 'dummy string'
