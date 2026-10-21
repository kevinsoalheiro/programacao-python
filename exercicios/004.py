dado = input('Insira um dado: ')
print('\nO dado inserido é:'\
      '\nAlfanumerico? {}'.format(dado.isalpha()),\
        '\nÉ alfabético? {}'.format(dado.isalpha()),\
        '\nNumérico? {}'.format(dado.isnumeric()),\
        '\nMaiscula? {}'.format(dado.isupper()),\
        '\nMinuscula? {}'.format(dado.islower()),\
        '\nSó tem espaços? {}'.format(dado.isspace()))
