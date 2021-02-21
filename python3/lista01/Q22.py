#Faça um programa que receba o número de lados de um polígono convexo,
#calcule e mostre o número de diagonais desse polígono. Onde N é o número de lados do polígono.
#Sabe-se que ND = N(N-3)/2.

#Receba o número de lados do polígono convexo:
numeroLadosPoligonoConvexo = int(input("Entre com o número de lados do polígono convexo: "))
#Receba o valor do número de diagonais do polígono convexo:
numeroDiagonaisPoligonoConvexo = numeroLadosPoligonoConvexo*(numeroLadosPoligonoConvexo-3)/2
#Imprima o o número de diagonais do polígono convexo:
print("Esse polígono tem {} diagonais".format(numeroDiagonaisPoligonoConvexo))