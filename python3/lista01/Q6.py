#Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas.
#Faça um programa que receba o salário fixo de um funcionário e o valor de suas vendas,
#calcule e mostre a comissão e o salário final do funcionário.

percentualComissao = 4
salarioFixo = float(input("Entre com o valor do salário fixo do funcionário: "))
valorVenda = float(input("Entre com o valor das vendas: "))
valorComissao = percentualComissao/100*valorVenda
salarioComissao = salarioFixo+valorComissao
print("O valor da comissão é de: {:.2f} R$, e o valor do salário com comissão é: {:.2f} R$".format(valorComissao,salarioComissao))