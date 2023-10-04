import GameAdaptor

rules = '''UU-Game How to Play:
Objective:
•	UU-Game is a two-player strategy game. Each player has 12 starting pieces, with the objective of placing them strategically in a 24-intersection board game and eliminating the opponent’s pieces.
•	The goal is to form "mills" by aligning three of your pieces horizontally or vertically to gain the ability to remove the opponent’s pieces.
•	Your objective is to remove your opponent's pieces to reduce their count to two or make it impossible for them to make a legal move.
Setup:
The game board consists of 24 intersections or spots where you can place your pieces in the initial phase.
Starting the Game: Each player starts with 12 pieces of their color (Player Black and Player White).
Placing Pieces: Players take turns placing their pieces on empty spots. The game starts with Player Black.
Entering Your Move: To make a move, you must specify an alphanumeric location (e.g., "A1," "B2," "C3") to indicate where you want to place or move your pieces.
Forming Mills: When you manage to align three of your pieces in a row (horizontally or vertically), you've formed a mill. 
Removing Opponent's Pieces: After forming a mill, you can choose to remove one of your opponent's pieces from the board. Removed pieces can't be brought back. 
Opponent's Turn: After you remove one of your opponent's pieces, it becomes their turn.
Moving Pieces: After all pieces are on the board, players take turns moving their pieces to adjacent empty spots along the lines.
No Duplicate Mills: The game won't let you form the same mill twice to keep things fair.
Limited Mill Removal: You can't remove a piece from your opponent's mill (three in a row) unless they have only three pieces left.
Displaying the Game Board: Every two turns, the game board will be visually displayed in the terminal so that you can see the current game state.
Keeping Track: Throughout the game, you'll see how many pieces you and your opponent have left on the board.
Special Rule: Three Pieces Left: If you have only three pieces left, you can move them to any vacant spot on the board, not just adjacent ones.
Valid Moves: Your turn won't end until you make a valid move on the board, so you won't miss any opportunities.
Ending the Game: The game ends when one player is left with only two pieces or after 200 moves, resulting in a draw.
Winning: The player who meets one of the end-game conditions (two pieces left for the opponent or no legal moves) wins the game.
Game Feedback: The game provides feedback on what's happening, such as error messages or notifications for invalid moves.'''

a = GameAdaptor.GameAdaptor()
message = ''
while not a.game.isTheGameFinished():
    print('___________________________________________________________________________________________________')
    print()
    print(
        f'''A1 : [{a.representationOfBoard['A1'][0]}] ------------------------------- D1 : [{a.representationOfBoard['D1'][0]}] ------------------------------- G1 : [{a.representationOfBoard['G1'][0]}]
    | \               	      	          |                	       	     /  |
    |  \               	                  |                	            /   |
    |   \               	          |                	           /    |
    |     B2 : [{a.representationOfBoard['B2'][0]}] --------------------- D2 : [{a.representationOfBoard['D2'][0]}] --------------------- F2 : [{a.representationOfBoard['F2'][0]}] 
    |       | \                           |          	       	      / |       |
    |       |  \         		  |         		     /  |       |
    |       |   \                         |      		    /   |       |
    |       |    \			  |			   /    |       |
    |       |     C3 : [{a.representationOfBoard['C3'][0]}] ------------- D3 : [{a.representationOfBoard['D3'][0]}] ------------- E3 : [{a.representationOfBoard['E3'][0]}]|       |
    |       |       |                                           |     	|       |
    |       |       |                                           |     	|       |
    |       |       |                                           |     	|       |
    |       |       |                                           |     	|       |
A4 : [{a.representationOfBoard['A4'][0]}] - B4 : [{a.representationOfBoard['B4'][0]}] - C4 : [{a.representationOfBoard['C4'][0]}]                           E4 : [{a.representationOfBoard['E4'][0]}] - F4 : [{a.representationOfBoard['F4'][0]}] - G4 : [{a.representationOfBoard['G4'][0]}]
    |       |       |                                           |     	|       |
    |       |       |                                           |     	|       |
    |       |       |                                           |     	|       |
    |       |       |                                           |     	|       |
    |       |     C5 : [{a.representationOfBoard['C5'][0]}] ------------- D5 : [{a.representationOfBoard['D5'][0]}] ------------- E5 : [{a.representationOfBoard['E5'][0]}] |	|
    |       |	 /	   		  |	   		  \     |       | 
    |       |	/	   		  |	   		   \    |       |
    |       |  /	   		  |	   		    \   |       |
    |       | /	   		          |	   		     \  |       |
    |     B6 : [{a.representationOfBoard['B6'][0]}] --------------------- D6 : [{a.representationOfBoard['D6'][0]}] --------------------- F6 : [{a.representationOfBoard['F6'][0]}]|
    |   /			     	  |				   \    |
    |  /				  |				    \   |
    | /	   		    	          |				     \  |
A7 : [{a.representationOfBoard['A7'][0]}] ------------------------------- D7 : [{a.representationOfBoard['D7'][0]}] ------------------------------- G7 : [{a.representationOfBoard['G7'][0]}] ''')

    print('''To display rules of the game type "Rules"''')
    print()
    print(f'Player1 pieces left : {a.game.playersList[0].numberOfPieces}')
    print(f'Player2 pieces left : {a.game.playersList[1].numberOfPieces}')
    print()
    print(f'''Player holding {['black', 'white'][a.game.playerOnTurn]} pieces is on turn''')
    print(message)
    inp = input()
    
    if inp =='Rules':
        print(rules)
    else:
        message = a.play(inp)
