import tkinter as tk
from typing import List

class AbstractScene(tk.Frame):
    window: tk.Tk
    frames: List[tk.Frame]

    def __init__(self, window) -> None:
        super().__init__()
        self.window = window
        self.frames = []
    
    def build(self):
        raise NotImplementedError('`build` method not implemented')

    def show(self):
        for frame in self.frames:
            frame.pack()

    def hide(self):
        for frame in self.frames:
            frame.pack_forget()