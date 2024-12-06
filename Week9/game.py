import numpy as np

# Initialize the board as a 3x3 NumPy array filled with zeros (empty cells)
board = np.zeros((3, 3), dtype=int)

def print_board(board):
    # Print the board in a readable format
    for row in board:
        print(' | '.join([' ' if cell == 0 else 'X' if cell == 1 else 'O' for cell in row]))
        print('-' * 9)

print("Welcome to Tic Tac Toe!")
print_board(board)
def update_board(board, move, player):
    x, y = map(int, move.split(','))
    if board[x, y] == 0:
        board[x, y] = player
        return True
    else:
        print("Cell already taken! Try again.")
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
current_player = 1  # Player 1 starts
while True:
    print(f"Player {current_player}'s turn.")
    user_move = input("Enter your move as x,y coordinates (0-2): ")
    
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
