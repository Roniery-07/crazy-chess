from .piece import Piece


class Queen(Piece):
    def __init__(self, color, position, piece_type, square_size):
        super().__init__(color, position, piece_type, square_size)

    def valid_moves(self, grid):
        moves = []
        current_col, current_row = self.position
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (-1, 1),
            (-1, -1),
            (1, -1),
        ]

        for dh, dv in directions:
            for i in range(1, 8):
                new_col = current_col + (i * dh)
                new_row = current_row + (i * dv)

                if 0 <= new_col < 8 and 0 <= new_row < 8:
                    target = grid[new_row][new_col]
                    if target is None:
                        moves.append((new_col, new_row))
                    else:
                        # if I find a piece I will stop the loop in that direction, however
                        # the only thing I must verify is the piece color, if it is an aly or an enemy
                        if target.color != self.color:
                            moves.append((new_col, new_row))
                        break
                else:
                    break

        return moves
