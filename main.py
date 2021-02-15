p = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # Coordinate positions on the board
start = True  # Sets the main game loop
tie = 1
print("Welcome to tic tac toe!")


def board():  # Creates an a board made of Arrays and strings
    print("    [1] [2] [3]")
    print("               ")
    print(f"[1]  {p[0]} | {p[1]} | {p[2]} ")
    print("    -----------")
    print(f"[2]  {p[3]} | {p[4]} | {p[5]} ")
    print("    -----------")
    print(f"[3]  {p[6]} | {p[7]} | {p[8]} ")
    print("               ")
    print("Please enter the coordinates")


def move1():  # Make the move for the player 1
    play = False

    while not play:
        x = input("Line ")
        y = input("Column ")

        if x == "1" and y == "1":
            if p[0] == " ":
                p[0] = "X"
                play = True
            else:
                print("This position has already been occupied")
        elif x == "1" and y == "2":
            if p[1] == " ":
                p[1] = "X"
                play = True
            else:
                print("This position has already been occupied")
        elif x == "1" and y == "3":
            if p[2] == " ":
                p[2] = "X"
                play = True
            else:
                print("This position has already been occupied")
        elif x == "2" and y == "1":
            if p[3] == " ":
                p[3] = "X"
                play = True
            else:
                print("This position has already been occupied")
        elif x == "2" and y == "2":
            if p[4] == " ":
                p[4] = "X"
                play = True
            else:
                print("This position has already been occupied")
        elif x == "2" and y == "3":
            if p[5] == " ":
                p[5] = "X"
                play = True
            else:
                print("This position has already been occupied")
        elif x == "3" and y == "1":
            if p[6] == " ":
                p[6] = "X"
                play = True
            else:
                print("This position has already been occupied")
        elif x == "3" and y == "2":
            if p[7] == " ":
                p[7] = "X"
                play = True
            else:
                print("This position has already been occupied")
        elif x == "3" and y == "3":
            if p[8] == " ":
                p[8] = "X"
                play = True
            else:
                print("This position has already been occupied")
        else:
            print("Wrong coordinates, try again")


def move2():  # Make the move for the player 1
    play = False

    while not play:
        x = input("Line ")
        y = input("Column ")

        if x == "1" and y == "1":
            if p[0] == " ":
                p[0] = "O"
                play = True
            else:
                print("This position has already been occupied")
        elif x == "1" and y == "2":
            if p[1] == " ":
                p[1] = "O"
                play = True
            else:
                print("This position has already been occupied")
        elif x == "1" and y == "3":
            if p[2] == " ":
                p[2] = "O"
                play = True
            else:
                print("This position has already been occupied")
        elif x == "2" and y == "1":
            if p[3] == " ":
                p[3] = "O"
                play = True
            else:
                print("This position has already been occupied")
        elif x == "2" and y == "2":
            if p[4] == " ":
                p[4] = "O"
                play = True
            else:
                print("This position has already been occupied")
        elif x == "2" and y == "3":
            if p[5] == " ":
                p[5] = "O"
                play = True
            else:
                print("This position has already been occupied")
        elif x == "3" and y == "1":
            if p[6] == " ":
                p[6] = "O"
                play = True
            else:
                print("This position has already been occupied")
        elif x == "3" and y == "2":
            if p[7] == " ":
                p[7] = "O"
                play = True
            else:
                print("This position has already been occupied")
        elif x == "3" and y == "3":
            if p[8] == " ":
                p[8] = "O"
                play = True
            else:
                print("This position has already been occupied")
        else:
            print("Wrong coordinates, try again")


def check():  # Check if has a winner
    global start
    global tie
    if (p[0] == "X" and p[1] == "X" and p[2] == "X") or (p[0] == "X" and p[3] == "X" and p[6] == "X"):
        print("Player 1 is the winner!")
        start = False
    elif (p[3] == "X" and p[4] == "X" and p[5] == "X") or (p[1] == "X" and p[4] == "X" and p[7] == "X"):
        print("Player 1 is the winner!")
        start = False
    elif (p[6] == "X" and p[7] == "X" and p[8] == "X") or (p[2] == "X" and p[5] == "X" and p[8] == "X"):
        print("Player 1 is the winner!")
        start = False
    elif (p[0] == "X" and p[4] == "X" and p[8] == "X") or (p[2] == "X" and p[4] == "X" and p[6] == "X"):
        print("Player 1 is the winner!")
        start = False
    elif (p[0] == "O" and p[1] == "O" and p[2] == "O") or (p[0] == "O" and p[3] == "O" and p[6] == "O"):
        print("Player 2 is the winner!")
        start = False
    elif (p[3] == "O" and p[4] == "O" and p[5] == "O") or (p[1] == "O" and p[4] == "O" and p[7] == "O"):
        print("Player 2 is the winner!")
        start = False
    elif (p[6] == "O" and p[7] == "O" and p[8] == "O") or (p[2] == "O" and p[5] == "O" and p[8] == "O"):
        print("Player 2 is the winner!")
        start = False
    elif (p[0] == "O" and p[4] == "O" and p[8] == "O") or (p[2] == "O" and p[4] == "O" and p[6] == "O"):
        print("Player 2 is the winner!")
        start = False
    else:
        tie = tie + 1

    if tie > 9:
        print("It's a tie")
        start = False


while start:  # main game loop
    board()
    move1()
    board()
    check()
    if start:
        move2()
        board()
        check()
