#Faça um programa que receba a medida de dois ângulos de um triângulo,
#calcule e mostre a medida do terceiro ângulo. Sabe-se que a soma dos ângulos de um triângulo é 180.

#Receba o valor do 1º ângulo do triângulo em graus:
angulo1 = int(input("Entre com o valor do 1º ângulo do triângulo em graus: "))
#Receba o valor do 2º ângulo do triângulo em graus:
angulo2 = int(input("Entre com o valor do 2º ângulo do triângulo em graus: "))
#Receba o valor do cálculo para o ângulo 3:
angulo3 = 180-(angulo1+angulo2)
#Imprima o valor do 3º ângulo procurado:
print("O terceiro ângulo tem o valor de {} graus".format(angulo3))