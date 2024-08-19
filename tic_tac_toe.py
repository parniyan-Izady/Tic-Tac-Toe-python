import random

def main():
    choice = 20
    while choice != 3:
        display_main_menu()
        choice = int(input())
        if choice == 1:
            option = 10
            while option != 1:
                board = list(range(16))
                lock_random_positions(board)
                play_single_player(board)
                print("-----------------------------------------")
                print("             Tic-Tac-Toe")
                print("-----------------------------------------")
                print("1> Return to main menu")
                print("2> Restart this game")
                print("Enter your choice...")
                option = int(input())
                if option == 1:
                    break
                while option > 2:
                    print("Invalid choice!")
                    option = int(input("Enter your choice..."))
        elif choice == 2:
            option = 0
            while option != 1:
                board = list(range(16))
                lock_random_positions(board)
                play_two_players(board)
                print("-----------------------------------------")
                print("             Tic-Tac-Toe")
                print("-----------------------------------------")
                print("1> Return to main menu")
                print("2> Restart this game")
                print("Enter your choice...")
                option = int(input())
                if option == 1:
                    break
                while option > 2:
                    print("Invalid choice!")
                    option = int(input("Enter your choice..."))


def display_main_menu():
    print("-----------------------------------------")
    print("             Tic-Tac-Toe")
    print("-----------------------------------------")
    print("1> Play against the computer")
    print("2> Play against a friend")
    print("3> Exit")
    print("Enter your choice...")


def play_single_player(board):
    turn_count = 0
    display_board(board)
    player_move(board, "Enter your number please... ", 'x')
    while turn_count < 6:
        computer_move(board)
        turn_count = check_winner(board, "Computer wins!", 'o', turn_count)

        if turn_count < 6:
            display_board(board)
            player_move(board, "Enter your number please... ", 'x')
            turn_count = check_winner(board, "You win!", 'x', turn_count)
            turn_count += 1

    display_board(board)
    if turn_count == 6:
        print("It's a tie")


def play_two_players(board):
    turn_count = 0
    display_board(board)
    player_move(board, "Player 1:", 'x')
    while turn_count < 6:
        display_board(board)
        player_move(board, "Player 2:", 'o')
        turn_count = check_winner(board, "Player 2 wins!", 'o', turn_count)

        if turn_count < 6:
            display_board(board)
            player_move(board, "Player 1:", 'x')
            turn_count = check_winner(board, "Player 1 wins!", 'x', turn_count)
            turn_count += 1

    display_board(board)
    if turn_count == 6:
        print("It's a tie!")


# Locking three random positions
def lock_random_positions(board):
    count = 0
    while count != 3:
        value = random.randint(0, 15)
        if board[value] != '#':
            board[value] = '#'
            count += 1


# Computer's move
def computer_move(board):
    while True:
        value = random.randint(0, 15)
        if board[value] not in ['#', 'x', 'o']:
            board[value] = 'o'
            break


# Check for a winner
def check_winner(board, message, symbol, turn_count):
    for step in [1, 3, 4, 5]:
        if step == 1:
            for index in [0, 1, 4, 5, 8, 9, 12, 13]:
                if board[index] == symbol and board[index + step] == symbol and board[index + 2 * step] == symbol:
                    print(message)
                    return 10
        elif step == 3:
            for index in [2, 3, 6, 7]:
                if board[index] == symbol and board[index + step] == symbol and board[index + 2 * step] == symbol:
                    print(message)
                    return 10
        elif step == 4:
            for index in [0, 1, 2, 3, 4, 5, 6, 7]:
                if board[index] == symbol and board[index + step] == symbol and board[index + 2 * step] == symbol:
                    print(message)
                    return 10
        elif step == 5:
            for index in [0, 1, 4, 5]:
                if board[index] == symbol and board[index + step] == symbol and board[index + 2 * step] == symbol:
                    print(message)
                    return 10
    return turn_count


# Display the game board
def display_board(board):
    print("-----------------------------------------", end=" ")
    for y in range(16):
        if y % 4 == 0:
            print()
            print("|   ", end=" ")
        if board[y] not in ['#', 'o', 'x']:
            if y < 9:
                print(f"0{y + 1}   |   ", end=" ")
            else:
                print(f"{y + 1}   |   ", end=" ")
        else:
            print(f"{board[y]}    |   ", end=" ")
        if y % 4 == 3:
            print()
            print("-----------------------------------------", end=" ")
    print()


# Handle player's move
def player_move(board, prompt, symbol):
    while True:
        print(prompt)
        index = int(input())
        print()
        index -= 1
        if 0 <= index <= 15 and board[index] not in ['#', 'x', 'o']:
            board[index] = symbol
            break
        print("Invalid number!")


main()
