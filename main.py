# Function to display the Tic Tac Toe board
def display_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

# Function to check if the game is a draw
def check_draw(board):
    return all(cell != " " for row in board for cell in row)

# Function to initialize the game board
def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Main game loop
def play_tic_tac_toe():
    while True:
        board = initialize_board()  # Initialize the game board
        current_player = "X"  # Player X starts

        while True:
            display_board(board)  # Display the current state of the board
            print(f"Player {current_player}'s turn.")

            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

            if board[row][col] == " ":
                board[row][col] = current_player  # Update the board with the player's move
            else:
                print("That position is already taken. Try again.")
                continue

            if check_win(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                break

            if check_draw(board):
                display_board(board)
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"  # Switch to the other player's turn

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    play_tic_tac_toe()  # Start the game when the script is run