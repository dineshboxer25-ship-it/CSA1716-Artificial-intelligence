
board = [' '] * 9

def display():
    for i in range(0, 9, 3):
        print(" ", board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("---------")

def check_winner():
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    return None

moves = [6, 3, 5, 9, 1, 2, 8, 4, 7]

for turn, cell in enumerate(moves):
    player = 'X' if turn % 2 == 0 else 'O'

    board[cell - 1] = player
    print(f"\nPlayer {player} plays cell {cell}")
    display()

    if check_winner():
        print(f"Player {player} wins!")
        break
else:
    print("Game Draw!")

