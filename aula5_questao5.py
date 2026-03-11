genero = input("Qual o seu genero? (M ou F): ")

idade = int(input("Quantos anos você tem? "))

anos_trabalhados = int(input("Quantos anos você trabalhou? "))

aposentar = ((genero == "M" and idade >= 65) or 
             (genero == "F" and idade >= 60) or
             (anos_trabalhados >= 30) or
             (idade >= 60 and anos_trabalhados >= 25) )

print (aposentar)