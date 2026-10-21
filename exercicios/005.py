while True:
    try:
        n1 = int(input('Insira um numero inteiro: '))
        break

    except:
        print('\nDADO INVÁLIDO!')
        print('\nPor favor, insira um número inteiro: \n')

print('{} é o antecessor de {} e {} é o seu sucessor'.format(n1, n1-1, n1+1))
