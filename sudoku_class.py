class Board():
    def __init__(self):
        self.board = [["4", "*", "3", "*", "*", "6", "*", "7", "*"],
                      ["1", "*", "*", "5", "*", "7", "6", "*", "4"],
                      ["7", "6", "5", "1", "*", "4", "3", "9", "2"],
                      ["*", "2", "4", "3", "7", "9", "*", "5", "*"],
                      ["*", "*", "9", "6", "4", "1", "7", "*", "*"],
                      ["3", "*", "*", "8", "*", "2", "*", "6", "9"],
                      ["5", "1", "*", "2", "9", "*", "*", "4", "*"],
                      ["2", "3", "*", "4", "*", "*", "*", "1", "7"],
                      ["9", "*", "6", "7", "1", "8", "2", "*", "5"]]

        self.board_correct = [["4", "8", "3", "9", "2", "6", "5", "7", "1"],
                              ["1", "9", "2", "5", "3", "7", "6", "8", "4"],
                              ["7", "6", "5", "1", "8", "4", "3", "9", "2"],
                              ["6", "2", "4", "3", "7", "9", "1", "5", "8"],
                              ["8", "5", "9", "6", "4", "1", "7", "2", "3"],
                              ["3", "7", "1", "8", "5", "2", "4", "6", "9"],
                              ["5", "1", "7", "2", "9", "3", "8", "4", "6"],
                              ["2", "3", "8", "4", "6", "5", "9", "1", "7"],
                              ["9", "4", "6", "7", "1", "8", "2", "3", "5"]]

    def show_board(self):
        for row in self.board:
            for element in row:
                print(element, end=" ")
            print()     # to add a new line after last element in each row

    def insert_element(self, row, column, guess):
        if self.board[row-1][column-1] == "*":  # -1 because list index starts from 0
            self.board[row-1][column-1] = str(guess)
        else:
            print(
                "Incorrect position! Choose an empty space from the board (marked as *). Try again")

    def is_board_complete(self):
        for row in self.board:
            for element in row:
                if element == "*":
                    return False
        return True

    def is_board_correct(self):
        for row in range(0, 9):
            for element in range(0, 9):
                if self.board[row][element] != self.board_correct[row][element]:
                    return False
        return True
