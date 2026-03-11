#pergunte a idade
idade = int(input("Digite sua idade: "))

#Pergunte quantos jogos ja jogou?
jogou_3 = (input("Já jogou 3 jogos? (Responda true or false) "))

#Converta jogou_3 para valor booleano
jogou_3 = jogou_3 == "True"

#Solicite quantas vitorias 
vitorias = int(input("Quantos jogos você já venceu? "))  

apto = (16 <= idade <= 18) and jogou_3 and (vitorias >= 1)

print (apto)