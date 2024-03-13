lista = [1 , 2 , 3, 4, 5]

print(lista[0])

lista[1] = 20

print(lista)

# Adicionando valores a lista.
lista.append(6)
print(lista)

# Remove pela pelo valor e não pelo index.
lista.remove(6)
print(lista)

lista.append(7)
lista.append(-4)
#Ordenando os valores da lista
lista.sort()
print(lista)

#Mostrando o tamanho da lista
print(len(lista))

#Verificando se o valor esta na lista.
print(4 in lista)