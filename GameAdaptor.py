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

    def play(self, move : str):
        'A4 to B4'
        'H to B4'

        initialPosition = move.split(' to ')[0]
        moveTo = move.split(' to ')[1]

        temp = self.game.play(initialPosition, moveTo)

        return temp[0]


# a = GameAdaptor()
# print(a.play('A1 to D1'))

# a = GameAdaptor()
# print(a.game.playerOnTurn)
# print(a.play('H to D1'))
# print(a.game.playerOnTurn)
# print(a.play('H to A1'))
# print(a.game.playerOnTurn)
# print(a.play('H to D2'))
# print(a.game.playerOnTurn)
# print(a.play('H to A4'))
# print(a.game.playerOnTurn)
# print(a.play('H to D3'))
# print(a.game.playerOnTurn)
# print(a.play('H to A7'))
# print(a.game.playerOnTurn)