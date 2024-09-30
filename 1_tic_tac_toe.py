def print_board(board):
    """Prints the current state of the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Checks for a winner in the board."""
    # Check rows, columns and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def is_draw(board):
    """Checks if the game is a draw."""
    return all(cell != ' ' for row in board for cell in row)

def is_valid_move(board, row, col):
    """Checks if a move is valid."""
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def tic_tac_toe():
    """Main function to play Tic-Tac-Toe."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    for turn in range(9):
        print_board(board)
        print(f"Player {current_player}, enter your move (row and column): ")
        
        try:
            row, col = map(int, input().split())
        except ValueError:
            print("Invalid input. Please enter row and column as two numbers.")
            continue

        if not is_valid_move(board, row, col):
            print("Invalid move. Try again.")
            continue

        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return

        if is_draw(board):
            print_board(board)
            print("The game is a draw!")
            return

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

    print_board(board)
    print("The game is a draw!")

# Run the game
tic_tac_toe()


OUTPUT:1.WINNING
 |   |  
---------
  |   |  
---------
  |   |  
---------
Player X, enter your move (row and column): 
0 0
X |   |  
---------
  |   |  
---------
  |   |  
---------
Player O, enter your move (row and column): 
1 0
X |   |  
---------
O |   |  
---------
  |   |  
---------
Player X, enter your move (row and column): 
0 1
X | X |  
---------
O |   |  
---------
  |   |  
---------
Player O, enter your move (row and column): 
0 2
X | X | O
---------
O |   |  
---------
  |   |  
---------
Player X, enter your move (row and column): 
1 1
X | X | O
---------
O | X |  
---------
  |   |  
---------
Player O, enter your move (row and column): 
2 1
X | X | O
---------
O | X |  
---------
  | O |  
---------
Player X, enter your move (row and column): 
2 0
X | X | O
---------
O | X |  
---------
X | O |  
---------
Player O, enter your move (row and column): 
1 2 
X | X | O
---------
O | X | O
---------
X | O |  
---------
Player X, enter your move (row and column): 
2 2 
X | X | O
---------
O | X | O
---------
X | O | X
---------
Player X wins!

2.DRAW
 |   |  
---------
  |   |  
---------
  |   |  
---------
Player X, enter your move (row and column): 
0 0
X |   |  
---------
  |   |  
---------
  |   |  
---------
Player O, enter your move (row and column): 
1 1
X |   |  
---------
  | O |  
---------
  |   |  
---------
Player X, enter your move (row and column): 
2 2
X |   |  
---------
  | O |  
---------
  |   | X
---------
Player O, enter your move (row and column): 
0 1
X | O |  
---------
  | O |  
---------
  |   | X
---------
Player X, enter your move (row and column): 
2 1
X | O |  
---------
  | O |  
---------
  | X | X
---------
Player O, enter your move (row and column): 
2 0
X | O |  
---------
  | O |  
---------
O | X | X
---------
Player X, enter your move (row and column): 
1 0
X | O |  
---------
X | O |  
---------
O | X | X
---------
Player O, enter your move (row and column): 
1 2
X | O |  
---------
X | O | O
---------
O | X | X
---------
Player X, enter your move (row and column): 
1 2
Invalid move. Try again.
X | O |  
---------
X | O | O
---------
O | X | X
---------
The game is a draw!


3.INVALID INPUT

 |   |  
---------
  |   |  
---------
  |   |  
---------
Player X, enter your move (row and column): 
0 0
X |   |  
---------
  |   |  
---------
  |   |  
---------
Player O, enter your move (row and column): 
0 0
Invalid move. Try again.
X |   |  
---------
  |   |  
---------
  |   |  
---------
Player O, enter your move (row and column): 


