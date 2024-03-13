from blessings import Terminal
from openai import OpenAI
# Precisa pegar a key no site openai.com mas precisa ter credito
# Teste não finalizado
client = OpenAI(
    api_key='?????'
)

def gerar_questao(topico):
    resposta = client.completions.create(
        model="gpt-3.5-turbo",
        "role": "system",
        "content": "Faca perguntas:"
    )

# Roda somente em linux
term = Terminal()

print(term.clear)

print(term.bold_underline('Um texto qualquer'))
print(term.red('mensagem de erro'))
print(term.green('mensagem de sucesso'))

