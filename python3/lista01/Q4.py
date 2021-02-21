#Faça um programa que receba duas notas, calcule e mostre a média ponderada dessas notas, considerando peso 2 para a primeira nota e peso 3 para a segunda nota.

#Declarando o peso 1
peso1 = 2
#Declarando o peso 2
peso2 = 3
#Receba o 1ª número:
numero1 = float(input("Entre com o 1º número: "))
#Receba o 2ª número:
numero2 = float(input("Entre com o com o 2º número: "))
#Receba a média ponderada do 1º e 2º número:
mediaPonderada = (numero1*peso1+numero2*peso2)/(peso1+peso2)
#Imprima a média ponderada
print("A média ponderada é:",mediaPonderada)



