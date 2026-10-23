import math

entrada = input('Digite um número REAL: ')
numero = float(entrada)

# Identifica a quantidade de casas decimais
casas = len(entrada.split('.')[1]) if '.' in entrada else 0

# Separa a parte inteira e decimal
inteiro = math.trunc(numero)
decimal = round(numero - inteiro, casas)

print('{} corresponde à parte inteira do número'
      '\n{} corresponde à parte decimal do número'.format(inteiro, decimal))
