#Calcular o dobro, triplo e raiz quadrada do número inserido
import math

while True:
    try:
        n1=float(input('Insira um número: '))

        if n1 < 0:
            print('Insira um número não negativo!')
            continue

        break

    except ValueError:
        print('\nDADO INVÁLIDO!')
        print('Por favor, insira apenas números')


if n1.is_integer():
    n1 = int(n1)

dobro = round(2*n1,len(str((n1))))
triplo = round(3*n1, len(str((n1))))


raiz = math.sqrt(n1)

if raiz.is_integer():
    raiz = int(raiz)
else:
    raiz = round(raiz,3)

print('O dobro do número {} é {}, o seu triplo é {} e a sua raiz quadrada é {}'.format(n1, dobro, triplo, raiz))
