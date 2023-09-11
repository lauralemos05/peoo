print('Informe o valor da prestação:')
valor = float(input())
print('Informe a taxa de juros:')
taxa = float(input())
print('Informe o tempo de atraso:')
tempo = float(input())

p = valor + (valor*(taxa/100))*tempo

print('O valor a pagar é',p)
