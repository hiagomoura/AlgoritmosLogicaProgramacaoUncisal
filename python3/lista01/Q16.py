#Faça um programa que receba o valor dos catetos de um triângulo,
#calcule e mostre o valor da hipotenusa.

import math
#Receba o valor do catetoA:
catetoA = int(input("Entre com o valor do cateto A: "))
#Receba o valor do catetoB:
catetoB = int(input("Entre com o valor do cateto B: "))
#Cálcule o valor da hipotenusa (Teorema de Pitágoras: a²=b²+c²):
hipotenusa =  int(math.sqrt(math.pow(catetoA,2) + math.pow(catetoB,2)))
#Imprima o valor da hipotenusa:
print("O valor da hipotenusa é:",hipotenusa)