from .game import Grid, Player


class ConsolePlayer(Player):
    """Allow a human to see the grid in its shell, and input a column from the
    keyboard."""

    def play(self, grid: Grid) -> int:

        for i in range(6):
            print(grid.grid)
            print("You can play in the columns from 1 to 7")
            j = input("Please enter the column where you want to play: ")
            grid.grid[i][j]
