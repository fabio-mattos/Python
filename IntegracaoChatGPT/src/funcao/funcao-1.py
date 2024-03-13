# Definindo uma função
def saudacao():
    print('Bom Dia')
    print('Boa Tarde')
    print('Boa Noite')

saudacao()



# Definindo uma função
def saudacao(nome, idade):
    print(f'Ola {nome}! Voce tem {idade} anos')

saudacao('Fabio',53)

#Pode passar os parametros nomeados independente da ordem

saudacao(idade=53, nome='Fabio')
 
saudacao(nome='Fabio', idade=53)