#João recebeu seu salário e precisa pagar duas contas que estão atrasadas.
#Como as contas estão atrasadas, João terá de pagar multa de 2% sobre cada conta.
#Faça um programa que calcule e mostre quando restará do salário do João.

from math import fabs

percentualMulta = 0.02
salarioJoao = float(input("Entre com o valor do salário do João: "))
valorConta1 = float(input("Entre com o valor da 1ª conta a ser paga sem considerar os juros: "))
valorConta2 = float(input("Entre com o valor da 2ª conta a ser paga sem considerar os juros: "))

#Calculando a valor da conta com multa:
valorConta1 += valorConta1*percentualMulta
valorConta2 += valorConta2*percentualMulta
valorTotalContasComMulta = valorConta1+valorConta2
#Calcule quanto restou do salário de João após pagar as duas contas:
if(valorTotalContasComMulta > salarioJoao):
    print("Não é possível efetuar o pagamento, o valor das contas excede o salário de João em R$ {}".format(fabs(salarioJoao-valorTotalContasComMulta)))
else:
    print("O salário restante de João é:",salarioJoao-valorTotalContasComMulta)
