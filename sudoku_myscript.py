from sudoku_class import Board, Board_Medium, Board_Hard

print("\n~~~~~~~~~~Welcome to Sudoku!~~~~~~~~~~")
print("At first read the main rules to play the game: ")
print("Size of the sudoku board is 9x9.")
print("Each row has all numbers from 1 to 9.")
print("Each column has all numbers from 1 to 9.")
print("Each 3x3 grid box has all numbers from 1 to 9.")
print("To insert number: select a row, then a column.")
print("Choose your guess from 1 to 9.")
print("Have fun!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
gamer_answer = input(
    "Select difficulty level (1 - easy, 2 - medium, 3 - hard): ")

if gamer_answer == '1':
    board = Board()
    board.show_board()
elif gamer_answer == '2':
    board = Board_Medium()
    board.show_board()
elif gamer_answer == '3':
    board = Board_Hard()
    board.show_board()

while board.is_board_complete() == False:
    try:
        row = int(input("Enter a row (1-9): "))
    except ValueError:
        print("Error - row must be a number from 1 to 9!")
    try:
        column = int(input("Enter a column (1-9): "))
    except ValueError:
        print("Error - column must be a number from 1 to 9!")
    try:
        guess = int(input("Enter your guess (1-9): "))
        if row in range(1, 10) and column in range(1, 10) and guess in range(1, 10):
            board.insert_element(row, column, guess)
        else:
            print("Error - row, column and guess have to be number from 1 to 9!")
    except ValueError:
        print("Error - guess must be a number from 1 to 9!")
    board.show_board()
    gamer_answer = input(
        "Press any key to continue or press q to quit the game.")
    if gamer_answer == 'q':
        print("You've quit the game. Goodbye")
        break

if board.is_board_complete == True:
    if board.is_board_correct() == True:
        print("Congratulation, correct answers! You've successfully completed sudoku!")
    else:
        print("Sorry, you've failed. Your sudoku is not correct, please try again.")
