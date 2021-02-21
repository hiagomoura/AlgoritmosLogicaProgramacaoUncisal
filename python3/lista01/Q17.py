#Faça um programa que receba o raio, calcule e mostre:
# a) O comprimento de uma esfera, sabe-se que C = 2*PI*R;
# b) A área de uma esfera, sabe0se que A = PI*R²;
# c) O volume de uma esfera, sabe-se que V = 3/4*PI*R³

import math

#Receba o valor do raio:
raio = float(input("Entre com o valor do raio: "))
#Receba o resultado do cálculo do comprimento da Esfera:
comprimentoEsfera = 2*math.pi*raio
#Receba o resultado do cálculo da área da esfera:
areaEsfera = math.pi*math.pow(raio,2)
#Receba o resultado do cálculo do volume da esfera:
volumeEsfera = 3/4*math.pi*math.pow(raio,3)
#Imprima o resultado dos cálculos do comprimento, área e volume da esfera:
print("Comprimento da Esfera é: {:.2f}\nÁrea da Esfera: {:.2f}\nVolume da Esfera: {:.2f}".format(comprimentoEsfera,areaEsfera,volumeEsfera))

