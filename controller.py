from view import View
from model import Model
import tkinter as tk


class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.nome_do_arquivo = 'banco_de_dados.csv'
        self.configs()
        self.recupera_dados()

    def configs(self):
        bt_Adicionar = self.view.bAdicionar
        bt_Adicionar['command'] = self.adicionar
        bt_Remover = self.view.bRemover
        bt_Remover['command'] = self.remover
        bt_Limpar = self.view.bLimpar
        bt_Limpar['command'] = self.limpar

    def recupera_dados(self):
        musicas = self.model.ler_csv(self.nome_do_arquivo)
        tv = self.view.tv
        for musica in musicas[1:]:
            tv.insert('', tk.END, values=(musica[0], musica[1], musica[2], musica[3]))    

    def adicionar(self):
        nome = self.view.nomeVar.get()
        artista = self.view.artistaVar.get()
        tom = self.view.tomVar.get()
        ritmo = self.view.ritmoVar.get()
        self.model.adicionar_csv(self.nome_do_arquivo, [nome, artista, tom, ritmo])
        tv = self.view.tv
        tv.insert('', tk.END, values=(nome, artista, tom, ritmo))
        self.view.nomeVar.set('')
        self.view.artistaVar.set('')
        self.view.tomVar.set('')
        self.view.ritmoVar.set('')

    def remover(self):
        tv = self.view.tv
        for selected_item in tv.selection():
            index = tv.index(selected_item)
            self.model.remover_linha_csv(self.nome_do_arquivo, index+1)
            tv.delete(selected_item)

    def limpar(self):
        col = self.view.colunas
        self.model.criar_csv(self.nome_do_arquivo, col)

if __name__ == '__main__':
    v = View()
    m = Model()
    c = Controller(v, m)
    v.mainloop()