from Player import Player
from Board import Board

class Game:

    def __init__(self, board : Board()):
        self.playerOnTurn = 1
        self.gamePhase = 'initial'
        self.numberOfTurns = 0
        self.playersList : list[Player] = [Player(1,'black', board), Player(2,'white', board)]
        self.board = board

    def play(self, playerOnTurn:int, gamePhase:str, moveTo:str) -> str:
        return 'dummy string'

    def isTheGameFinished(self, numberOfPiecesP1 : int, numberOfPiecesP2 : int) -> bool:
        return True
