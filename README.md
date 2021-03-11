# Tic-Tac-Toe

An implementation of Minimax AI Algorithm on Tic-Tac-Toe (or Noughts and Crosses) game.

Min-max is a decision-making algorithm which uses decision theory, game theory, statistics and 
philosophy to calculate the optimal move. The mechanism evaluates minimum lose and maximum profit. 
This logic can also be extended to play more complicated game like chess, checkers etc.


##How does it works?

Pseudocode (adapted):

``` 
minimax( max_min_type):
    
    IF the game is over and the bot won
        THEN return 1
        
    ELSE IF the game is over and the human 
        THEN retrun -1
        
    ELSE IF the game is over and it's draw
        THEN return 0
    
    ELSE 
    {
        IF max_type algorithm THEN
            best_score ← -10
            FOR every move in a possible_mover_tabble
                make_move(move)
                score ← minimax_algorithm(min_type)
                undo_move()
                IF score is greater then best_score THEN
                    best_score ← score
            ENDFOR
            
        IF min_type algorithm THEN
            best_score ← 10
            FOR every move in a possible_mover_tabble
                make_move(move)
                score ← minimax_algorithm(max_type)
                undo_move()
                IF score is smaller then best_score THEN
                    best_score ← score
            ENDFOR 
       
        return best_score
    }

```

## Usage

```python
Welcome to Tic Tac Toe!


	      1      2     3
	          |     |
	 1        |     |   
	    ______|_____|_____
	          |     |
	 2        |     |   
	    ______|_____|_____
	          |     |
	 3        |     |   
	          |     |


Do you want to be 'X' (moves first) or 'O' ?
o
AI turn


	      1      2     3
	          |     |
	 1     X  |     |   
	    ______|_____|_____
	          |     |
	 2        |     |   
	    ______|_____|_____
	          |     |
	 3        |     |   
	          |     |


Your turn
Which box (RowColumn)? : 
13


	      1      2     3
	          |     |
	 1     X  |     |  O
	    ______|_____|_____
	          |     |
	 2        |     |   
	    ______|_____|_____
	          |     |
	 3        |     |   
	          |     |


AI turn


	      1      2     3
	          |     |
	 1     X  |     |  O
	    ______|_____|_____
	          |     |
	 2     X  |     |   
	    ______|_____|_____
	          |     |
	 3        |     |   
	          |     |


Your turn
Which box (RowColumn)? : 
31


	      1      2     3
	          |     |
	 1     X  |     |  O
	    ______|_____|_____
	          |     |
	 2     X  |     |   
	    ______|_____|_____
	          |     |
	 3     O  |     |   
	          |     |


AI turn


	      1      2     3
	          |     |
	 1     X  |     |  O
	    ______|_____|_____
	          |     |
	 2     X  |  X  |   
	    ______|_____|_____
	          |     |
	 3     O  |     |   
	          |     |


Your turn
Which box (RowColumn)? : 
33


	      1      2     3
	          |     |
	 1     X  |     |  O
	    ______|_____|_____
	          |     |
	 2     X  |  X  |   
	    ______|_____|_____
	          |     |
	 3     O  |     |  O
	          |     |


AI turn


	      1      2     3
	          |     |
	 1     X  |     |  O
	    ______|_____|_____
	          |     |
	 2     X  |  X  |  X
	    ______|_____|_____
	          |     |
	 3     O  |     |  O
	          |     |


The computer has beaten you! You lose.
End the game!

```