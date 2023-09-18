from Player import Player

class Game:

    def __init__(self):
        self.playerOnTurn = 1
        self.gamePhase = 'initial'
        self.numberOfTurns = 0
        self.playersList : list[Player]

    def play(self, playerOnTurn:int, gamePhase:str, moveTo:str) -> str:
        return 'dummy string'

    def isTheGameFinished(self, numberOfPiecesP1 : int, numberOfPiecesP2 : int) -> bool:
        return True
