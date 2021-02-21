#Faça um programa que receba a quantidade de dinheiro em reais que uma pessoa que vai viajar possui.
#Essa pessoa vai passar por vários países e precisa converter seu dinheiro em doláres, marco alemão e libra esterlina.
#Sabe-se que a cotação do dólar é de R$ 1,80, do marco alemão é de R$ 2,00 e da libra esterlina é de R$ 1,57.
#O programa deve fazer as conversões e mostrá-las:

cotacaoDolar = 1.80
cotacaoMarcoAlemao = 2.00
cotacaoLibraEsterlina = 1.57

saldoViagemReais = float(input("Entre com a quantidade de dinheiro em reais que possui para a viagem: "))
saldoViagemDolares = saldoViagemReais/cotacaoDolar
saldoViagemMarcoAlemao = saldoViagemReais/cotacaoMarcoAlemao
saldoViagemLibraEsterlina = saldoViagemReais/cotacaoLibraEsterlina

print("Saldo em doláres: {:.2f}\nSaldo em Marco Alemão: {:.2f}\nSaldo Libra Esterlina {:.2f}".format(saldoViagemDolares,saldoViagemMarcoAlemao,saldoViagemLibraEsterlina))
