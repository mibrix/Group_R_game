class Move:

    def __init__(self, initialPosition : str, moveTo : str, playerIdx : int, millsFormed : list[dict], pieceIdx : int):
        self.initialPosition = initialPosition
        self.moveTo = moveTo
        self.playerIdx = playerIdx
        self.millsFormed = millsFormed
        self.pieceIdx = pieceIdx  #B1 detones first piece of a player that holds black pieces

class Board:

    def __init__(self):
        self.boardRepresentation = { 'A1' : ['E', {'B2', 'D1', 'A4'}],
                                     'D1' : ['E', {'A1', 'G1', 'D2'}],
                                     'G1' : ['E', {'F2', 'D1', 'G4'}],
                                     'A4' : ['E', {'B4', 'A7', 'A1'}],
                                     'G4' : ['E', {'G7', 'F4', 'G1'}],
                                     'A7' : ['E', {'B6', 'A4', 'D7'}],
                                     'D7' : ['E', {'G7', 'A7', 'D6'}],
                                     'G7' : ['E', {'F6', 'G4', 'D7'}],

                                     'B2': ['E', {'B4', 'C3', 'A1', 'D2'}],
                                     'D2': ['E', {'F2', 'B2', 'D1', 'D3'}],
                                     'F2': ['E', {'E3', 'D2', 'F4', 'G1'}],
                                     'F4': ['E', {'F2', 'F6', 'E4', 'G4'}],
                                     'F6': ['E', {'E5', 'F4', 'G7', 'D6'}],
                                     'D6': ['E', {'B6', 'D5', 'F6', 'D7'}],
                                     'B6': ['E', {'B4', 'A7', 'C5', 'D6'}],
                                     'B4': ['E', {'B6', 'B2', 'A4', 'C4'}],

                                     'C3': ['E', {'B2', 'D3', 'C4'}],
                                     'D3': ['E', {'C3', 'E3', 'D2'}],
                                     'E3': ['E', {'F2', 'E4', 'D3'}],
                                     'E4': ['E', {'E3', 'F4', 'E5'}],
                                     'E5': ['E', {'D5', 'E4', 'F6'}],
                                     'D5': ['E', {'D6', 'C5', 'E5'}],
                                     'C5': ['E', {'B6', 'D5', 'C4'}],
                                     'C4': ['E', {'C3', 'B4', 'C5'}]
                                     }  #if player with black pieces place a piece to D1 then change
                                                                    # "E" to "B"
                                                                    # elif player with white pieces place a piece to D1 then change
                                                                    # "E" to "W"
                                                                    # E = empty; B = black; W = white
        self.historyOfMoves = []


        self.possibleMills = [{'A1', 'D1', 'G1'}, {'B2', 'D2', 'F2'},
                              {'C3', 'D3', 'E3'}, {'A4', 'B4', 'C4'},
                              {'E4', 'F4', 'G4'}, {'C5', 'D5', 'E5'},
                              {'B6', 'D6', 'F6'}, {'A7', 'D7', 'G7'},
                              {'A1', 'A4', 'A7'}, {'B2', 'B4', 'B6'},
                              {'C3', 'C4', 'C5'}, {'D1', 'D2', 'D3'},
                              {'D5', 'D6', 'D7'}, {'E3', 'E4', 'E5'},
                              {'F2', 'F4', 'F6'}, {'G1', 'G4', 'G7'},
                              {'A1', 'B2', 'C3'}, {'E3', 'F2', 'G1'},
                              {'E5', 'F6', 'G7'}, {'A7', 'B6', 'C5'}]

        #diagonal mill counts as well?

    def isTheMoveLegal(self, initialPosition : str, moveTo : str, piecesLeft : int) -> bool:  #if player plays invalid move: return False else True
        #two cases

        #from home to board
        if initialPosition == 'H':
            if self.boardRepresentation[moveTo][0] == 'E':
                return True
            else:
                return False

        #moving pieces on board
        else:
            #if initialPosition is adjecent to the moveTo position AND is empty
            if moveTo in self.boardRepresentation[initialPosition][1] and self.boardRepresentation[moveTo][0] == 'E':
                return True
            #player has only three pieces left, so he can move the piece wherever
            elif piecesLeft == 3 and self.boardRepresentation[moveTo][0] == 'E':
                return True
            else:
                return False

    def removeOpponentPiece(self, opponentIdx : int ):
        '''return True for valid input else False'''
        print('''Remove opponet's piece''')
        piecePosition: str = input()

        if piecePosition not in ['A1', 'D1', 'G1', 'A4', 'G4', 'A7', 'D7',
                                        'G7', 'B2', 'D2', 'F2', 'F4', 'F6', 'D6',
                                        'B6', 'B4', 'C3', 'D3', 'E3', 'E4', 'E5',
                                        'D5', 'C5', 'C4']:
            print('Illgegal position. Do it again.')
            return False

        if self.boardRepresentation[piecePosition][0][0] == ['B','W'][opponentIdx]:
            self.boardRepresentation[piecePosition][0] = 'E'
            return True
        else:
            print('Illgegal position. Do it again.')
            return False

    def movePiece(self, initialPosition : str, moveTo : str, playerIdx : int, pieceIdx : int) -> list:

        if initialPosition != 'H':
            self.boardRepresentation[initialPosition][0] = 'E'

        self.boardRepresentation[moveTo][0] = ['B', 'W'][playerIdx] + str(pieceIdx)

        self.historyOfMoves.append(Move(initialPosition, moveTo, playerIdx, [{}], pieceIdx))

        #Mill was formed

        #logic of the algorithm below:
            #go two steps in graph each way
            #form paths consisting only of pieces of a certain player
            #check if any of this paths are a mill
        paths = []
        for adj in self.boardRepresentation[moveTo][1]:
            if self.boardRepresentation[adj][0][0] == ['B', 'W'][playerIdx]:
                paths.append([moveTo, adj])

        paths_three = []
        #add neighbour of a neighbour
        for path in paths:
            for adj in self.boardRepresentation[path[-1]][1]:
                for adj1 in self.boardRepresentation[path[0]][1]:
                    if self.boardRepresentation[adj][0][0] == ['B', 'W'][playerIdx] and adj not in path:
                        if set(path + [adj]) not in [set(temp) for temp in paths_three]:
                            paths_three.append(path + [adj])
                    if self.boardRepresentation[adj1][0][0] == ['B', 'W'][playerIdx] and adj1 not in path:
                        if set(path + [adj1]) not in [set(temp) for temp in paths_three]:
                            paths_three.append(path + [adj1])


        formed_mills = []
        for path in paths_three:
            if set(path) in self.possibleMills:
                formed_mills.append(path)

        formed_mills_pieces = []
        for mill in formed_mills:
            temp = {}
            for coordinate in mill:
                temp[coordinate] = self.boardRepresentation[coordinate][0]
            formed_mills_pieces.append(temp)

        if formed_mills_pieces == []:
            return ['Piece was moved succesfully',0]

        #next section evaluates whether player will be awarded with points for forming a mill

        #if such mill was never formed before
        bol = [True for _ in range(len(formed_mills_pieces))]
        for n, move in enumerate(self.historyOfMoves[::-1]):
            for c,mill in enumerate(formed_mills_pieces):
                if mill in move.millsFormed:
                    bol[c] = False

        final_mills = []

        for n,mill in enumerate(formed_mills_pieces):
            if bol[n]:
                final_mills.append(mill)
                formed_mills_pieces[n] = False

        #find out whether the mill was formed by a player in the past
        for n,move in enumerate(self.historyOfMoves[::-1]):
            for mill in formed_mills_pieces:
                if mill in move.millsFormed and mill != False:
                    move_of_piece = {}

                    for pieceId in mill.values():
                        move_of_piece[pieceId] = 0

                    for move_new in self.historyOfMoves[::-1][:n]:
                        move_of_piece[['B', 'W'][playerIdx] + str(move_new.pieceIdx)] += 1

                    if sum(move_of_piece.values()) > 2:
                        # add mill to history if legal
                        final_mills.append(mill)


        self.historyOfMoves[-1].millsFormed = final_mills


        if final_mills != []:
            for _ in range(len(final_mills)):
                while not self.removeOpponentPiece((playerIdx - 1) % 2):
                    True
            return [f'Piece was moved succesfully. {len(final_mills)} mill(s) was/were formed', len(final_mills)]
        else:
            return ['Piece was moved succesfully',0]



#Tests:

# a = Board()
# a.movePiece('H', 'A1', 0, 1)
# a.movePiece('H', 'D1', 0, 2)
# a.movePiece('H', 'G7', 0, 3)
# a.movePiece('H', 'G4', 0, 4)
# print(a.movePiece('H', 'G1', 0, 5))
#
# a.movePiece('A1', 'A4', 0, 1)
# print(a.movePiece('A4', 'A1', 0, 1))
# #
#
# print('_________________________')
# for i in a.historyOfMoves:
#     print(i.initialPosition,
#         i.moveTo,
#         i.playerIdx,
#         i.millsFormed,
#         i.pieceIdx)
# print('_________________________')
#
#
# print([i.pieceIdx for i in a.historyOfMoves])





