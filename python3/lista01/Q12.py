#Faça um programa que receba o valor do salário mínimo e o valor do salário de um funcionário,
#calcule e mostre a quantidade de salários mínimos que ganha esse funcionário.

#Receba o valor do salário mínimo:
salarioMinimo = float(input("Entre com o valor do salário mínimo: "))
#Receba o valor do salário do funcionário:
salarioFuncionario = float(input("Entre com o valor do salário do funcionário: "))
#Imprima o valor de quantos salários mínimos ganha esse funcionário:
print("O funcionário ganha: {:.2f} salários mínimos".format(salarioFuncionario/salarioMinimo))

