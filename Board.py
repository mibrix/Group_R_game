class Board:

    def __init__(self):
        self.boardRepresentation = {'A1' : ('E',['A4','D1']),
                                    'D1' : ('E',['A1','G1','D2'])}
        self.historyOfMoves = []

    def isTheMoveLegal(self, initialPosition : str, moveTo : str) -> bool:
        return False

    def movePiece(self, initialPosition : str, moveTo : str) -> bool:
        return True # if mill that counts is formed return True else False