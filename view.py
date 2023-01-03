import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciador de Repertórios")
        self.colunas = ['Nome', 'Artísta', 'Tom', 'Ritmo']
        self.iniciar()

    def iniciar(self):
        tamLetra = 20
        area_de_trabalho = tk.Frame(self)
        area_de_trabalho.pack()

        area_de_entrada = tk.Frame(area_de_trabalho)
        area_de_entrada.grid(row=0, column=0)

        tTituloPagina = tk.Label(area_de_entrada, text="Nova Música", font=('', tamLetra))
        tTituloPagina.grid(row=0, column=0, sticky='WE')
        
        entradas = tk.Frame(area_de_entrada)
        entradas.grid(row=1, column=0)

        self.nomeVar = tk.StringVar()
        tNome = tk.Label(entradas, text="Título", font=('', tamLetra))
        eNome = tk.Entry(entradas, font=('', tamLetra), textvariable=self.nomeVar)
        tNome.grid(row=1, column=0)
        eNome.grid(row=1, column=1)

        self.artistaVar = tk.StringVar()
        tArtista = tk.Label(entradas, text="Artísta", font=('', tamLetra))
        eArtista = tk.Entry(entradas, font=('', tamLetra), textvariable=self.artistaVar)
        tArtista.grid(row=2, column=0)
        eArtista.grid(row=2, column=1)

        self.tomVar = tk.StringVar()
        tTom = tk.Label(entradas, text="Tom", font=('', tamLetra))
        eTom = tk.Entry(entradas, font=('', tamLetra), textvariable=self.tomVar)
        tTom.grid(row=3, column=0)
        eTom.grid(row=3, column=1)

        self.ritmoVar = tk.StringVar()
        tRitmo = tk.Label(entradas, text="Ritmo", font=('', tamLetra))
        eRitmo = tk.Entry(entradas, font=('', tamLetra), textvariable=self.ritmoVar)
        tRitmo.grid(row=4, column=0)
        eRitmo.grid(row=4, column=1)

        botoes = tk.Frame(area_de_entrada)
        self.bAdicionar = tk.Button(botoes, text='Adicionar', font=('', tamLetra))
        self.bLimpar = tk.Button(botoes, text='Limpar', font=('', tamLetra))

        botoes.grid(row=2, column=0)
        self.bAdicionar.grid(row=0, column=0)
        self.bLimpar.grid(row=0, column=1)

        self.tv = ttk.Treeview(area_de_trabalho, columns=self.colunas, show='headings')
        for i in self.colunas:
            self.tv.heading(i, text=i)
        self.tv.grid(row=0, column=1, sticky='NSWE')

if __name__ == "__main__":
    tela = View()
    tela.mainloop()