import tkinter as tk
from dados import adicionar_csv, criar_csv


class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciador de Repertórios")
        self.iniciar()
        self.nome_do_arquivo = 'banco_de_dados.csv'

    def iniciar(self):
        tamLetra = 20
        area_de_trabalho = tk.Frame(self)
        tTituloPagina = tk.Label(area_de_trabalho, text="Nova Música", font=('', tamLetra))

        area_de_trabalho.pack()
        tTituloPagina.grid(row=0, column=0)

        self.nomeVar = tk.StringVar()
        self.artistaVar = tk.StringVar()
        self.tomVar = tk.StringVar()

        entradas = tk.Frame(area_de_trabalho)
        tNome = tk.Label(entradas, text="Título", font=('', tamLetra))
        self.eNome = tk.Entry(entradas, font=('', tamLetra), textvariable=self.nomeVar)
        tArtista = tk.Label(entradas, text="Artísta", font=('', tamLetra))
        self.eArtista = tk.Entry(entradas, font=('', tamLetra), textvariable=self.artistaVar)
        tTom = tk.Label(entradas, text="Tom", font=('', tamLetra))
        self.eTom = tk.Entry(entradas, font=('', tamLetra), textvariable=self.tomVar)

        entradas.grid(row=1, column=0)
        tNome.grid(row=0, column=0)
        self.eNome.grid(row=0, column=1)
        tArtista.grid(row=1, column=0)
        self.eArtista.grid(row=1, column=1)
        tTom.grid(row=2, column=0)
        self.eTom.grid(row=2, column=1)

        botoes = tk.Frame(area_de_trabalho)
        bAdicionar = tk.Button(botoes, text='Adicionar', font=('', tamLetra), command=self.adicionar)
        bLimpar = tk.Button(botoes, text='Limpar', font=('', tamLetra), command=self.limpar)

        botoes.grid(row=2, column=0)
        bAdicionar.grid(row=0, column=0)
        bLimpar.grid(row=0, column=1)

    def adicionar(self):
        nome = self.eNome.get()
        artista = self.eArtista.get()
        tom = self.eTom.get()
        adicionar_csv(self.nome_do_arquivo, [nome, artista, tom])
        self.nomeVar.set('')
        self.artistaVar.set('')
        self.tomVar.set('')

    def limpar(self):
        criar_csv(self.nome_do_arquivo, ['Nome', 'Artísta', 'Tom'])

if __name__ == "__main__":
    tela = View()
    tela.mainloop()