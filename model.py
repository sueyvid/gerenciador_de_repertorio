'''
Nome: Biblioteca para alterar csv
Autor: Sueyvid José
'''
import csv


class Model:
    def __init__(self):
        self.code = 'UTF-8'

    def criar_csv(self, nome_do_arquivo, texto:list):
        '''
        Nome do Arquivo: string com a extensão .csv
        Texto: lista de strings
        '''
        with open(nome_do_arquivo, 'w', newline='', encoding=self.code) as csvfile:
            escritor = csv.writer(csvfile, delimiter=',')
            escritor.writerow(texto)

    def adicionar_csv(self, nome_do_arquivo, texto:list):
        '''
        Nome do Arquivo: string com a extensão .csv
        Texto: lista de strings
        '''
        with open(nome_do_arquivo, 'a', newline='', encoding=self.code) as csvfile:
            escritor = csv.writer(csvfile, delimiter=',')
            escritor.writerow(texto)

    def ler_csv(self, nome_do_arquivo):
        texto = list()
        with open(nome_do_arquivo, newline='', encoding=self.code) as csvfile:
            leitor = csv.reader(csvfile, delimiter=',')
            for row in leitor:
                texto.append(row)
        return texto

    def remover_linha_csv(self, nome_do_arquivo, linha):
        texto = self.ler_csv(nome_do_arquivo)
        texto.pop(linha)
        self.criar_csv(nome_do_arquivo, texto[0])
        for i in texto[1:]:
            self.adicionar_csv(nome_do_arquivo, i)
    
if __name__ == '__main__':
    m = Model()
    m.criar_csv('banco_de_dados.csv', ['Slot 1', 'Slot 2', 'Slot 3'])
    m.adicionar_csv('banco_de_dados.csv', ['Slot 1', 'Slot 2', 'Slot 4'])
    m.adicionar_csv('banco_de_dados.csv', ['Slot 1', 'Slot 2', 'Slot 5'])
    print(m.ler_csv('banco_de_dados.csv'))
    m.remover_linha_csv('banco_de_dados.csv', 0)