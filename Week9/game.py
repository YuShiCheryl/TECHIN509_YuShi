import numpy as np

# Initialize the board as a 3x3 NumPy array filled with zeros (empty cells)
board = np.zeros((3, 3), dtype=int)

def print_board(board):
    # Print the board in a readable format
    for row in board:
        print(' | '.join([' ' if cell == 0 else 'X' if cell == 1 else 'O' for cell in row]))
        print('-' * 9)

def update_board(board, move, player):
    try:
        # Ensure input is exactly 2 digits
        if len(move) != 2 or not move.isdigit():
            raise ValueError("Invalid input length.")
        
        # Convert input into row and column, subtracting 1 for 0-based indexing
        x, y = int(move[0]) - 1, int(move[1]) - 1
        
        # Check if the move is valid
        if x not in range(3) or y not in range(3):
            raise ValueError("Input out of range.")
        if board[x, y] == 0:
            board[x, y] = player
            return True
        else:
            print("Cell already taken! Try again.")
            return False
    except ValueError:
        print("Invalid input! Enter your move as two digits (row and column, 1-3). Example: 12 for row 1, column 2.")
        return False

def check_winner(board):
    for i in range(3):
        # Check rows and columns
        if all(board[i, :] == 1) or all(board[:, i] == 1):
            return 1
        if all(board[i, :] == 2) or all(board[:, i] == 2):
            return 2
    
    # Check diagonals
    if all(np.diag(board) == 1) or all(np.diag(np.fliplr(board)) == 1):
        return 1
    if all(np.diag(board) == 2) or all(np.diag(np.fliplr(board)) == 2):
        return 2
    
    # Check for tie
    if not (board == 0).any():
        return 0
    
    return -1

# Game loop
print("Welcome to Tic Tac Toe!")
print_board(board)

current_player = 1  # Player 1 starts
while True:
    print(f"Player {current_player}'s turn.")
    user_move = input("Enter your move as two digits (row and column, 1-3). Example: 12: ")
    
    if update_board(board, user_move, current_player):
        print_board(board)
        winner = check_winner(board)
        
        if winner == 1:
            print("Player 1 (X) wins!")
            break
        elif winner == 2:
            print("Player 2 (O) wins!")
            break
        elif winner == 0:
            print("It's a tie!")
            break
        
        # Switch players
        current_player = 2 if current_player == 1 else 1
