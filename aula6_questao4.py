distancia = float(input("Qual a distância da entrega (km): "))

peso = float(input("Qual o peso do pacote (kg): "))

# Verifica a faixa de distância para definir o preço por kg
if distancia <= 100:
    preco_kg = 1.0
elif distancia <= 300:
    preco_kg = 1.5
else:
    preco_kg = 2.0

frete = preco_kg * peso

# Verifica se o peso é superior a 10 kg para adicionar a taxa extra
if peso > 10:
    frete = frete + 10

# Imprime o valor total do frete com duas casas decimais
print(f"Valor do frete: R${frete:.2f}")