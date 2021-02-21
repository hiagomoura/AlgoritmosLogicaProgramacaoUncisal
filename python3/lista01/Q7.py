#Faça um programa que receba o peso de uma pessoa, calcule e mostre:
# a) O novo peso se a pessoa engordar 15% sobre o peso digitado;
# b) O novo peso se a pessoa emagrecer 20% sobre o peso digitado.

pesoPessoa = float(input("Entre com o peso da pessoa: "))
print("O novo peso ao engordar 15% desse peso é: {:.2f} e o novo peso caso venha a emagrecer 20% desse peso é: {:.2f} ".format(pesoPessoa*0.15+pesoPessoa,pesoPessoa-pesoPessoa*0.20))

