import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_player_move():
    while True:
        move = input("Enter your move (row[1-3] col[1-3]): ")
        try:
            row, col = map(int, move.split())
            if 1 <= row <= 3 and 1 <= col <= 3:
                return row - 1, col - 1
            else:
                print("Invalid move! Row and column must be between 1 and 3.")
        except ValueError:
            print("Invalid move! Please enter row and column numbers.")

def get_ai_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            return row, col

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        if players[current_player] == "X":
            row, col = get_player_move()
        else:
            print("AI's move:")
            row, col = get_ai_move(board)
            print(f"AI chose row {row + 1}, col {col + 1}")

        if board[row][col] == " ":
            board[row][col] = players[current_player]
            if check_winner(board, players[current_player]):
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = (current_player + 1) % 2
        else:
            print("That cell is already occupied!")

if __name__ == "__main__":
    main()
