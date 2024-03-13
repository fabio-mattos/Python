# Dicinário
# Guarda o dados através de chave e valor
aluno = {}

aluno['nome'] = 'Joao'
aluno['idade'] = 20
aluno['curso'] = 'Engenharia'

print(aluno)

#Mostrando o nome do aluno
print(f"O nome do aluno e: {aluno['nome']}")

#Excluindo
del aluno['idade']
