import tkinter as tk
from board import Board

BOARD_SIZE = 100


def on_resize(event: tk.Event, board: Board):
    BOARD_SIZE = min(event.height, event.width)
    board.update_size(BOARD_SIZE)


def main():
    root = tk.Tk()
    board = Board(root, BOARD_SIZE, bg="black")
    root.geometry("600x300")

    root.bind("<Configure>", lambda e: on_resize(e, board=board))
    board.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
