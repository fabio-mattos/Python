#Laço for
for i in range(10):
    print(f"Mostrando o valor de i = {i}")


# Laço for passando o intervalo
# Nesse exemplo o laço vai de 1 a 10
for i in range(1,11):
    print(f"Mostrando o valor de i = {i}")    


# Mostrando a saida 1 - 2 - 3 - 4 - 5
for i in range(1, 6):
    print(i, end=" - " if i < 5 else "")
