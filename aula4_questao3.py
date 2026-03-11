#Primeiro será digitado o produto, em seguida o preço unitario do mesmo,
# após isso será digitando a quantidade

# Dite o nome do produto 1
Nome1 = input("Digite o nome do produto 1:")

# Dite o preço unitário do produto 1
Preço1 = float(input("Digite o preço unitário do produto 1:"))

# Dite a quantidade do produto 1
Quantidade1 = int(input("Digite a quantidade do produto 1:"))

# Dite o calculo total do produto 1
Total1 = preco1 * quantidade1

# Dite o nome do produto 2
Nome2 = input("Digite o nome do produto 2:")

# Solicita o preço unitário do produto 2
Preço2 = float(input("Digite o preço unitário do produto 2:"))

# Solicita a quantidade do produto 2
Quantidade2 = int(input("Digite a quantidade do produto 2:"))

# Calcula o total do produto 2
Total2 = preco2 * quantidade2

# Solicita o nome do produto 3
Nome3 = input("Digite o nome do produto 3:")

# Solicita o preço unitário do produto 3
Preco3 = float(input("Digite o preço unitário do produto 3:"))

# Solicita a quantidade do produto 3
Quantidade3 = int(input("Digite a quantidade do produto 3:"))

# Calcula o total do produto 3
Total3 = preco3 * quantidade3

# Calcula o total geral da compra
Total_compra = total1 + total2 + total3

# Imprime o total formatado com separador de milhar e duas casas decimais
print(f"Total: R${total_compra:,.2f}")