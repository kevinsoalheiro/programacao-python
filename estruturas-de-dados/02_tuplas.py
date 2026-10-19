#Tuplas
# é uma espécie de lista IMUTÁVEL feita com ()

pessoa = ("Kelly", 26, 1.65, True)
nome, idade, altura, booleano = pessoa
print(pessoa)
print(nome)
print('\nEsse é o indíce 0 da tupla: ', pessoa[0],
      '\nEsse é o indíce 1 da tupla: ', pessoa[3],
      '\nEsse é o tamanho da tuplas: ', len(pessoa))

numeros = (10, 20, 30, 40, 50)
print(numeros[:3])   # (10, 20, 30)
print(numeros[::-2]) # (50, 40, 30, 20, 10)
#A sintaxe é tupla[início:fim:passo]. O índice fim não é incluído.

#count(x) -> Conta quantas vezes x aparece
#index(x) -> Retorna o índice da primeira ocorrência de x
#len() -> Retorna o número de elementos
#min() -> Retorna o menor valor
#max() -> Retorna o maior valor
#sum() -> Soma os elementos numéricos
#sorted() -> Retorna uma lista ordenada

