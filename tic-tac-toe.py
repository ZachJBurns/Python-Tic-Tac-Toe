def play_a_turn(player, game_board, x_or_o, turn):
    display_board(game_board)
    print("It's {}'s turn!".format(player))

    (x, y) = input("Please enter your choice in the format a,b with a being the column and b being the row ").split(",")
    x = int(x)
    y = int(y)
    try:
        if game_board[y-1][x-1] == "-" and x_or_o:
            game_board[y-1][x-1] = "X"
            turn += 1
        elif game_board[y-1][x-1] == "-" and not x_or_o:
            game_board[y-1][x-1] = "O"
            turn += 1
        else:
            print("Someone has already played there! Skipping your turn. \n")
    except IndexError:
        print("Please enter numbers between 1 - 3. Skipping your turn")
    except ValueError:
        print("Please enter numbers between 1 - 3. Skipping your turn")

    return turn


def game_won(player, game_board):
    # Checks if any of the rows are equal

    for i in range(0, 3):
        if game_board[i][0] == game_board[i][1] == game_board[i][2] != '-':
            return True

    # Checks if any of the columns are equal.
    for i in range(0, 3):
        if game_board[0][i] == game_board[1][i] == game_board[2][i] != '-':
            return True

    # Checks if any of the diagonals are equal
    if game_board[0][0] == game_board[1][1] == game_board[2][2] != "-":
        return True
    elif game_board[2][0] == game_board[1][1] == game_board[0][2] != "-":
        return True


def display_board(game_board):
    print("   1  2  3")
    for choice, game in enumerate(game_board):
        print(choice + 1, end=" ")
        print('[%s]' % ', '.join(map(str, game)))



def main():
    turn = 0
    player1 = input("What is Player 1's name? ").strip()  # This player is X's
    player2 = input("What is Player 2's name? ").strip()  # This player is O's
    print()
    game_board = [['-', '-', '-'],
                  ['-', '-', '-'],
                  ['-', '-', '-']]

    while True:
        turn = play_a_turn(player1, game_board, True, turn)
        print(turn)
        if game_won(player1, game_board):
            display_board(game_board)
            print("Congratulations! {} has won against {}".format(player1, player2))
            return
        turn = play_a_turn(player2, game_board, False, turn)
        if game_won(player2, game_board):
            display_board(game_board)
            print("Congratulations! {} has won against {}".format(player2, player1))
            return
        if turn >= 9:
            print("All Positions Filled. Its a Tie!")
            return

main()
