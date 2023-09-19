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
        self.historyOfMoves = []    #use this variable to evaluate if the mill counts
                                    #you can update this variable in method movePiece
                                    # P1 H B2
                                    # P1 B2 B4 M[B1:A1, B3:D1, B2:G1] | M is present when a legal mill is formed by this move

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

    def isTheMoveLegal(self, initialPosition : str, moveTo : str, playerIdx : int) -> bool:  #if player plays invalid move: return False else True
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
            else:
                return False

    def movePiece(self, initialPosition : str, moveTo : str, playerIdx : int) -> bool:

        if initialPosition != 'H':
            self.boardRepresentation[initialPosition][0] = 'E'

        self.boardRepresentation[moveTo][0] = ['B', 'W'][playerIdx]

        #don't mind comments in slovak, they will be removed
        #mill was formed
        #algoritmus, ktory pojde dva kroky kazdym smerom, pokial ma ten isty hrac polozeny piece na danom mieste
        #z kazdej cesty spravy pole
        #tieto polia potom prejdu for cyklom ci sa nahodou nenachadzaju v liste moznych millov
        paths = []
        for adj in self.boardRepresentation[moveTo][1]:
            if self.boardRepresentation[adj][0] == ['B', 'W'][playerIdx]:
                paths.append([moveTo, adj])


        paths_three = []
        #pridaj susedovho suseda
        for path in paths:
            for adj in self.boardRepresentation[path[-1]][1]:
                if self.boardRepresentation[adj][0] == ['B', 'W'][playerIdx] and adj not in path:
                    paths_three.append(path + [adj])

        for path in paths_three:
            if set(path) in self.possibleMills:
                print(path)
                return True

        #este treba skontrolovat ci nebol sformovany mlyn iba na dva tahy (posunutim jedneho piecu a vratenim ho naspat)
            #toto bude zrejme treba osetrit cislovanim jednotlivych pieces

        #history of moves
        self.historyOfMoves.append(f'P{playerIdx} {initialPosition} {moveTo}')

        return True # if mill that counts is formed return True else False

a = Board()
a.movePiece('H', 'A1', 0)
a.movePiece('H', 'D1', 0)
a.movePiece('H', 'G1', 0)




#adjecency list
# A1 D1 A4 B2
# D1 A1 G1 D2
# G1 D1 F2 G4
# A4 B4 A7 A1
# G4 F4 G1 G7
# A7 A4 B6 D7
# D7 A7 G7 D6
# G7 D7 G4 F6
#
# B2 A1 D2 B4 C3
# D2 F2 D3 B2 D1
# F2 D2 E3 F4 G1
# F4 E4 G4 F6 F2
# F6 D6 E5 G7 F4
# D6 B6 F6 D5 D7
# B6 D6 A7 B4 C5
# B4 C4 B6 B2 A4
#
# C3 D3 C4 B2
# D3 C3 E3 D2
# E3 E4 D3 F2
# E4 E3 F4 E5
# E5 D5 E4 F6
# D5 C5 E5 D6
# C5 C4 D5 B6
# C4 C5 C3 B4

#all possible mills

# A1 D1 G1
# B2 D2 F2
# C3 D3 E3
# A4 B4 C4
# E4 F4 G4
# C5 D5 E5
# B6 D6 F6
# A7 D7 G7
#
# A1 A4 A7
# B2 B4 B6
# C3 C4 C5
# D1 D2 D3
# D5 D6 D7
# E3 E4 E5
# F2 F4 F6
# G1 G4 G7
#
# A1 B2 C3
# E3 F2 G1
# E5 F6 G7
# A7 B6 C5





