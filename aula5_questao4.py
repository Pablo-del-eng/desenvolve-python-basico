classe = input("Qual a sua classe? ")

força = int(input("Quantos pontos de força? "))

magia = int(input("Quantos pontos de magia? "))

if classe == "guerreiro":
    valido = (força >= 15) and (magia <= 10)

elif classe == "mago":
    valido = (força <= 10) and (magia >= 15)

elif classe == "arqueiro":
    valido = (15 <= força <= 5) and (15 <= magia <=5)

else:
    valido = False 

print (f"Pontos de atributo consistentes com a classe escolhida {valido}")

