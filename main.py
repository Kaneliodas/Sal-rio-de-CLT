#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
Ganha_h = float(input("Quanto você ganha por hora? "))
num_h_mes =float(input("Quantas horas você trabalha no mês? "))
Bruto = Ganha_h*(num_h_mes*30)
impos_r = (11/100) * Bruto
INSS = (8/100) * Bruto
sindicato = (5/100) * Bruto
liqui = Bruto - (impos_r+INSS+sindicato)
print("O valor do seu salário Bruto: " + str(Bruto))
print("O valor do seu  Imposto de Renda: " + str(impos_r))
print("O valor do seu INSS: " + str(INSS))
print("O valor do sindicato: " + str(sindicato))
print("O valor do seu salário líquido : " + str(liqui))
