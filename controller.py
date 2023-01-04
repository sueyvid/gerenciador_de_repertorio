from view import View
from model import Model
import tkinter as tk
from tkinter import filedialog as fd


#TODO: Opção de salvar base de dados
#TODO: Treeview do repertório


class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.nome_do_arquivo = ''
        self.config_botoes()

    def config_botoes(self):
        bt_Adicionar = self.view.bAdicionar
        bt_Adicionar['command'] = self.adicionar
        bt_Remover = self.view.bRemover
        bt_Remover['command'] = self.remover
        bt_Limpar = self.view.bLimpar
        bt_Limpar['command'] = self.limpar
        bt_Selecionar = self.view.bSelecionar
        bt_Selecionar['command'] = self.selecionar

    def selecionar(self):
        filetypes = (
            ('csv files', '*.csv'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='../gerenciador_repertorio/dados',
            filetypes=filetypes)

        if filename:
            filename = filename.split('/')[-1]
            self.nome_do_arquivo = f'../gerenciador_repertorio/dados/{filename}'
            self.recupera_dados()
            self.view.arquivoVar.set(value=f'nome do arquivo: {filename}')

    def recupera_dados(self):
        musicas = self.model.ler_csv(self.nome_do_arquivo)
        nome_do_arquivo = 'temp.csv'
        self.limpar()
        tv = self.view.tv
        for musica in musicas[1:]:
            nome, artista, tom, ritmo = musica
            self.model.adicionar_csv(nome_do_arquivo, [nome, artista, tom, ritmo])
            tv.insert('', tk.END, values=(nome, artista, tom, ritmo))

    def adicionar(self):
        nome_do_arquivo = 'temp.csv'
        nome = self.view.nomeVar.get()
        artista = self.view.artistaVar.get()
        tom = self.view.tomVar.get()
        ritmo = self.view.ritmoVar.get()
        self.model.adicionar_csv(nome_do_arquivo, [nome, artista, tom, ritmo])
        tv = self.view.tv
        tv.insert('', tk.END, values=(nome, artista, tom, ritmo))
        self.view.nomeVar.set('')
        self.view.artistaVar.set('')
        self.view.tomVar.set('')
        self.view.ritmoVar.set('')

    def remover(self):
        nome_do_arquivo = 'temp.csv'
        tv = self.view.tv
        for selected_item in tv.selection():
            index = tv.index(selected_item)
            self.model.remover_linha_csv(nome_do_arquivo, index+1)
            tv.delete(selected_item)

    def limpar(self):
        nome_do_arquivo = 'temp.csv'
        col = self.view.colunas
        self.model.criar_csv(nome_do_arquivo, col)

if __name__ == '__main__':
    v = View()
    m = Model()
    c = Controller(v, m)
    v.mainloop()