# Minesweeper Game

![Screenshot of Minesweeper game being played](https://github.com/AlliysonBonner/Minesweeper/blob/main/image.png?raw=true)

This is a console-based implementation of the classic Minesweeper game written in Python. The game is played on a two-dimensional grid, where some of the cells contain hidden bombs. The objective is to clear the board without detonating any bombs.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Gameplay](#gameplay)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation
To install the game, you'll need to have Python 3 installed on your machine. You can download Python from the official website: https://www.python.org/downloads/.

Once you have Python installed, download the `minesweeper.py` file from this repository and save it to your computer.

## Usage
To start the game, open a terminal window and navigate to the directory where you saved the `minesweeper.py` file. Then, run the following command:

`python minesweeper.py`

The game will start, and you'll be prompted to enter the size of the board and the number of bombs to be placed on the board.

## Gameplay
The game is played by entering coordinates of the cell you want to reveal or flag. To reveal a cell, enter its row and column numbers separated by a comma. To flag a cell, enter "F" followed by the row and column numbers separated by a comma.

For example, to reveal the cell in the third row and fifth column, enter `3,5`. To flag the same cell, enter `F3,5`.

If you reveal a cell containing a bomb, the game is over. If you reveal all the cells that don't contain bombs, you win!

## Features
- Customizable board size and number of bombs.
- Flagging of cells to help keep track of potential bomb locations.
- Recursive revealing of empty cells to speed up gameplay.
- Colorful console output for better visualization of the board.

## Contributing
Contributions are welcome! If you find a bug or have a suggestion for an improvement, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/alliysonbonner/Minesweeper/LICENSE.md) file for details.

## Author
* Name: Alliyson Bonner
* Github: https://github.com/alliysonbonner
* LinkedIn: https://www.linkedin.com/in/alliyson
* Email: alliyson.bonner@gmail.com
