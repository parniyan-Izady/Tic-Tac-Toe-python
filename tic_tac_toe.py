import random

def main():
    # Main game loop that continues until the user chooses to exit
    while True:
        display_main_menu()
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                # Loop for single-player mode
                while True:
                    board = list(range(16))
                    lock_random_positions(board)
                    play_single_player(board)
                    display_game_menu()
                    option = int(input("Enter your choice (1-2): "))
                    if option == 1:
                        break  # Return to the main menu
                    elif option == 2:
                        continue  # Restart the game
                    else:
                        print("Invalid choice! Please enter 1 or 2.")
            elif choice == 2:
                # Loop for two-player mode
                while True:
                    board = list(range(16))
                    lock_random_positions(board)
                    play_two_players(board)
                    display_game_menu()
                    option = int(input("Enter your choice (1-2): "))
                    if option == 1:
                        break  # Return to the main menu
                    elif option == 2:
                        continue  # Restart the game
                    else:
                        print("Invalid choice! Please enter 1 or 2.")
            elif choice == 3:
                print("Exiting the game. Goodbye!")
                break  # Exit the game loop
            else:
                print("Invalid choice! Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def display_main_menu():
    # Display the main menu with options for the game
    print("""
+----------------------------------------+
|             TIC-TAC-TOE                |
+----------------------------------------+
| 1> Play against the computer           |
| 2> Play against a friend               |
| 3> Exit                                |
+----------------------------------------+
""")

def display_game_menu():
    # Display the game menu with options to return to the main menu or restart the game
    print("""
+----------------------------------------+
|             TIC-TAC-TOE                |
+----------------------------------------+
| 1> Return to main menu                 |
| 2> Restart this game                   |
+----------------------------------------+
""")

def play_single_player(board):
    # Single-player game logic
    turn_count = 0
    display_board(board)
    player_move(board, "Enter your number (1-16): ", 'x')
    while turn_count < 6:
        computer_move(board)
        turn_count = check_winner(board, "Computer wins!", 'o', turn_count)

        if turn_count < 6:
            display_board(board)
            player_move(board, "Enter your number (1-16): ", 'x')
            turn_count = check_winner(board, "You win!", 'x', turn_count)
            turn_count += 1

    display_board(board)
    if turn_count == 6:
        print("It's a tie")

def play_two_players(board):
    # Two-player game logic
    turn_count = 0
    display_board(board)
    player_move(board, "Player 1, enter your number (1-16): ", 'x')
    while turn_count < 6:
        display_board(board)
        player_move(board, "Player 2, enter your number (1-16): ", 'o')
        turn_count = check_winner(board, "Player 2 wins!", 'o', turn_count)

        if turn_count < 6:
            display_board(board)
            player_move(board, "Player 1, enter your number (1-16): ", 'x')
            turn_count = check_winner(board, "Player 1 wins!", 'x', turn_count)
            turn_count += 1

    display_board(board)
    if turn_count == 6:
        print("It's a tie!")

def lock_random_positions(board):
    # Randomly lock three positions on the board
    count = 0
    while count != 3:
        value = random.randint(0, 15)
        if board[value] != '#':
            board[value] = '#'
            count += 1

def computer_move(board):
    # Computer's move logic
    while True:
        value = random.randint(0, 15)
        if board[value] not in ['#', 'x', 'o']:
            board[value] = 'o'
            break

def check_winner(board, message, symbol, turn_count):
    # Check for a winner based on possible winning combinations
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

def display_board(board):
    # Display the current state of the board
    print("-----------------------------------------", end=" ")
    for y in range(16):
        if y % 4 == 0:
            print()
            print("|   ", end=" ")
        if board[y] not in ['#', 'o', 'x']:
   
