import random

# Gera um numero aleatorio entre 1 e 10
a = random.randint(1, 10)

# Sempre tem que indentar o bloco do if com tab
if a > 5:
    print(f"O valor de a = {a}")
    print("O valor e maior que 5")
    print("Expressao gerou um resultado: True")
    print("Continua dentro do bloco do IF")
else:
    print(f"O valor de a = {a}")
    print("Continua dentro do bloco do ELSE")
    print("Expressao gerou um resultado: True")
    print("Continua dentro do bloco do ELSE")

print("Fim do Codigo")