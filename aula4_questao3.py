# Solicita o nome do produto 1
nome1 = input("Digite o nome do produto 1:")

# Solicita o preço unitário do produto 1
preco1 = float(input("Digite o preço unitário do produto 1:"))

# Solicita a quantidade do produto 1
quantidade1 = int(input("Digite a quantidade do produto 1:"))

# Calcula o total do produto 1
total1 = preco1 * quantidade1

# Solicita o nome do produto 2
nome2 = input("Digite o nome do produto 2:")

# Solicita o preço unitário do produto 2
preco2 = float(input("Digite o preço unitário do produto 2:"))

# Solicita a quantidade do produto 2
quantidade2 = int(input("Digite a quantidade do produto 2:"))

# Calcula o total do produto 2
total2 = preco2 * quantidade2

# Solicita o nome do produto 3
nome3 = input("Digite o nome do produto 3:")

# Solicita o preço unitário do produto 3
preco3 = float(input("Digite o preço unitário do produto 3:"))

# Solicita a quantidade do produto 3
quantidade3 = int(input("Digite a quantidade do produto 3:"))

# Calcula o total do produto 3
total3 = preco3 * quantidade3

# Calcula o total geral da compra
total_compra = total1 + total2 + total3

# Imprime o total formatado com separador de milhar e duas casas decimais
print(f"Total: R${total_compra:,.2f}")