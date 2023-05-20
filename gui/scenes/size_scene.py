import tkinter as tk

from .scene import AbstractScene
from .matrix_scene import MatrixScene
from ..elements.popup import show_popup

class SizeEnterScene(AbstractScene):
    width_entry: tk.Entry
    height_entry: tk.Entry

    def __init__(self, window) -> None:
        super().__init__(window)

    def validate_size(self):
        width = self.width_entry.get()
        height = self.height_entry.get()
        if not width.isnumeric():
            print('Width must be a number')
            show_popup('Неправильный ввод', 'Ширина должна быть числом')
            return False
        if not height.isnumeric():
            print('Height must be a number')
            show_popup('Неправильный ввод', 'Высота должна быть числом')
            return False
        width = int(width)
        height = int(height)
        if not width == 2 and not height == 2 or width > 10 or height > 10: 
            show_popup('Неправильный ввод', 'Высота и ширина должны быть в пределах от 2 до 10')
            return False
        return True

    def button_callback(self):
        if not self.validate_size():
            return
        width = int(self.width_entry.get())
        height = int(self.height_entry.get())
        print(width, height)
        scene = MatrixScene(self.window, width, height)
        self.window.change_scene(scene)

    def on_key(self, event):
        if event.keysym == 'Return':
            if event.widget == self.width_entry:
                self.height_entry.focus_set()
            else:
                if not self.validate_size():
                    return
                width = int(self.width_entry.get())
                height = int(self.height_entry.get())
                scene = MatrixScene(self.window, width, height)
                self.window.change_scene(scene)

    def build(self):
        frame = tk.Frame(self.window)

        # Фрейм для воода размеров матрицы
        entry_frame = tk.Frame(frame)

        size_label = tk.Label(entry_frame, text="Размер матрицы:", font=("Arial", 12))
        size_label.grid(row=0, column=0, padx=10)

        # Поле для ввода ширины
        self.width_entry = tk.Entry(entry_frame, width=5)
        self.width_entry.grid(row=0, column=1, padx=5)
        self.width_entry.bind('<KeyPress>', self.on_key)

        # Поле для ввода высоты
        self.height_entry = tk.Entry(entry_frame, width=5)
        self.height_entry.grid(row=0, column=2, padx=5)
        self.height_entry.bind('<KeyPress>', self.on_key)

        entry_frame.pack(pady=100)

        # Кнопка "Начать"
        start_button = tk.Button(frame, text="Перейти к вводу матрицы", font=("Arial", 12), command=self.button_callback)
        start_button.pack()

        self.frames.append(frame)