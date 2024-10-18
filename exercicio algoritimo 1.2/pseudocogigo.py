n = input ("Qual o numero a ser multiplicado por 9?" )

digito_1 = float(n) - 1
digito_2 = 10 - float(n)

numero_final = float(digito_1) * 10 + float(digito_2)



print (f"O resultado de 9 multiplicado por {n} é igual a {numero_final}") 