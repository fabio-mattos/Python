#Entradas e saidas da tela
""" 
  Para poder executar tem que ser via linha de comando:
  PS D:\DEV\Pessoal\Python\IntegracaoChatGPT> python D:\DEV\Pessoal\Python\IntegracaoChatGPT\src\fundamentos/oi.py
      Informe seu nome: 
       fabio
       fabio
     O nome informado é fabio
"""



print("Informe seu nome: ")
nome = input()

print("Informe sua idade:")
idade = int(input())


print(nome)

#F-String 
print(f"O nome informado é {nome} e tem {idade} anos")