import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from connect4.game import Grid, Player, Cell


class CheaterB(Player):
    """This IA cheats and modify the grid to ensure player B wins."""

    #def play(self, grid: Grid) -> int:
       # """win horizontal"""
    """ i = 0
        j = 0
        for cell in range(grid.lines):
            for cell2 in range(grid.columns):
                var = grid.grid[cell][cell2]
                if var == Cell.A:
                    i += 1
                    for i in range(5):
                        print(Grid)
                        grid.place(i, Cell.B)
                        print(Grid)
                        return i
                
        print(grid)
        if i == j:
            return i"""

    def play(self, grid: Grid) -> int:
        """win horizontal"""
        for i in range(4):
            grid.place(i, Cell.B)
        return 0

    print(Grid)