import csv

def criar_csv(nome_do_arquivo, texto:list):
    '''
    Nome do Arquivo: string com a extensão .csv
    Texto: lista de strings
    '''
    with open(nome_do_arquivo, 'w', newline='') as csvfile:
        escritor = csv.writer(csvfile, delimiter=',')
        escritor.writerow(texto)

def adicionar_csv(nome_do_arquivo, texto:list):
    '''
    Nome do Arquivo: string com a extensão .csv
    Texto: lista de strings
    '''
    with open(nome_do_arquivo, 'a', newline='') as csvfile:
        escritor = csv.writer(csvfile, delimiter=',')
        escritor.writerow(texto)

def ler_csv(nome_do_arquivo):
    texto = list()
    with open(nome_do_arquivo, newline='') as csvfile:
        leitor = csv.reader(csvfile, delimiter=',')
        for row in leitor:
            texto.append(row)
    return texto

def remover_linha_csv(nome_do_arquivo, linha):
    texto = ler_csv(nome_do_arquivo)
    texto.pop(linha)
    criar_csv(nome_do_arquivo, texto[0])
    for i in texto[1:]:
        adicionar_csv(nome_do_arquivo, i)
    

criar_csv('banco_de_dados.csv', ['Slot 1', 'Slot 2', 'Slot 3'])
adicionar_csv('banco_de_dados.csv', ['Slot 1', 'Slot 2', 'Slot 4'])
adicionar_csv('banco_de_dados.csv', ['Slot 1', 'Slot 2', 'Slot 5'])
print(ler_csv('banco_de_dados.csv'))
remover_linha_csv('banco_de_dados.csv', 0)