#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
from math import pi
raio = float(input('Informe o Valor do Raio : '))
area = pi * (raio**2)
print("O valor da Area é {:.1f} ".format(area))