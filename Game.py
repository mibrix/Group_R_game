from Player import Player
from Board import Board

class Game:

    def __init__(self, board : Board()):
        self.playerOnTurn = 1   #player1 or player2
        self.gamePhase = 'initial'  #initial(when players put the pieces from "pocket"
                                    #late = after all pieces have been placed to the board
        self.numberOfTurns = 0      #incriment after every turn
        self.playersList : list[Player] = [Player(1,'black', board), Player(2,'white', board)]
        self.board = board

    def play(self, playerOnTurn:int, gamePhase:str, moveTo:str) -> str:
        #call appropriate method for player on turn
        return 'dummy string'

    def isTheGameFinished(self, numberOfPiecesP1 : int, numberOfPiecesP2 : int) -> bool:
        #check if the game is finished

        #if the game is finished
        return True

        #else return false
