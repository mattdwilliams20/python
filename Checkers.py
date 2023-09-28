# Checkers game

# Initialize the board
board = [[" ", "b", " ", "b", " ", "b", " ", "b"],
         ["b", " ", "b", " ", "b", " ", "b", " "],
         [" ", "b", " ", "b", " ", "b", " ", "b"],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " ", " "],
         ["r", " ", "r", " ", "r", " ", "r", " "],
         [" ", "r", " ", "r", " ", "r", " ", "r"],
         ["r", " ", "r", " ", "r", " ", "r", " "]]

# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Function to validate a move
def is_valid_move(board, start_row, start_col, end_row, end_col, player):
    # Check if the start and end positions are within the board boundaries
    if start_row < 0 or start_row >= 8 or start_col < 0 or start_col >= 8:
        return False
    if end_row < 0 or end_row >= 8 or end_col < 0 or end_col >= 8:
        return False

    # Check if the start position contains the player's piece
    if player == "r" and board[start_row][start_col] != "r" and board[start_row][start_col] != "R":
        return False
    if player == "b" and board[start_row][start_col] != "b" and board[start_row][start_col] != "B":
        return False

    # Check if the end position is empty
    if board[end_row][end_col] != " ":
        return False

    # Check if the move is diagonal
    if abs(start_row - end_row) != 1 or abs(start_col - end_col) != 1:
        return False

    # Check if the move is forward for regular pieces
    if player == "r" and end_row < start_row:
        return False
    if player == "b" and end_row > start_row:
        return False

    return True

# Function to make a move
def make_move(board, start_row, start_col, end_row, end_col, player):
    # Make the move
    board[end_row][end_col] = board[start_row][start_col]
    board[start_row][start_col] = " "

    # Check if the piece becomes a king
    if player == "r" and end_row == 0:
        board[end_row][end_col] = "R"
    if player == "b" and end_row == 7:
        board[end_row][end_col] = "B"

    return board

# Main game loop
current_player = "r"  # Red player starts first

while True:
    # Print the board
    print_board(board)
    print("Current turn: Player", current_player)

    # Get the move from the current player
    start_row = int(input("Enter the start row: "))
    start_col = int(input("Enter the start column: "))
    end_row = int(input("Enter the end row: "))
    end_col = int(input("Enter the end column: "))

    # Validate and make the move
    if is_valid_move(board, start_row, start_col, end_row, end_col, current_player):
        board = make_move(board, start_row, start_col, end_row, end_col, current_player)
        current_player = "b" if current_player == "r" else "r"
    else:
        print("Invalid move! Try again.")

    # Check for a win condition
    if "r" not in sum(board, []):  # No more red pieces
        print("Player b wins!")
        break
    if "b" not in sum(board, []):  # No more black pieces
        print("Player r wins!")
        break