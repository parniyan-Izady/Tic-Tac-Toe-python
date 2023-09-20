import random


def main():
    f = 20
    while f != 3:
        menu()
        f = int(input())
        if f == 1:
            x = 10
            while x != 1:
                numbers = list(range(16))
                get_random_numbers_one(numbers)
                one_player_mode(numbers)
                print("-----------------------------------------")
                print("             Tic-Tac-Toe")
                print("-----------------------------------------")
                print("1> Return to first menu!")
                print("2> Restart this game!")
                print("Enter your number...")
                x = int(input())
                if x == 1:
                    break
                while x > 2:
                    print("Invalid number!")
                    x = int(input("Enter your number..."))
        if f == 2:
            x = 0
            while x != 1:
                numbers = list(range(16))
                two_players_mode(numbers)
                print("-----------------------------------------")
                print("             Tic-Tac-Toe")
                print("-----------------------------------------")
                print("1> Return to first menu!")
                print("2> Restart this game!")
                print("Enter your number...")
                x = int(input())
                if x == 1:
                    break
                while x > 2:
                    print("Invalid number!")
                    x = int(input("Enter your number..."))


def menu():
    print("-----------------------------------------")
    print("             Tic-Tac-Toe")
    print("-----------------------------------------")
    print("1> Play against a computer")
    print("2> Play against a friend")
    print("3> Exit")
    print("Enter your number please...")


def one_player_mode(numbers):
    p = 0
    show_string(numbers)
    read_number(numbers, "Enter your number please... ", 'x')
    while p < 6:
        get_random_numbers_two(numbers)
        p = winner(numbers, "Computer wins!", 'o', p)

        if p < 6:
            show_string(numbers)
            read_number(numbers, "Enter your number please... ", 'x')
            p = winner(numbers, "You win!", 'x', p)
            p += 1

    show_string(numbers)
    if p == 6:
        print("It's a tie")


def two_players_mode(numbers):
    p = 0
    show_string(numbers)
    read_number(numbers, "Player 1:", 'x')
    while p < 6:
        show_string(numbers)
        read_number(numbers, "player 2:", 'o')
        p = winner(numbers, "Player 2 wins!", 'o', p)

        if p < 6:
            show_string(numbers)
            read_number(numbers, "player 1:", 'x')
            p = winner(numbers, "Player 1 wins!", 'x', p)
            p += 1

    show_string(numbers)
    if p == 6:
        print("It's a tie!")


# Getting three random numbers for locking
def get_random_numbers_one(numbers):
    i = 0
    while i != 3:
        value = random.randint(0, 15)
        if numbers[value] != '#':
            numbers[value] = '#'
            i += 1


# Getting random numbers for computer
def get_random_numbers_two(numbers):
    while True:
        value = random.randint(0, 15)
        if numbers[value] != '#' and numbers[value] != 'x' and numbers[value] != 'o':
            numbers[value] = 'o'
            break


# Winner algoritem
def winner(numbers, prompt, chr, p):
    for i in [1, 3, 4, 5]:
        if i == 1:
            for z in [0, 1, 4, 5, 8, 9, 12, 13]:
                if numbers[z] == chr and numbers[z + i] == chr and numbers[z + 2 * i] == chr:
                    print(prompt)
                    p = 10
                    return p
        elif i == 3:
            for z in [2, 3, 6, 7]:
                if numbers[z] == chr and numbers[z + i] == chr and numbers[z + 2 * i] == chr:
                    print(prompt)
                    p = 10
                    return p
        elif i == 4:
            for z in [0, 1, 2, 3, 4, 5, 6, 7]:
                if numbers[z] == chr and numbers[z + i] == chr and numbers[z + 2 * i] == chr:
                    print(prompt)
                    p = 10
                    return p
        elif i == 5:
            for z in [0, 1, 4, 5]:
                if numbers[z] == chr and numbers[z + i] == chr and numbers[z + 2 * i] == chr:
                    print(prompt)
                    p = 10
                    return p
    return p


# Showing the appearance of the game
def show_string(numbers):
    print("-----------------------------------------", end=" ")
    for y in range(16):
        if y % 4 == 0:
            print()
            print("|   ", end=" ")
        if numbers[y] != '#' and numbers[y] != 'x' and numbers[y] != 'o':
            if y < 9:
                print(f"0{y + 1}   |   ", end=" ")
            else:
                print(f"{numbers[y]+1}   |   ", end=" ")
        else:
            print(f"{numbers[y]}    |   ", end=" ")
        if y % 4 == 3:
            print()
            print("-----------------------------------------", end=" ")
    print()


# Getting the numbers and checking its validity
def read_number(numbers, prompt, value):
    while True:
        print(prompt)
        index = int(input())
        print()
        index -= 1
        if 0 <= index <= 15 and numbers[index] != '#' and numbers[index] != 'x' and numbers[index] != 'o':
            numbers[index] = value
            break
        print("Invalid number!")


main()
