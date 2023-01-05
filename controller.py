from view import View
from model import Model
import tkinter as tk
from tkinter import filedialog as fd


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
        bt_Salvar = self.view.bSalvar
        bt_Salvar['command'] = self.salvar

    def salvar(self):
        filetypes = (
            ('csv files', '*.csv'),
            ('All files', '*.*')
        )

        localfile = fd.asksaveasfilename(
            confirmoverwrite=True,
            filetypes=filetypes,
            initialdir='/Desktop')

        local = self.nome_do_arquivo.split('/')
        temp = ''
        for i in local[:-2]:
            temp += f'{i}/'
        temp += 'temp.csv'
        # print(self.model.ler_csv(s))

        conteudo = self.model.ler_csv(temp)
        col = self.view.colunas
        self.model.criar_csv(self.nome_do_arquivo, col)
        for linha in conteudo[1:]:
            self.model.adicionar_csv(self.nome_do_arquivo, linha)


    def selecionar(self):
        filetypes = (
            ('csv files', '*.csv'),
            ('All files', '*.*')
        )

        localfile = fd.askopenfilename(
            title='Open a file',
            initialdir='/Desktop',
            filetypes=filetypes)

        if localfile:
            filename = localfile.split('/')[-1]
            self.nome_do_arquivo = f'{localfile}'
            self.recupera_dados()
            self.view.arquivoVar.set(value=f'nome do arquivo: {filename}')
            self.view.bSalvar['state'] = tk.NORMAL

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
        tv = self.view.tv
        for i in tv.get_children():
            tv.delete(i)

if __name__ == '__main__':
    v = View()
    m = Model()
    c = Controller(v, m)
    v.mainloop()