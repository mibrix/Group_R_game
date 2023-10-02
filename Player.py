from Board import Board

class Player:

    def __init__(self, playerIdx : int, color : str, board : Board()):
        self.playerIdx = playerIdx
        self.numberOfPieces : int = 12
        self.color = color
        self.board = board
        #self.score = 0

        self.gamePhase = 'initial'  # initial(when players put the pieces from "pocket"
        # late = after all pieces have been placed to the board

    def play(self, initialPosition : str, moveTo : str) -> list:

        if self.gamePhase == 'initial':

            if initialPosition != 'H':
                return ['It is initial phase of the game. Starting position should be H']

        elif self.gamePhase == 'late':

            if self.board.boardRepresentation[initialPosition][0] != ['B', 'W'][self.playerIdx]:
                return ['You are not allowed to move the piece']

        if not self.board.isTheMoveLegal(initialPosition, moveTo, self.numberOfPieces):
            return ['You are not allowed to put a piece to intentioned position']


        temp = self.board.movePiece(initialPosition, moveTo, self.playerIdx, self.numberOfPieces)


        if temp == 'Piece was moved succesfully. Mill was formed':
            self.increaseScore()

        return temp



    def getScore(self):
        """ The current score of this player """
        return self.score


    def increaseScore(self):
        """ Increase the score of this player by 1."""
        self.score += 1


