#Faça um programa que receba uma temperatura em Celsius,
#calcule e mostre essa temperatura em Fahrenheit. Sabe-se que F = 180(C+32)/100

#Receba o valor da temperatura na escala Celsius:
temperaturaCelsius = float(input("Entre com o valor da temperatura em Celsius: "))
#Receba o resultado do cálculo de conversão de Celsius para a escala Fahrenheit:
temperaturaFahrenheit = 180*(temperaturaCelsius+32)/100
#Imprima o valor da temperatura equivalente em Fahrenheit:
print("A temperatura equivalente em Fahrenheit é:",temperaturaFahrenheit)