from .piece import Piece


class Knight(Piece):
    def __init__(self, color, position, piece_type, square_size):
        super().__init__(color, position, piece_type, square_size)

    def valid_moves(self, grid):
        moves = []
        current_col, current_row = self.position
        directions = [
            (1, 2),
            (-1, 2),
            (2, 1),
            (-2, 1),
            (-1, -2),
            (-2, -1),
            (1, -2),
            (2, -1),
        ]

        for dh, dv in directions:
            new_col = current_col + dh
            new_row = current_row + dv

            if 0 <= new_col < 8 and 0 <= new_row < 8:
                target = grid[new_row][new_col]
                if target is None:
                    moves.append((new_col, new_row))
                else:
                    if target.color != self.color:
                        moves.append((new_col, new_row))
                    continue

            else:
                continue
        return moves
