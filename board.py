import tkinter as tk
from typing import Optional, List
from pieces.piece import Piece
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.king import King
from pieces.bishop import Bishop
from pieces.knight import Knight


class Board(tk.Canvas):
    def __init__(self, parent, size, turn="white", **kwarg):
        super().__init__(parent, width=size, height=size, **kwarg)
        self.size = size
        self.ROWS_NUMBER = 8
        self.COLUMNS_NUMBER = 8
        self.square_size = self.size // self.ROWS_NUMBER
        self.grid: List[List[Optional[Piece]]] = [
            [None for _ in range(self.ROWS_NUMBER)] for _ in range(self.COLUMNS_NUMBER)
        ]
        self.selected_piece = None
        self.selected_pos = None
        self.turn = turn

        self.bind("<Button-1>", self.handle_click)
        self.setup_board()

    def update_size(self, size):
        self.configure(width=size, height=size)
        self.size = size
        self.square_size = size // self.ROWS_NUMBER

        for y in range(self.ROWS_NUMBER):
            for x in range(self.COLUMNS_NUMBER):
                piece = self.grid[y][x]
                if piece is not None:
                    piece.square_size = self.square_size
                    piece.get_image_file()

        self.render()

    def clear_board(self):
        self.delete("all")

    def setup_board(self):
        back_rank_types = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        piece_names = [
            "rook",
            "knight",
            "bishop",
            "queen",
            "king",
            "bishop",
            "knight",
            "rook",
        ]

        for x in range(8):
            self.grid[1][x] = Pawn("black", (x, 1), "pawn", self.square_size)
            self.grid[6][x] = Pawn("white", (x, 6), "pawn", self.square_size)

            PieceClass = back_rank_types[x]
            name = piece_names[x]

            self.grid[0][x] = PieceClass("black", (x, 0), name, self.square_size)

            self.grid[7][x] = PieceClass("white", (x, 7), name, self.square_size)

    def handle_click(self, event: tk.Event):
        x = event.x // self.square_size
        y = event.y // self.square_size

        clicked_piece = self.grid[y][x]
        if self.selected_piece is None:
            if clicked_piece is not None:
                if clicked_piece.color == self.turn:
                    print(f"You selected {self.grid[y][x].piece_type} ")
                    self.selected_piece = clicked_piece
                    self.selected_pos = (x, y)
                    self.render()
        else:
            # if self.selected_piece.color == self.turn:
            self.move_piece(self.selected_pos, (x, y))
            self.selected_piece = None
            self.selected_pos = None
            self.turn = "white" if self.turn != "white" else "black"
            self.render()

    def move_piece(self, start_pos, end_pos):
        # print(f"Moving piece from {start_pos}x{end_pos}")
        start_x, start_y = start_pos
        end_x, end_y = end_pos
        piece = self.grid[start_y][start_x]
        if piece:
            valid_moves = piece.valid_moves(self.grid)
            print(f"{valid_moves} valid_moves - {end_pos} clicked position ")

        if end_pos in piece.valid_moves(self.grid):
            # print("It is a valid move")
            self.grid[start_y][start_x] = None
            self.grid[end_y][end_x] = piece

            if piece:
                piece.position = (end_x, end_y)

    def draw_squares(self):
        print("Drawing Board!")
        self.clear_board()

        for y in range(self.ROWS_NUMBER):
            for x in range(self.COLUMNS_NUMBER):
                color = "#eeeed2" if (x + y) % 2 == 0 else "#769656"
                x_pos = self.square_size * x
                y_pos = self.square_size * y
                self.create_rectangle(
                    x_pos,
                    y_pos,
                    x_pos + self.square_size,
                    y_pos + self.square_size,
                    fill=color,
                    outline="",
                )

                if self.selected_pos == (x, y):
                    self.create_rectangle(
                        x * self.square_size,
                        y * self.square_size,
                        (x + 1) * self.square_size,
                        (y + 1) * self.square_size,
                        outline="yellow",
                        width=3,
                    )

    def grid_printer(self):
        for row in self.grid:
            print()

    def render(self):
        self.clear_board()
        self.draw_squares()

        for row in range(self.ROWS_NUMBER):
            for col in range(self.COLUMNS_NUMBER):
                piece = self.grid[row][col]
                if piece:
                    piece.draw(self)
