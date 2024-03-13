# Quantidade indeterminada de repetições
# For é usado geralmente quando sabemos a quantidade de repetições
# while é usado quando não sabemos a quantidade de repetições

pergunta = "Deseja continuar? (S/n) "
resposta = input(pergunta)
quantidade  = 1

while resposta.lower() != "n":
    print(f"Vamos continuar pela {quantidade} vez")
    resposta = input(pergunta)

    quantidade += 1
    # quantidade = quantidade + 1

print("Encerrando...")
