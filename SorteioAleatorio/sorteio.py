import random

def linha_aleatoria(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        linha_aleatoria = random.choice(linhas)
    return linha_aleatoria.strip()

nome_arquivo = 'lista.txt'   
linha = linha_aleatoria(nome_arquivo)
print("Linha aleatória selecionada:", linha)