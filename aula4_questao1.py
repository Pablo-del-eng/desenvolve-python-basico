#dados 
comprimento = int(input("Digite o comprimento do terreno: "))
largura = int(input("Digite a largura do terreno: "))
preço_metro = 500

#Calculos

#Aqui sera calculado a area multiplicando o comprimento pela largura apresentada pelo usuario
area = comprimento * largura 

#Aqui sera calculado o preço do terreno utilizando a area * o preço do metro 
preço_terreno = preço_metro * area

#Saída 
print ("O comprimento do terreno é:")
print (comprimento)
print ("A largura do terreno é:")
print (largura)

print (f"o terreno possui {area}m2 e custa {preço_terreno} reais    ")