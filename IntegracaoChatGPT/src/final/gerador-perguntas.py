from blessings import Terminal
from openai import OpenAI
import json

# Precisa pegar a key no site openai.com mas precisa ter credito
client = OpenAI(
    api_key='?????'
)


def gerar_questao(topico):
    resposta = client.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": """
          Faca perguntas e responda uma opcoes de resposta entre 1 a 4  
        """
        }, {
            "role": "user",
            "content": f"Gere uma questao sobre {topico}"
        }]
    )

    conteudo = resposta.choices[0].message.content
    return json.loads(conteudo)


pontos = 0
# Roda somente em linux
term = Terminal()
topico = input("Sobre qual tópico voce quer responder?")

while topico:
    print("Carregando")
    questao = gerar_questao(topico)

    print(term.clear)
    print(term.bold_underline(questao['pergunta']))

    for i, opcao in enumerate(questao['opcoes'], start=1):
        print(f"{i}) {opcao}")

    resposta = int(input("Escolha uma opcao[1-4]:")) -1
    escolhida = questao['opcoes'][resposta].lower()
    certa = questao['certa'].lower()

    if escolhida == certa:
        pontos += 1
        print(term.green(f"Voce acertou! Agora voce tem {pontos} pontos\n"))
    else:
        print(term.red(f"Voce erro! A resposta correta era: {certa}"))

    continuar = input("Quer Continuar? S/n")

    if continuar.lower() == 'n':
        break

print('Programa Finalizado!')