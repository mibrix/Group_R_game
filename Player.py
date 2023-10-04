from Board import Board

class Player:

    def __init__(self, playerIdx : int, color : str, board : Board()):
        self.playerIdx = playerIdx
        self.numberOfPieces : int = 12
        self.placedPieces = 0
        self.color = color
        self.board = board

        self.gamePhase = 'initial'  # initial(when players put the pieces from "pocket"
        # late = after all pieces have been placed to the board

    def play(self, initialPosition : str, moveTo : str) -> list:

        if self.gamePhase == 'initial':

            if initialPosition != 'H':
                return ['It is initial phase of the game. Starting position should be H']

        elif self.gamePhase == 'late':

            if initialPosition == 'H':
                return ['It is after initial phase of the game. You are allowed to move only the pieces placed on board.']

            if self.board.boardRepresentation[initialPosition][0][0] != ['B', 'W'][self.playerIdx]:
                return ['You are not allowed to move the piece']

        if not self.board.isTheMoveLegal(initialPosition, moveTo, self.numberOfPieces):
            return ['You are not allowed to put a piece to intentioned position']


        temp = self.board.movePiece(initialPosition, moveTo, self.playerIdx, self.placedPieces, self.numberOfPieces)

        if self.gamePhase == 'initial':
            self.placedPieces += 1


        return temp



