board = [' ' for _ in range(9)]


def display_board():
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')

def check_winner(board, player):
    if (board[0] == board[1] == board[2] == player) or \
       (board[3] == board[4] == board[5] == player) or \
       (board[6] == board[7] == board[8] == player):
        return True
    if (board[0] == board[3] == board[6] == player) or \
       (board[1] == board[4] == board[7] == player) or \
       (board[2] == board[5] == board[8] == player):
        return True
    if (board[0] == board[4] == board[8] == player) or \
       (board[2] == board[4] == board[6] == player):
        return True
    return False

def play_game():
    display_board()
    player = 'X'
    game_over = False

    while not game_over:
        position = int(input("Enter a position (1-9): ")) - 1

        if board[position] == ' ':
            board[position] = player
            display_board()

            if check_winner(board, player):
                print("Congratulations! Player " + player + " wins!")
                game_over = True
            elif ' ' not in board:
                print("It's a tie!")
                game_over = True
            else:
                player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move. That position is already filled.")

play_game()