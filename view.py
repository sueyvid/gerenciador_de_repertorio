import tkinter as tk
from tkinter import ttk
from tkinter_alterada import *


class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciador de Repertórios")
        self.colunas = ['Nome', 'Artísta', 'Tom', 'Ritmo']
        self.iniciar()

    def iniciar(self):
        # Tema tkinter
        s = ttk.Style()
        s.theme_use('clam')
        # print(s.theme_names())

        frame_principal = Frame(self)
        
        # Área de entrada
        frame_entrada = Frame(frame_principal)
        titulo_entrada = Label(frame_entrada, text="Nova Música")
        
        entradas = Frame(frame_entrada, grid=[1,0])
        tNome = Label(entradas, text="Título", grid=[1,0])
        self.nomeVar = Entry(entradas, grid=[1,1])
        tArtista = Label(entradas, text="Artísta", grid=[2,0])
        self.artistaVar = Entry(entradas, grid=[2,1])
        tTom = Label(entradas, text="Tom", grid=[3,0])
        self.tomVar = Entry(entradas, grid=[3,1])
        tRitmo = Label(entradas, text="Ritmo", grid=[4,0])
        self.ritmoVar = Combobox(entradas, grid=[4,1])

        botoes = Frame(frame_entrada, grid=[2,0])
        self.bAdicionar = Button(botoes, text='Adicionar', grid=[0,0])
        self.bEditar = Button(botoes, text='Editar', grid=[0,1])
        self.bRemover = Button(botoes, text='Remover', grid=[0,2])
        self.bLimpar = Button(botoes, text='Limpar', grid=[0,3])
        self.bEditar.state(['disabled'])

        # Área de arquivo
        frame_arquivo = Frame(frame_principal, grid=[0,1])
        titulo_arquivo = Label(frame_arquivo, text="Escolher Arquivo")
        nome_do_arquivo = Label(frame_arquivo, text='nome do arquivo', grid=[1,0])
        self.bSelecionar = Button(frame_arquivo, text='Selecionar Arquivo', grid=[2,0])
        self.bSalvar = Button(frame_arquivo, text='Salvar Arquivo', grid=[3,0])
        self.bSalvar.state(['disabled'])

        # Área treeview
        tv_frame = Frame(frame_principal, grid=[1,0], columnspan=2)
        self.tv_dados = Treeview(tv_frame, columns=self.colunas, show='headings', sticky='NSWE')
        self.tv_dados.definir_larguras([200, 150, 100, 100])
        self.tv_dados.scroll_vertical()

        self.tv_repertorio = Treeview(tv_frame, grid=[0,2], columns=self.colunas, show='headings', sticky='NSWE')
        self.tv_repertorio.definir_larguras([200, 150, 100, 100])
        self.tv_repertorio.scroll_vertical()

        # Área de modificações
        modificacoes_frame = Frame(frame_principal, grid=[2,0], columnspan=2)
        self.bSubir = Button(modificacoes_frame, text='⬆')
        self.bDescer = Button(modificacoes_frame, text='⬇', grid=[0,1])
        self.bGerar = Button(modificacoes_frame, text='Gerar', grid=[1,0], columnspan=2)

if __name__ == "__main__":
    tela = View()
    tela.mainloop()