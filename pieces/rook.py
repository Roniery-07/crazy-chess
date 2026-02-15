from .piece import Piece
from typing import List, Tuple


class Rook(Piece):
    def __init__(self, color, position: List[Tuple[int, int]], piece_type, square_size):
        super().__init__(color, position, piece_type, square_size)

    def valid_moves(self, grid):

        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        current_col, current_row = self.position

        for dh, dv in directions:
            for i in range(1, 8):
                new_col = current_col + (i * dh)
                new_row = current_row + (i * dv)

                if 0 <= new_col < 8 and 0 <= new_row < 8:
                    print("calculating")
                    target = grid[new_row][new_col]

                    if target is None:
                        print("appending")
                        moves.append((new_col, new_row))
                    else:
                        if target.color != self.color:
                            print("appending")
                            moves.append((new_col, new_row))
                        break
                else:
                    break
        return moves
