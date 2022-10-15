from .game import Grid, Player


class SevenIA(Player):
    """IA which play all its turns on the seventh column."""

    def play(self, grid: Grid) -> int:
        for i in range(6):
            grid.grid[i][6]

