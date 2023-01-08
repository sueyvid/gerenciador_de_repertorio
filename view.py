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
        area_de_trabalho = ttk.Frame(self)
        area_de_trabalho.pack()

        # Area de entrada
        area_de_entrada = ttk.Frame(area_de_trabalho)
        area_de_entrada.grid(row=0, column=0)

        tTituloEntrada = ttk.Label(area_de_entrada, text="Nova Música")
        tTituloEntrada.grid(row=0, column=0, sticky='WE')
        
        entradas = ttk.Frame(area_de_entrada)
        entradas.grid(row=1, column=0)

        self.nomeVar = tk.StringVar()
        tNome = ttk.Label(entradas, text="Título")
        eNome = ttk.Entry(entradas, textvariable=self.nomeVar)
        tNome.grid(row=1, column=0)
        eNome.grid(row=1, column=1)

        self.artistaVar = tk.StringVar()
        tArtista = ttk.Label(entradas, text="Artísta")
        eArtista = ttk.Entry(entradas, textvariable=self.artistaVar)
        tArtista.grid(row=2, column=0)
        eArtista.grid(row=2, column=1)

        self.tomVar = tk.StringVar()
        tTom = ttk.Label(entradas, text="Tom")
        eTom = ttk.Entry(entradas, textvariable=self.tomVar)
        tTom.grid(row=3, column=0)
        eTom.grid(row=3, column=1)

        self.ritmoVar = tk.StringVar()
        tRitmo = ttk.Label(entradas, text="Ritmo")
        eRitmo = ttk.Entry(entradas, textvariable=self.ritmoVar)
        tRitmo.grid(row=4, column=0)
        eRitmo.grid(row=4, column=1)

        botoes = ttk.Frame(area_de_entrada)
        botoes.grid(row=2, column=0)
        self.bAdicionar = ttk.Button(botoes, text='Adicionar')
        self.bAdicionar.grid(row=0, column=0)
        self.bEditar = ttk.Button(botoes, text='Editar')
        self.bEditar.grid(row=0, column=1)
        self.bRemover = ttk.Button(botoes, text='Remover')
        self.bRemover.grid(row=0, column=2)
        self.bLimpar = ttk.Button(botoes, text='Limpar')
        self.bLimpar.grid(row=0, column=3)
        self.bEditar.state(['disabled'])

        # Área de arquivo
        area_de_arquivo = ttk.Frame(area_de_trabalho)
        area_de_arquivo.grid(row=0, column=1)
        tTituloArquivo = ttk.Label(area_de_arquivo, text="Escolher Arquivo")
        tTituloArquivo.grid(row=0, column=0)
        self.arquivoVar = tk.StringVar(value='nome do arquivo')
        nome_do_arquivo = ttk.Label(area_de_arquivo, textvariable=self.arquivoVar)
        nome_do_arquivo.grid(row=1, column=0)
        self.bSelecionar = ttk.Button(area_de_arquivo, text='Selecionar Arquivo')
        self.bSelecionar.grid(row=2, column=0)
        self.bSalvar = ttk.Button(area_de_arquivo, text='Salvar Arquivo')
        self.bSalvar.grid(row=3, column=0)
        s = ttk.Style()
        # print(s.theme_names())
        s.theme_use('clam')
        self.bSalvar.state(['disabled'])

        # Área treeview
        self.tv_dados = ttk.Treeview(area_de_trabalho, columns=self.colunas, show='headings')
        for i in self.colunas:
            self.tv_dados.heading(i, text=i)
        self.tv_dados.grid(row=1, column=0, sticky='NSWE', columnspan=2)

        self.tv_repertorio = ttk.Treeview(area_de_trabalho, columns=self.colunas, show='headings')
        for i in self.colunas:
            self.tv_repertorio.heading(i, text=i)
        self.tv_repertorio.grid(row=2, column=0, sticky='NSWE', columnspan=2)

        self.bSubir = ttk.Button(area_de_trabalho, text='⬆')
        self.bSubir.grid(row=3, column=0)
        self.bDescer = ttk.Button(area_de_trabalho, text='⬇')
        self.bDescer.grid(row=3, column=1)
        self.bGerar = ttk.Button(area_de_trabalho, text='Gerar')
        self.bGerar.grid(row=4, column=0, columnspan=2)

if __name__ == "__main__":
    tela = View()
    tela.mainloop()