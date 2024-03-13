import json

#OBS: Json tem que ter aspas duplas separando as chaves e valores.
exemplo = """
   {
      "pergunta": "Qual o resultado da expressao 2 + 2?",
      "opcoes":  ["5","4","11","22"],
      "certa": "4"
   }

"""
questao = json.loads(exemplo)

opcoes = questao['opcoes']

print("Qual o valor de 2 + 2?")
for i, opcao in enumerate(opcoes,start=1):
    print(f"{i}) {opcao}")


resposta = int(input("Escolha uma opcao acima de [1-4]: "))
opcao_selecionada = opcoes[resposta - 1]
opcao_certa = questao['certa']


if opcao_selecionada == opcao_certa:
    print("Voce acertou!")
else:
    print(f"Voce errou! A resposta certa e: {opcao_certa}")

