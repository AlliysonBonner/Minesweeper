import random
import re


class Board:
    """
    The Board class models a Minesweeper game board.

    Attributes:
        dim_size (int): The size of the board.
        num_bombs (int): The number of bombs on the board.
        board (list): A 2D list representing the board.
        dug (set): A set of tuples representing the dug cells.
        flags (set): A set of tuples representing the flagged cells.

    Methods:
        place_bombs(): Randomly plants bombs on the board.
        assign_values_to_board(): Assigns numerical values to the board based on neighboring bombs.
        get_num_neighboring_bombs(row, col): Returns the number of neighboring bombs.
        dig(row, col): Recursively digs cells until a bomb is found or cells adjacent to bombs are reached.
        flag(row, col): Adds or removes a flag from the specified cell.
        __str__(): Returns a string representation of the board.
    """
    def __init__(self, dim_size, num_bombs):
        """Initializes the Board object.

        Args:
            dim_size (int): The size of the board.
            num_bombs (int): The number of bombs on the board.
        """
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # Create an empty board
        self.board = [[' ' for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # Place bombs on the board
        self.place_bombs()

        # Keep track of cells that have been dug
        self.dug = set()

        # Keep track of cells that have flags
        self.flags = set()

    def place_bombs(self):
        """
        Randomly plants bombs on the board.

        Returns:
            None
        """
        # Initialize the number of bombs that have been planted
        bombs_planted = 0

        # Keep randomly planting bombs until the specified number of bombs is reached
        while bombs_planted < self.num_bombs:
            # Generate random coordinates
            row, col = random.randint(0, self.dim_size - 1), random.randint(0, self.dim_size - 1)

            # If the current cell does not have a bomb already
            if self.board[row][col] == ' ':
                # Place a bomb in the current cell
                self.board[row][col], bombs_planted = '*', bombs_planted + 1


    def assign_values_to_board(self):
        """
        Assigns numerical values to the board based on neighboring bombs.
        """
        for r in range(self.dim_size):  # Loop over rows
            for c in range(self.dim_size):  # Loop over columns
                if self.board[r][c] == '*':  # If the current position contains a bomb
                    continue  # Skip assigning a value to this position
                # Assign the value of number of bombs in the neighboring cells to the current position
                self.board[r][c] = str(self.get_num_neighboring_bombs(r, c))

    def get_num_neighboring_bombs(self, row, col):
        """
        Returns the number of neighboring bombs.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            int: The number of neighboring bombs.
        """
        count = 0
        # Loop through the neighboring cells
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                # If the neighboring cell has a bomb, increment the count
                count += self.board[r][c] == '*'
        return count

    def dig(self, row, col):
        """
        Recursively digs cells until a bomb is found or cells adjacent to bombs are reached.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            bool: True if the cell is safe, False if a bomb is found.
        """
        # Check if the cell has a flag
        if (row, col) in self.flags:
            # Ask the user if they really want to dig in a spot marked with a flag
            confirm = input("This spot is marked with a flag. Are you sure you want to dig here? (y/n): ")
            if confirm.lower() == 'n':
                return True
            elif confirm.lower() == 'y':
                # Toggle the flag and dig in the cell
                self.flag(row, col)
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
                return True

        # If the cell contains a bomb, mark it with an asterisk and return False
        if self.board[row][col] == '*':
            self.dug.add((row, col))
            self.board[row][col] = '*'  # Mark the cell with an asterisk
            return False

        # Mark the cell as dug
        self.dug.add((row, col))

        # If the cell is adjacent to 0 bombs, dig its neighbors recursively
        if self.board[row][col] == '0':
            for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
                for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                    if (r, c) not in self.dug:
                        self.dig(r, c)

        return True



    def flag(self, row, col):
        """
        Toggles the flag in the specified cell.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
        """
        if (row, col) not in self.dug:
            if (row, col) not in self.flags:
                # Add a flag to the cell
                self.flags.add((row, col))
                # If the cell doesn't contain a bomb, mark it with an 'F'
                if self.board[row][col] != '*':
                    self.board[row][col] = 'F'
            else:
                # Remove the flag from the cell
                self.flags.remove((row, col))
                # If the cell doesn't contain a bomb, mark it with a blank space
                if self.board[row][col] != '*':
                    self.board[row][col] = ' '



    def __str__(self):
        """
        Returns a string representation of the board.

        Returns:
            str: A string representation of the board.
        """
        # Create the header row with the column indices
        header = '   '
        for i in range(self.dim_size):
            header += f' {i}'

        # Start the string with the header
        s = f'{header}\n'

        # Add the rows of the board
        for i in range(self.dim_size):
            row = f'{i} |'  # Start the row with the row index
            for j in range(self.dim_size):
                if (i, j) in self.dug:
                    if self.board[i][j] == '*':
                        row += ' *'
                    else:
                        row += f' {self.board[i][j]}'
                elif (i, j) in self.flags:
                    row += ' F'  # If the cell has a flag, add the flag symbol
                else:
                    row += ' -'  # Otherwise, add the covered cell symbol
            s += f'{row}\n'

        return s


def play(dim_size=10, num_bombs=10):
    """
    Plays a game of Minesweeper.

    Args:
        dim_size (int): The size of the board.
        num_bombs (int): The number of bombs on the board.
    """
    board = Board(dim_size, num_bombs)
    board.assign_values_to_board()  # Populate board with numerical values
    safe = True

    while len(board.dug) < board.dim_size ** 2 - board.num_bombs:
        # print board
        print(board)
        # get user input
        user_input = input(
            "Enter the coordinates for where you'd like to dig, or enter 'F' before the coordinates to add a flag: "
        ).lower().replace(" ", "")
        # handle flag input
        if user_input.startswith("f"):
            user_input = user_input[1:]
            try:
                row, col = map(int, user_input.split(","))
                if not 0 <= row < board.dim_size or not 0 <= col < board.dim_size:
                    raise ValueError
            except ValueError:
                print("Invalid flag location. Please try again.")
                continue
            if (row, col) in board.dug:
                print("Cannot add flag to location that has already been dug.")
                continue
            board.flag(row, col)
        # handle dig input
        else:
            try:
                row, col = map(int, user_input.split(","))
                if not 0 <= row < board.dim_size or not 0 <= col < board.dim_size:
                    raise ValueError
            except ValueError:
                print("Invalid location. Please enter the row and column separated by a comma (e.g. 3,4).")
                continue
            if (row, col) in board.dug:
                print("Location has already been dug. Please try again.")
                continue
            safe = board.dig(row, col)
            if not safe:
                break

    # print final board
    print(board)

    # check game outcome
    if safe:
        print("Congratulations! You won!")
    else:
        print("Sorry, you hit a bomb. Game over!")

if __name__ == '__main__':
    play()
