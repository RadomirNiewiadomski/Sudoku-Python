from sudoku_class import Board

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
gamer_answer = input("Press p to play the game: ")

if gamer_answer == 'p':
    print_board = Board()
    print_board.show_board()
