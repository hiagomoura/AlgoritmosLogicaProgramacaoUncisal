#Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
# a) a idade dessa pessoa em anos;
# b) a idade dessa pessoa em meses
# c) a idade dessa pessoa em dias
# d) a idade dessa pessoa em semanas

#Receba o ano de nascimento da pessoa:
anoNascimento = int(input("Entre com o ano de nascimento da pessoa: "))
#Receba o ano atual:
anoAtual = int(input("Entre com o ano atual: "))
#Receba o resultado do cálculo da idade em anos da pessoa:
idadeEmAnos = anoAtual - anoNascimento
#Receba o resultado do cálculo da idade em meses da pessoa:
idadeEmMeses = idadeEmAnos*12
#Receba o resultado do cálculo da idade da pessoa em dias:
idadeEmDias = idadeEmMeses*30
#Receba o resultado do cálculo da idade em semanas:
idadeEmSemanas = idadeEmMeses*4