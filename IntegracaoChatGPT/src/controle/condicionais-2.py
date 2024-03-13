ano_nascimento = int(input("Em que ano voce nasceu?"))

if ano_nascimento <= 1964:
     geracao = "Geracao Baby Boomer"
elif ano_nascimento >= 1965 and ano_nascimento <= 1980:
    geracao = "Geracao X"     
elif ano_nascimento >= 1981 and ano_nascimento <= 1996:
    geracao = "Geracao Millenial"         
else:
    geracao = "Geracao Alpha"     

print(geracao)    