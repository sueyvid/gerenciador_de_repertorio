from view import View
from model import Model


class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.nome_do_arquivo = 'banco_de_dados.csv'
        self.configs()

    def configs(self):
        bt_Adicionar = self.view.bAdicionar
        bt_Adicionar['command'] = self.adicionar
        bt_Limpar = self.view.bLimpar
        bt_Limpar['command'] = self.limpar

    def adicionar(self):
        nome = self.view.nomeVar.get()
        artista = self.view.artistaVar.get()
        tom = self.view.tomVar.get()
        self.model.adicionar_csv(self.nome_do_arquivo, [nome, artista, tom])
        self.view.nomeVar.set('')
        self.view.artistaVar.set('')
        self.view.tomVar.set('')

    def limpar(self):
        self.model.criar_csv(self.nome_do_arquivo, ['Nome', 'Artísta', 'Tom'])

if __name__ == '__main__':
    v = View()
    m = Model()
    c = Controller(v, m)
    v.mainloop()