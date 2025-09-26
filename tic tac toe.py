# Simple 2-player Tic-Tac-Toe

# Create empty board
board = [" " for _ in range(9)]

# Function to display the board
def display_board():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

# Function to check if someone has won
def check_winner(player):
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Main game loop
turns = 0
current_player = "X"

while turns < 9:
    display_board()
    move = input(f"Player {current_player}, choose your position (1-9): ")
    
    if not move.isdigit():
        print("Please enter a number between 1-9.")
        continue
    
    move = int(move) - 1
    if move < 0 or move > 8:
        print("Invalid position. Choose 1-9.")
        continue
    
    if board[move] != " ":
        print("Position already taken! Try again.")
        continue
    
    board[move] = current_player
    
    if check_winner(current_player):
        display_board()
        print(f"Player {current_player} wins! 🎉")
        break
    
    # Switch player
    current_player = "O" if current_player == "X" else "X"
    turns += 1

if turns == 9 and not check_winner("X") and not check_winner("O"):
    display_board()
    print("It's a draw! 🤝")
