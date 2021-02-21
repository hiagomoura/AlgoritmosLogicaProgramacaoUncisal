#Faça um programa que calcule e mostre a tabuada de um número digitado pelo usuário
#Receba o número para cálculo da tabuada
numero = int(input("Entre com o número que deseja exibir a tabuada: "))
#Itere de 0 a 10 multiplicando o número de entrada digitado
for n in range(0,11):
    print("{} x {} = {} ".format(n,numero,n*numero))