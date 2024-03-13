# Dicionário chave valor
produto = {
    "nome": "Notebook",
    "preco": 4500.50,
    "quantidade": 100
}

# Iterando sobre as chaves do dicionário
for chave in produto:
   print(chave)

# Não importa o nome que colocar depois do for 
# vai mostrar sempre os valores das chaves   
   for xxx in produto:
       print(xxx)   

# Iterando sobre os valores do dicionário       
   for valor in produto.values():
      print(valor)     

   for chave, valor in produto.items():
       print(f"{chave} = {valor}")   

   for chave in produto:
       print(f"{chave} => {produto[chave]}")    