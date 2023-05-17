import tkinter as tk

from .scenes.scene import AbstractScene
from .scenes.size_scene import SizeEnterScene

class App(tk.Tk):
    current_scene: AbstractScene
    
    def __init__(self) -> None:
        super().__init__()
        self.geometry("600x400")

        # Заголовок
        title_label = tk.Label(self, text="Решение игры геометрическим методом", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Автор
        author_text = tk.Entry(self, font=("Arial", 10), justify='center', width=100)
        author_text.insert(0, "github.com/aptemmaleev")
        author_text.config(state='readonly')
        author_text.pack(padx=200)

        self.current_scene = SizeEnterScene(self)
        self.current_scene.build()
        self.current_scene.show()
    
    def change_scene(self, new_scene: AbstractScene):
        self.current_scene.hide()
        self.current_scene = new_scene
        self.current_scene.build()
        self.current_scene.show()

    def start(self):
        self.mainloop()