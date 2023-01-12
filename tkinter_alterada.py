import tkinter as tk
from tkinter import ttk


class Frame(ttk.Frame):
    def __init__(self, master, grid=[0, 0], sticky=None, **kwargs):
        super().__init__(master)
        self.grid(row=grid[0], column=grid[1], sticky=sticky, **kwargs)

class Label(ttk.Label):
    def __init__(self, master, text, grid=[0, 0], sticky=None):
        self.texto = tk.StringVar()
        super().__init__(master, text=text)
        self.grid(row=grid[0], column=grid[1], sticky=sticky)

    def ativar_textvariable(self, texto=None):
        if texto:
            self.texto.set(texto)
        self.config(textvariable=self.texto)

    def set(self, value):
        self.texto.set(value)

class Entry(ttk.Entry):
    def __init__(self, master, grid=[0, 0], sticky=None):
        self.texto = tk.StringVar()
        super().__init__(master, textvariable=self.texto)
        self.grid(row=grid[0], column=grid[1], sticky=sticky)

    def set(self, texto):
        self.texto.set(texto)

class Combobox(ttk.Combobox):
    def __init__(self, master, grid=[0, 0], sticky=None):
        super().__init__(master)
        self.grid(row=grid[0], column=grid[1], sticky=sticky)

    def adicionar_opcoes(self, opcoes):
        self["values"] = opcoes
    
    def selecionar_opcao(self, opcao):
        self.set(opcao)

    def selecionado(self):
        return self.get()

class Button(ttk.Button):
    def __init__(self, master, text, grid=[0, 0], sticky=None, **kwargs):
        super().__init__(master, text=text)
        self.grid(row=grid[0], column=grid[1], sticky=sticky, **kwargs)

class Treeview(ttk.Treeview):
    def __init__(self, master, grid=[0, 0], columns=None, show='headings', sticky=None):
        super().__init__(master, columns=columns, show=show)
        self.grid(row=grid[0], column=grid[1], sticky=sticky)
        self.colunas = columns
        self.grid = grid
        for i in columns:
            self.heading(i, text=i)

    def definir_larguras(self, larguras):
        for i, v in enumerate(self.colunas):
            self.column(v, width=larguras[i])

    def scroll_vertical(self):
        sb_y = ttk.Scrollbar(self.master, orient=tk.VERTICAL, command=self.yview)
        self.configure(yscroll=sb_y.set)
        sb_y.grid(row=self.grid[0], column=self.grid[1]+1, sticky='NS')