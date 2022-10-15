import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from connect4.game import Grid, Player, Cell
#from .game import Grid, Player


class DumbIA(Player):
    """IA which play on the column of the first possible empty cell it finds."""

    def play(self, grid: Grid) -> int:
        val = 0
        for i in range(6):
            for j in range(7):
                cell = grid.grid[i][j]
                #il faut faire gaffe parce que c est le nom du parametre apres le variablde de la classe
                # regarder definition self
                if cell == Cell.EMPTY:
                    print(grid)
                    val = j

                    return val



#if i want to make the file exectutable

# i will have to write the follwoing code to make it work as soon as i launch in the interpruter if i am working on linux
# if __name__ == "__main__":
# instructions i want to execute