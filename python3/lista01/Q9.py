#Faça um programa que calcule e mostre a área de um trapézio.
#Sabe-se que: A = ((base maior + base menor)*h)/2
#Receba o valor da base maior do trapézio:
baseMaior = float(input("Entre com o valor da base maior do trapézio: "))
#Receba o valor da base menor do trapézio:
baseMenor = float(input("Entre com o valor da base menor do trapézio: "))
#Receba o valor de altura do trapézio:
altura = float(input("Entre com a altura do trapézio: "))
#Receba o resultado do cálculo da área do trapézio:
areaTrapezio = (baseMaior+baseMenor)*altura/2
#Imprima o resultado contendo o valor da área do trapézio:
print("A área desse trapézio é:",areaTrapezio)