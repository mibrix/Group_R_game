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

        if len(move.split(' to ')) == 1:
            return 'Incorrect input. Try again!'

        if len(move.split(' to ')) == 2 and move.split(' to ')[1] not in ['A1', 'D1', 'G1', 'A4', 'G4', 'A7', 'D7',
                                                                          'G7', 'B2', 'D2', 'F2', 'F4', 'F6', 'D6',
                                                                          'B6', 'B4', 'C3', 'D3', 'E3', 'E4', 'E5',
                                                                          'D5', 'C5', 'C4']:
            return 'Incorrect input. Try again!'

        initialPosition = move.split(' to ')[0]
        moveTo = move.split(' to ')[1]

        temp = self.game.play(initialPosition, moveTo)

        return temp[0]


#tests

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