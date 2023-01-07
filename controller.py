from view import View
from model import Model
import tkinter as tk
from tkinter import filedialog as fd
import os


class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.entradas = [self.view.nomeVar,
                    self.view.artistaVar,
                    self.view.tomVar,
                    self.view.ritmoVar]
        self.config_os()
        self.config_botoes()

    def config_os(self):
        self.nome_do_arquivo = ''
        self.arquivo_raiz = ''
        self.filetypes = (('csv files', '*.csv'), ('All files', '*.*'))

        pasta_raiz = os.getcwd()
        self.arquivo_temp = f'{pasta_raiz}/temp.csv'
        self.arquivo_repertorio = f'{pasta_raiz}/repertorio.csv'
        self.local_do_arquivo = f'{pasta_raiz}/dados'
        if not 'dados' in os.listdir(pasta_raiz):
            os.mkdir(self.local_do_arquivo)

    def config_botoes(self):
        arq_temp = self.arquivo_temp
        arq_rep = self.arquivo_repertorio
        tv_dados = self.view.tv_dados
        tv_rep = self.view.tv_repertorio
        mus = self.pegar_dados_entrada

        self.view.bAdicionar['command'] = lambda: self.adicionar(arq_temp, tv_dados, mus)
        self.view.bEditar['command'] = lambda: self.editar(arq_temp, tv_dados, mus)
        self.view.bRemover['command'] = lambda: self.remover(arq_temp, tv_dados)
        self.view.bLimpar['command'] = lambda: self.limpar(arq_temp, tv_dados)
        self.view.bSelecionar['command'] = self.selecionar
        self.view.bSalvar['command'] = self.salvar
        tv_dados.bind('<Double-1>', lambda e: self.mover_musica(e, tv_dados, tv_rep, arq_temp, arq_rep))
        tv_rep.bind('<Double-1>', lambda e: self.mover_musica(e, tv_rep, tv_dados, arq_rep, arq_temp))
        tv_dados.bind('<ButtonRelease>', self.selecao)
        self.view.bSubir['command'] = lambda: self.mudar_posicao_musica(tv_rep, 'subir')
        self.view.bDescer['command'] = lambda: self.mudar_posicao_musica(tv_rep, 'descer')

    def selecao(self, e):
        if not self.view.tv_dados.selection():
            for var in self.entradas:
                var.set('')
        else:
            selecionado = self.view.tv_dados.selection()[0]
            index = self.view.tv_dados.index(selecionado)
            texto = self.model.retorna_linha_csv(self.arquivo_temp, index+1)
            for i, var in enumerate(self.entradas):
                var.set(texto[i])

    # Entrada
    def pegar_dados_entrada(self):
        '''Pega os dados escritos na entrada e os retorna'''
        musica = list()
        for variavel in self.entradas:
            musica.append(variavel.get())
            variavel.set('')
        return musica

    def adicionar(self, nome_do_arquivo, tv, musicas, pos=tk.END):
        '''adiciona músicas no arquivo e na treeview'''
        if not isinstance(musicas, list):
            musicas = musicas()
        if isinstance(musicas[0], list):
            for musica in musicas:
                if not pos == tk.END:
                    self.model.adicionar_csv(nome_do_arquivo, musica, pos+1)
                else:
                    self.model.adicionar_csv(nome_do_arquivo, musica)
                tv.insert('', pos, values=musica)
        else:
            if not pos == tk.END:
                self.model.adicionar_csv(nome_do_arquivo, musicas, pos+1)
            else:
                self.model.adicionar_csv(nome_do_arquivo, musicas)
            tv.insert('', pos, values=musicas)

    def editar(self, nome_do_arquivo, tv, musica):
        '''adiciona músicas no arquivo e na treeview'''
        if not isinstance(musica, list):
            musica = self.pegar_dados_entrada()
        selecionado = tv.selection()[0]
        index = tv.index(selecionado)
        self.model.editar_linha_csv(nome_do_arquivo, musica, index+1)
        for i in range(4):
            tv.set(selecionado, self.view.colunas[i], value=musica[i])
        tv.selection_remove(selecionado)

    def remover(self, nome_do_arquivo, tv):
        '''remove música, selecionada pelo usuário, do arquivo e da treeview'''
        for selected_item in tv.selection():
            index = tv.index(selected_item)
            self.model.remover_linha_csv(nome_do_arquivo, index+1)
            tv.delete(selected_item)

    def limpar(self, nome_do_arquivo, tv):
        '''reseta o arquivo e a treeview'''
        self.model.reescrever_conteudo_csv(nome_do_arquivo, self.view.colunas)
        for i in tv.get_children():
            tv.delete(i)

    # Arquivo
    def selecionar(self):
        '''Abre uma caixa de diálogo para selecionar um arquivo csv com os dados'''
        local_do_arquivo = fd.askopenfilename(
            title='Open a file',
            initialdir=self.local_do_arquivo,
            filetypes=self.filetypes)

        if local_do_arquivo:
            self.nome_do_arquivo = local_do_arquivo.split('/')[-1]
            self.arquivo_raiz = local_do_arquivo
            self.recupera_dados()
            self.view.arquivoVar.set(value=f'nome do arquivo: {self.nome_do_arquivo}')
            self.view.bSalvar['state'] = tk.NORMAL

    def salvar(self):
        '''Abre uma caixa de diálogo para salvar o arquivo csv'''
        local_do_arquivo = fd.asksaveasfilename(
            confirmoverwrite=True,
            filetypes=self.filetypes,
            initialdir=self.local_do_arquivo)
        self.arquivo_raiz = local_do_arquivo
        self.model.copiar_conteudo_csv(self.arquivo_temp, self.arquivo_raiz)

    def recupera_dados(self):
        '''limpa as treeviews e o arquivo temporário,
        depois adiciona os dados no arquivo e na treeview'''
        musicas = self.model.ler_csv(self.arquivo_raiz)
        self.limpar(self.arquivo_temp, self.view.tv_dados)
        self.limpar(self.arquivo_repertorio, self.view.tv_repertorio)
        self.adicionar(self.arquivo_temp, self.view.tv_dados, musicas[1:])

    # Treeview
    def mover_musica(self, event, tv1, tv2, arq1, arq2):
        for selected_item in tv1.selection():
            index = tv1.index(selected_item)
            musica = self.model.retorna_linha_csv(arq1, index+1)
            self.remover(arq1, tv1)
            self.adicionar(arq2, tv2, musica)

    def mudar_posicao_musica(self, tv, opcao):
        tam = len(tv.get_children()) - 1
        selecionado = self.view.tv_repertorio.selection()[0]
        index = tv.index(selecionado)
        musica = self.model.retorna_linha_csv(self.arquivo_repertorio, index+1)
        if opcao == 'subir' and index != 0:
            self.model.remover_linha_csv(self.arquivo_repertorio, index+1)
            self.model.adicionar_csv(self.arquivo_repertorio, musica, index)
            tv.move(selecionado, '', index-1)
        elif opcao == 'descer' and index != tam:
            self.model.remover_linha_csv(self.arquivo_repertorio, index+1)
            self.model.adicionar_csv(self.arquivo_repertorio, musica, index+2)
            tv.move(selecionado, '', index+1)
        else:
            print('posicao inválida')

if __name__ == '__main__':
    v = View()
    m = Model()
    c = Controller(v, m)
    v.mainloop()