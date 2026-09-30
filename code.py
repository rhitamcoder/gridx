winning_combos = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]

def create_board():
    board = [str(i) for i in range(1, 10)]
    return board

def display_board(board):
    row_1 = " | ".join(board[0:3])
    print(row_1)
    print("----------")
    row_2 = " | ".join(board[3:6])
    print(row_2)
    print("----------")
    row_3 = " | ".join(board[6:9])
    print(row_3)

def get_player_move(board):
    while True:
        usr_choice = input("Enter a Number (1-9): ")
        if usr_choice in board:
            return usr_choice
        else:
            print("It's an invalid entry. Try again")

def update_board(board, choice, current_player):
    index = int(choice) - 1
    board[index] = current_player

def check_winner(board):
    for combo in winning_combos:
        a, b, c = combo
        if board[a] == board[b] == board [c]:
            return board[a]

def is_board_full(board):
    for cell in board:
        if cell != "X" and cell != "O":
            return False
    return True

def play_game():
    board = create_board()
    current_player = "X"

    while True:
        display_board(board)
        choice = get_player_move(board)
        update_board(board, choice, current_player)

        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"{winner} wins!")
            break

        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

print("Welcome to Tic-Tac-Toe! Let's Enjoy.")

while True:
    play_game()

    again = input("Play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing! Goodbay, Mate.")
        break
