#Faça um programa que receba o número de horas trabalhadas, o valor do slário mínimo e o número de horas extras trabalhadas.
#Calcule e mostre o salário a receber seguindo as regras a seguir:
# a) A hora trabalhada vale 1/8 do salário mínimo;
# b) A hora extra vale 1/4 do salário mínimo;
# c) O salário bruto equivale ao número de horas trabalhadas multiplicadas pelo valor da hora trabalhada;
# d) A quantia a receber pelas hora extras equivale ao número de horas extradas trabalhadas multiplicado pelo valor da hora extra;
# e) O salário a receber equivale ao salário bruto mais a quantia a receber pelas horas extras.

#Receba o valor das horas trabalhadas:
horasTrabalhadas = float(input("Entre com as horas trabalhadas: "))
#Enquanto o valor de entrada de horas trabalhadas for negativo, repita o input do valor:
while horasTrabalhadas<0:
    horasTrabalhadas = float(input("Entre com um número positivo, não existe tempo negativo.\nEntre com as horas trabalhadas: "))
#Receba o valor do salário mínimo:        
valorSalarioMinimo = float(input("Entre com o salário mínimo: "))
#Enquanto o valor do salário mínimo for negativo, repita o input do valor:
while valorSalarioMinimo<0:
    valorSalarioMinimo = float(input("O valor do salário deve ser positivo.\nEntre com o salário mínimo: "))
#Receba o valor das horas extras trabalhadas:
horasExtras = float(input("Entre com as horas extras: "))
while horasExtras<0:
    horasExtras = float(input("Entre com um número positivo, não existe tempo negativo.\nEntre com as horas extras: "))
#Receba o valor da hora trabalhada:
valorHoraTrabalhada = 1/8*valorSalarioMinimo
#Receba o valor da hora extra:
valorHoraExtra = 1/4*valorSalarioMinimo
# Receba o valor do salário bruto:
valorSalarioBruto = valorHoraTrabalhada*horasTrabalhadas
# Receba o valor do salário da hora extra:
valorSalarioHoraExtra = valorHoraExtra*horasExtras
#Receba o valor do salário a receber:
valorSalarioFinalReceber = valorSalarioBruto+valorSalarioHoraExtra
#Imprima o valor do salário a receber:
print("O valor do salário a receber é de: {:.2f} R$".format(valorSalarioFinalReceber))
    