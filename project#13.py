def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Checks if the given player has won."""
    win_conditions = [
        # Check rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Check columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Check diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player] * 3 in win_conditions

def is_full(board):
    """Checks if the board is full."""
    return all(cell != " " for row in board for cell in row)

def play_game():
    """Main function to play the Tic-Tac-Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player_index = 0

    while True:
        print_board(board)
        print(f"Player {players[current_player_index]}'s turn")

        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue
            board[row][col] = players[current_player_index]

            if check_winner(board, players[current_player_index]):
                print_board(board)
                print(f"Player {players[current_player_index]} wins!")
                break
            if is_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player_index = (current_player_index + 1) % 2

        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")

if __name__ == "__main__":
    play_game()