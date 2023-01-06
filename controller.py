from view import View
from model import Model
import tkinter as tk
from tkinter import filedialog as fd
import os


class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.config_os()
        self.config_botoes()

    def config_os(self):
        self.nome_do_arquivo = 'banco_de_dados.csv'
        self.arquivo_raiz = r'C:\Users\suelt\OneDrive\Documentos\codigos\gerenciador_repertorio\dados\banco_de_dados.csv'
        self.filetypes = (('csv files', '*.csv'), ('All files', '*.*'))

        pasta_raiz = os.getcwd()
        self.arquivo_temp = f'{pasta_raiz}/temp.csv'
        self.arquivo_repertorio = f'{pasta_raiz}/repertorio.csv'
        self.local_do_arquivo = f'{pasta_raiz}/dados'
        if not 'dados' in os.listdir(pasta_raiz):
            os.mkdir(self.local_do_arquivo)
        self.recupera_dados()
        self.view.arquivoVar.set(value=f'nome do arquivo: {self.nome_do_arquivo}')

    def config_botoes(self):
        self.view.bAdicionar['command'] = self.adicionar
        self.view.bRemover['command'] = lambda:self.remover(self.arquivo_temp, self.view.tv_dados)
        self.view.bLimpar['command'] = lambda: self.limpar(self.arquivo_temp, self.view.tv_dados)
        self.view.bSelecionar['command'] = self.selecionar
        self.view.bSalvar['command'] = self.salvar
        self.view.tv_dados.bind('<Double-1>', self.adicionar_ao_repertorio)
        self.view.tv_repertorio.bind('<Double-1>', self.remover_do_repertorio)

    def adicionar_ao_repertorio(self, event):
        tv_dados = self.view.tv_dados
        for selected_item in tv_dados.selection():
            index = tv_dados.index(selected_item)
            musica = self.model.retorna_linha_csv(self.arquivo_temp, index+1)
            self.adicionar_musicas(self.arquivo_repertorio, self.view.tv_repertorio, [musica])
            self.remover(self.arquivo_temp, self.view.tv_dados)

    def remover_do_repertorio(self, event):
        tv_repertorio = self.view.tv_repertorio
        for selected_item in tv_repertorio.selection():
            index = tv_repertorio.index(selected_item)
            musica = self.model.retorna_linha_csv(self.arquivo_repertorio, index+1)
            self.adicionar_musicas(self.arquivo_temp, self.view.tv_dados, [musica])
            self.remover(self.arquivo_repertorio, self.view.tv_repertorio)

    def salvar(self):
        '''Abre uma caixa de diálogo para salvar o arquivo csv'''
        localfile = fd.asksaveasfilename(
            confirmoverwrite=True,
            filetypes=self.filetypes,
            initialdir=self.local_do_arquivo)
        self.model.copiar_conteudo_csv(self.arquivo_temp, self.arquivo_raiz)

    def selecionar(self):
        '''Abre uma caixa de diálogo para selecionar um arquivo csv com os dados'''
        localfile = fd.askopenfilename(
            title='Open a file',
            initialdir=self.local_do_arquivo,
            filetypes=self.filetypes)

        if localfile:
            self.nome_do_arquivo = localfile.split('/')[-1]
            self.arquivo_raiz = localfile
            self.recupera_dados()
            self.view.arquivoVar.set(value=f'nome do arquivo: {self.nome_do_arquivo}')
            self.view.bSalvar['state'] = tk.NORMAL

    def recupera_dados(self):
        '''limpa a treeview e o arquivo temporário,
        depois adiciona os dados no arquivo e na treeview'''
        musicas = self.model.ler_csv(self.arquivo_raiz)
        self.limpar(self.arquivo_temp, self.view.tv_dados)
        self.limpar(self.arquivo_repertorio, self.view.tv_repertorio)
        self.adicionar_musicas(self.arquivo_temp, self.view.tv_dados, musicas[1:])

    def adicionar_musicas(self, nome_do_arquivo, tv, musicas):
        for musica in musicas:
            nome, artista, tom, ritmo = musica
            self.model.adicionar_csv(nome_do_arquivo, [nome, artista, tom, ritmo])
            tv.insert('', tk.END, values=(nome, artista, tom, ritmo))

    def adicionar(self):
        '''adiciona os dados a partir das entradas'''
        nome = self.get_strVar(self.view.nomeVar)
        artista = self.get_strVar(self.view.artistaVar)
        tom = self.get_strVar(self.view.tomVar)
        ritmo = self.get_strVar(self.view.ritmoVar)
        self.adicionar_musicas(self.arquivo_temp, self.view.tv_dados, [[nome, artista, tom, ritmo]])
    
    def get_strVar(self, variavel):
        texto = variavel.get()
        variavel.set('')
        return texto

    def remover(self, nome_do_arquivo, tv):
        '''remove dado, selecionado pelo usuário, do arquivo e da treeview'''
        for selected_item in tv.selection():
            index = tv.index(selected_item)
            self.model.remover_linha_csv(nome_do_arquivo, index+1)
            tv.delete(selected_item)

    def limpar(self, nome_do_arquivo, tv):
        '''reseta o arquivo csv e apaga todos os dados da treeview'''
        self.model.reescrever_conteudo_csv(nome_do_arquivo, self.view.colunas)
        for i in tv.get_children():
            tv.delete(i)

if __name__ == '__main__':
    v = View()
    m = Model()
    c = Controller(v, m)
    v.mainloop()