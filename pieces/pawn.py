from .piece import Piece
from typing import List, Tuple


class Pawn(Piece):
    def __init__(self, color, position: List[Tuple[int, int]], piece_type, square_size):
        super().__init__(color, position, piece_type, square_size)

    def valid_moves(self, grid):
        # here I'll validated what are the possible movements
        x, y = self.position
        if self.color == "white":
            return [(x, y - 1)]

        return [(x, y + 1)]
