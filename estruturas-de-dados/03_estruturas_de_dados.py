#================================================
#Dicionarios
#================================================

#Tuplas()
#Listas[]
#Dicionarios {}

dados1 = list()

dados1.append('Pedro')
dados1.append(25)
print(dados1) #['Pedro', 25]

dados = {'nome': 'Pedro', 'idade':25}
print(dados)
dados['sexo'] = 'M'

filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
         }

print(filme.values()) #dict_values(['Star Wars', 1977, 'George Lucas'])
print(filme.keys())#dict_keys(['titulo', 'ano', 'diretor'])

for k, v in filme.items():
    print(f'O {k} é {v}') #O titulo é Star Wars O ano é 1977O diretor é George Lucas

locadora = []
print('\nInsira os comandos para criar uma LOCADORA')
for i in range(3):
    filme = {
        "titulo": input("Título: "),
        "ano": int(input("Ano: ")),
        "diretor": input("Diretor: ")
    }

    locadora.append(filme)

for i, filme in enumerate(locadora):
    print(f"\nFilme {i+1}:")
    print(f"Título: {filme['titulo']}")
    print(f"Ano: {filme['ano']}")
    print(f"Diretor: {filme['diretor']}")
