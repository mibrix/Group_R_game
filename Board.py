class Board:

    def __init__(self):
        self.boardRepresentation = {'A1' : ('E',['A4','D1']),       #finish this variable based on picture of coordinate system
                                    'D1' : ('E',['A1','G1','D2'])}  #if player with black pieces place a piece to D1 then change
                                                                    # "E" to "B"
                                                                    # elif player with white pieces place a piece to D1 then change
                                                                    # "E" to "W"
                                                                    # E = empty; B = black; W = white
        self.historyOfMoves = []    #use this variable to evaluate if the mill counts
                                    #you can update this variable in method movePiece

    def isTheMoveLegal(self, initialPosition : str, moveTo : str) -> bool:  #if player plays invalid move: return False else True
        return False

    def movePiece(self, initialPosition : str, moveTo : str) -> bool:
        return True # if mill that counts is formed return True else False