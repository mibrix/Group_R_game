import GameAdaptor

a = GameAdaptor.GameAdaptor()

while not a.game.isTheGameFinished():
    print('___________________________________________________________________________________________________')
    print()
    print(f'''A1 : {a.representationOfBoard['A1'][0]} ------------------------------- D1 : {a.representationOfBoard['D1'][0]} ------------------------------- G1 : {a.representationOfBoard['G1'][0]}
    | \               	      	          |                	       	     /  |
    |  \               	                  |                	            /   |
    |   \               	          |                	           /    |
    |     B2 : {a.representationOfBoard['B2'][0]} --------------------- D2 : {a.representationOfBoard['D2'][0]} --------------------- F2 : {a.representationOfBoard['F2'][0]}      |
    |       | \                           |          	       	      / |       |
    |       |  \         		  |         		     /  |       |
    |       |   \                         |      		    /   |       |
    |       |    \			  |			   /    |       |
    |       |     C3 : {a.representationOfBoard['C3'][0]} ------------- D3 : {a.representationOfBoard['D3'][0]} ------------- E3 : {a.representationOfBoard['E3'][0]}      |       |
    |       |       |                                           |     	|       |
    |       |       |                                           |     	|       |
    |       |       |                                           |     	|       |
    |       |       |                                           |     	|       |
A4 : {a.representationOfBoard['A4'][0]} - B4 : {a.representationOfBoard['B4'][0]} - C4 : {a.representationOfBoard['C4'][0]}                                    E4 : {a.representationOfBoard['E4'][0]} - F4 : {a.representationOfBoard['F4'][0]} - G4 : {a.representationOfBoard['G4'][0]}
    |       |       |                                           |     	|       |
    |       |       |                                           |     	|       |
    |       |       |                                           |     	|       |
    |       |       |                                           |     	|       |
    |       |     C5 : {a.representationOfBoard['C5'][0]} ------------- D5 : {a.representationOfBoard['D5'][0]} ------------- E5 : {a.representationOfBoard['E5'][0]}      |	|
    |       |	 /	   		  |	   		  \     |       | 
    |       |	/	   		  |	   		   \    |       |
    |       |  /	   		  |	   		    \   |       |
    |       | /	   		          |	   		     \  |       |
    |     B6 : {a.representationOfBoard['B6'][0]} --------------------- D6 : {a.representationOfBoard['D6'][0]} --------------------- F6 : {a.representationOfBoard['F6'][0]}      |
    |   /			     	  |				   \    |
    |  /				  |				    \   |
    | /	   		    	          |				     \  |
A7 : {a.representationOfBoard['A7'][0]} ------------------------------- D7 : {a.representationOfBoard['D7'][0]} ------------------------------- G7 : {a.representationOfBoard['G7'][0]} ''')


    print(f'Player1 pieces left : {a.game.playersList[0].numberOfPieces}')
    print(f'Player2 pieces left : {a.game.playersList[1].numberOfPieces}')
    print()
    print(f'''Player holding {['black','white'][a.game.playerOnTurn]} pieces is on turn''')
    inp = input()
    a.play(inp)

    
