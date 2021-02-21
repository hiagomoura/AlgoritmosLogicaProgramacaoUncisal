#Faça um programa que receba um hora (uma variável para hora e outra para minutos), calcule e mostre:
# a) A hora digitada convertida em minutos;
# b) O total dos minutos, ou seja, os minutos digitados mais a conversão anterior;
# c) O total dos minutos convertidos em segundos.

#Receba o valor da quantidade de horas:
hora = int(input("Entre com a hora: "))
#Receba o valor da quantidade de minutos:
minutos = int(input("Entre com os minutos: "))
#Imprima o valor equivalente em minutos da quantidade de horas digitada, o total de minutos, e o total de minutos em termos de segundos:
print("O valor equivalente em minutos da quantidade de horas digitada é {}\nO total de minutos é de: {}\nO total de minutos em segundos é de: {}".format(hora*60,minutos+hora*60,(minutos+hora*60)*60))