#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
media = 0
for i in range(1,5):
    n1 = float(input(f'Digite a nota {i} :'))
    media = media + n1
print("media das notas é  :", (media/4))