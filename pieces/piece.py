from abc import ABC, abstractmethod
import tkinter as tk
import os
from typing import List, Tuple
from PIL import Image, ImageTk


class Piece(ABC):
    def __init__(self, color, position, piece_type, square_size):
        self.color = color
        self.position = position
        self.piece_type = piece_type
        self.square_size = square_size
        self.image = None
        self.get_image_file()

    def get_image_file(self):
        base_dir = os.getcwd()
        path = os.path.join(base_dir, "assets", f"{self.color}-{self.piece_type}.png")
        pil_img = Image.open(path).convert("RGBA")

        size = int(self.square_size * 0.9)
        pil_img = pil_img.resize((size, size), Image.Resampling.LANCZOS)

        self.image = ImageTk.PhotoImage(pil_img)

    @abstractmethod
    def valid_moves(self, grid) -> List[Tuple[int, int]]:
        pass

    def draw(self, canvas: tk.Canvas):
        x = self.position[0] * self.square_size + self.square_size // 2
        y = self.position[1] * self.square_size + self.square_size // 2

        canvas.create_image(x, y, image=self.image)
