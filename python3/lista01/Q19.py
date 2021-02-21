#Sabe-se que para iluminar de maneira correta os cômodos de uma casa, para cada m²,
#deve-se usar 18W de potência. Faça um programa que receba as duas dimensões de um cômodo (em metros),
#calcule e mostre a sua área (em m²) e potência de iluminação que deverá ser utilizada.

#Receba o valor do comprimento do cômodo em metros:
comprimentoComodo = float(input("Entre com o valor do comprimento do cômodo em metros: "))
#Receba o valor da largura do cômodo em metros:
larguraComodo = float(input("Entre com o valor da largura do cômodo em metros: "))
#Receba o valor do comprimento do cômodo em metros:
areaComodo = comprimentoComodo*larguraComodo
#Receba o resultado do cálculo da potência para a área calculada:
potenciaIluminacao = areaComodo*18
#Imprima a área do cômodo e potência necessária para iluminá-lo:
print("A área do cômodo é de {} m²\nPotência para iluminá-lo deve ser de: {} W de potência.".format(areaComodo,potenciaIluminacao))