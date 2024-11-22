# manages the grid that checks for wins or a completed board
class Board:
    def __init__(self):
        # Initializes a 3x3 grid with empty spaces
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def board_outline(self):
        # Loops through each row of the board
        for i in range(3):  # Loop through each row
            print(" | ".join(self.grid[i]))  # Join the elements with " | " separator
            if i < 2:  # If it's not the last row, print the separator line
                print("-" * 10)  # Print a separator line (8 dashes)

    #updates the board with X or O, if the cell is empty.
    def update(self, row, col, symbol):
        #makes sures the cell is empty
        if self.grid[row-1][col-1] == " ":
            self.grid[row-1][col-1] = symbol #adds the X or O
            return True #the move is successful
        return False #shows that cell is not empty

    #check to see if the player won
    def check_win(self, symbol):
        #checks the rows, columns and diagonals
        for i in range(3):
            # self.grid[i][j] checks row
            # self.grid[j][i] checks columns
            if all(self.grid[i][j] == symbol for j in range(3)) or all(
                    self.grid[j][i] == symbol for j in range(3)):
                return True
            #self.grid[i][i] checks top-left to bottom-right diagonal
            #self.grid[i][2-1] checks top-right to bottom-left diagonal
            if all(self.grid[i][i] == symbol for i in range(3) or all(
                    self.grid[i][2-1] == symbol for i in range(3))):
                return True
            return False

    #check to see if the board is complete
    def is_complete(self):
        return all(
            self.grid[i][j] != " " for i in range(3) for j in range(3))
