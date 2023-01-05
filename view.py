import tkinter as tk
from tkinter import ttk


class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciador de Repertórios")
        self.colunas = ['Nome', 'Artísta', 'Tom', 'Ritmo']
        self.iniciar()

    def iniciar(self):
        # Area de trabalho
        tamLetra = 20
        area_de_trabalho = tk.Frame(self)
        area_de_trabalho.pack()

        # Area de entrada
        area_de_entrada = tk.Frame(area_de_trabalho)
        area_de_entrada.grid(row=0, column=0)

        tTituloEntrada = tk.Label(area_de_entrada, text="Nova Música", font=('', tamLetra))
        tTituloEntrada.grid(row=0, column=0, sticky='WE')
        
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
        botoes.grid(row=2, column=0)
        self.bAdicionar = tk.Button(botoes, text='Adicionar', font=('', tamLetra))
        self.bAdicionar.grid(row=0, column=0)
        self.bRemover = tk.Button(botoes, text='Remover', font=('', tamLetra))
        self.bRemover.grid(row=0, column=1)
        self.bLimpar = tk.Button(botoes, text='Limpar', font=('', tamLetra))
        self.bLimpar.grid(row=0, column=2)

        # Área de arquivo
        area_de_arquivo = tk.Frame(area_de_trabalho)
        area_de_arquivo.grid(row=0, column=1)
        tTituloArquivo = tk.Label(area_de_arquivo, text="Escolher Arquivo", font=('', tamLetra))
        tTituloArquivo.grid(row=0, column=0)
        self.arquivoVar = tk.StringVar(value='nome do arquivo')
        nome_do_arquivo = tk.Label(area_de_arquivo, textvariable=self.arquivoVar, font=('', 15))
        nome_do_arquivo.grid(row=1, column=0)
        self.bSelecionar = tk.Button(area_de_arquivo, text='Selecionar Arquivo', font=('', tamLetra))
        self.bSelecionar.grid(row=2, column=0)
        self.bSalvar = ttk.Button(area_de_arquivo, text='Salvar Arquivo')
        self.bSalvar.grid(row=3, column=0)
        self.bSalvar.state(['disabled'])

        # Área treeview
        self.tv = ttk.Treeview(area_de_trabalho, columns=self.colunas, show='headings')
        for i in self.colunas:
            self.tv.heading(i, text=i)
        self.tv.grid(row=1, column=0, sticky='NSWE', columnspan=2)

if __name__ == "__main__":
    tela = View()
    tela.mainloop()