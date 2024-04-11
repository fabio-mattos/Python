from random import choice

with open('lista.txt', 'r', encoding='utf-8') as arq:
    x = arq.readlines()
    linha_selecionada = choice(x).strip() 
    print(f'O selecionado foi: {linha_selecionada}' )