import tkinter as tk
from tkinter import *

from typing import List

from .scene import AbstractScene
from ..elements.popup import show_popup
from solver.graph import draw_graph

class MatrixScene(AbstractScene):
    solve_button: tk.Button
    matrix_entries: List[List[tk.Entry]]
    width: int
    height: int

    def __init__(self, window, width, height) -> None:
        super().__init__(window)
        self.width = width
        self.height = height

    # def button_callback(self):
    #     width = int(self.width_entry.get())
    #     height = int(self.height_entry.get())
    #     print(width, height)

    def button_callback(self):
        if not self.validate_matrix():
            return
        # Вывести значения матрицы
        matrix_values = [[float(entry.get()) for entry in row] for row in self.matrix_entries]
        draw_graph(matrix_values, player=1)
        draw_graph(matrix_values, player=2)

    def validate_matrix(self):
        matrix_values = [[entry.get() for entry in row] for row in self.matrix_entries]
        for row in matrix_values:
            for value in row:
                try:
                    float(value)
                except Exception as e:
                    show_popup('Неправильный ввод', 'Все значения должны быть числами')
                    return False
        return True
                    
    def on_key(self, event):
        if event.keysym == 'Return':
            
            print(event.widget.index(INSERT))

            if event.widget == self.matrix_entries[-1][-1]:
                if not self.validate_matrix():
                    return
            else:
                event.widget.tk_focusNext().focus_set()

        if event.keysym == 'Right':
            if event.widget == self.matrix_entries[-1][-1]:
                text = event.widget.get()
                self.matrix_entries[0][0].focus_set()
            else:
                event.widget.tk_focusNext().focus_set()
        elif event.keysym == 'Left':
            if event.widget == self.matrix_entries[0][0]:
                self.matrix_entries[-1][-1].focus_set()
            else:
                event.widget.tk_focusPrev().focus_set()
        elif event.keysym == 'Up':
            for row in self.matrix_entries:
                if event.widget in row:
                    index = row.index(event.widget)
                    if index > 0:
                        row[index-1].focus_set()
                    else:
                        row[-1].focus_set()
                    break
        elif event.keysym == 'Down':
            for row in self.matrix_entries:
                if event.widget in row:
                    index = row.index(event.widget)
                    if index < len(row)-1:
                        row[index+1].focus_set()
                    else:
                        row[0].focus_set()
                    break

    def build(self):
        # Создание фрейма сцены ввода значений матрицы
        frame = tk.Frame(self.window)

        matrix_frame = tk.Frame(frame)
        matrix_frame.pack()

        matrix_label = tk.Label(matrix_frame, text="Введите значения матрицы", font=("Arial", 16))
        matrix_label.grid(row=0, columnspan=self.width, pady=10)

        self.matrix_entries = []
        for i in range(self.height):
            row_entries = []
            for j in range(self.width):
                entry = tk.Entry(matrix_frame, width=9, justify='center')
                entry.grid(row=i+1, column=j, padx=2, pady=2)
                entry.bind('<KeyPress>', self.on_key)
                row_entries.append(entry)
            self.matrix_entries.append(row_entries)

        self.solve_button = tk.Button(frame, text="Решить задачу", font=("Arial", 12), command=self.button_callback)
        self.solve_button.pack(pady=10)

        self.frames.append(frame)