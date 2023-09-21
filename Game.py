from Player import Player
from Board import Board

class Game:

    def __init__(self, board : Board()):
        self.playerOnTurn = 0   #player0 or player1
        self.numberOfTurns = 0      #incriment after every turn
        self.playersList : list[Player] = [Player(0,'black', board), Player(1,'white', board)]
        self.board = board

    def play(self,  initialPosition : str, moveTo:str) -> str:
        #call appropriate method for player on turn

        temp = self.playersList[self.playerOnTurn].play(initialPosition, moveTo)
        print(f'here: {temp}')
        if 'Piece was moved succesfully' in temp:

            if self.playerOnTurn == 0:
                self.playerOnTurn = 1

            elif self.playerOnTurn == 1:
                self.playerOnTurn = 0

            self.numberOfTurns += 1

        return temp

    def isTheGameFinished(self, numberOfPiecesP1 : int, numberOfPiecesP2 : int) -> bool:
        #check if the game is finished

        #if the game is finished
        return True

        #else return false
