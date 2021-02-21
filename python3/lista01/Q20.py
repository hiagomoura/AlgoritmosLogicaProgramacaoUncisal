#Faça um programa que receba a medida do ângulo formado por uma escada apoiada no chão e a distância que a escada está da parede.
#Calcule e mostre a medida da escada para que se possa alcançar a ponta da escada.

from math import radians, cos

#Receba o valor do ângulo em graus entre a escada e o chão:
anguloEscada = float(input("Entre com o ângulo em graus entre a escada e o chão: "))
#Convertendo ângulo para seu valor em radianos:
anguloEscada = radians(anguloEscada)
#Receba o valor da distâcia da escada até a parede:
distanciaEscadaParede = float(input("Entre com a distância da escada até a parede: "))
#Receba o valor do cálculo da medida da escada (hipotenusa) usando relação trigonométrica (COS):
medidaEscada = distanciaEscadaParede/cos(anguloEscada)
#Imprima o valor da medida da escada:
print("A medida da escada é: {:.2f}".format(medidaEscada))