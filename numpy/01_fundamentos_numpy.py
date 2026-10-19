# 1. CRIAÇÃO DE ARRAYS — np.array()

#possuem o mesmo tipo de dado.
import numpy as np

#array a partir de uma lista:
numeros = np.array([10, 20, 30, 40, 50])
print(numeros)

#arrays de strings:
nomes = np.array(["Ana", "Carlos", "Maria"])
print("\nNomes:", nomes)

# array tipo matriz:
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nMatriz:", matriz)


# O NumPy pode converter automaticamente os elementos.

array_misto = np.array([10, 20.5, 30])
print("Array convertido:", array_misto)

# ------------------------------------------------------------
# DIFERENÇA NAS OPERAÇÕES MATEMÁTICAS
# ------------------------------------------------------------

lista = [1, 2, 3]
array = np.array([1, 2, 3])


print("\nLista * 2:", lista * 2)
# Resultado: [1, 2, 3, 1, 2, 3]

print("Array * 2:", array * 2)
# Resultado: [2 4 6]

print("Array + 10:", array + 10)
# Resultado: [11 12 13]

print("Array ** 2:", array ** 2)
# Resultado: [1 4 9]

print("Média:", np.mean(array))
# Resultado: 2.0


# ============================================================
# 2. DIMENSÕES — ndim, shape, size
# ============================================================

matriz = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

# ndim informa o número de dimensões do array. 
print("\nNúmero de dimensões:", matriz.ndim)
# Resultado: 2

# shape informa o formato do array -> 2 linhas e 3 colunas.
print("Formato:", matriz.shape)
# Resultado: (2, 3)

# size informa a quantidade TOTAL de elementos -> 6
print("Quantidade de elementos:", matriz.size)


# ============================================================
# 3. TIPOS DE DADOS — dtype E astype()
# ============================================================

# dtype: tipo de dado armazenado no array.

inteiros = np.array([1, 2, 3, 4])
decimais = np.array([1.5, 2.5, 3.5])
booleanos = np.array([True, False, True])

print("\nTipo dos inteiros:", inteiros.dtype) #resultado: Tipo dos inteiros: int64
print("Tipo dos decimais:", decimais.dtype) #resultado: Tipo dos inteiros: float64
print("Tipo dos booleanos:", booleanos.dtype) #resultado: Tipo dos inteiros: bool

# Tipos comuns:
# int32 / int64   -> números inteiros
# float32/float64 -> números decimais
# bool            -> verdadeiro ou falso
# <U...           -> strings Unicode


# ------------------------------------------------------------
# CONVERSÃO DE TIPOS — astype()
# ------------------------------------------------------------

# astype() cria um array com os dados convertidos para o tipo especificado.

notas = np.array([7.5, 8.9, 6.3])

print("\nNotas originais:", notas)

#decimais para inteiros:
notas_inteiras = notas.astype(int)

print("Notas convertidas:", notas_inteiras) #resultado: [7 8 6] (PS: Descarta a parte decimial)


#inteiros para decimais:
valores = np.array([10, 20, 30])
valores_float = valores.astype(float)

print("Valores float:", valores_float) #resultado: [10. 20. 30.]



#tipo na criação:
idades = np.array([20, 25, 30], dtype=np.float64)

print("Idades:", idades)
print("Tipo:", idades.dtype)


# ============================================================
# 4. FUNÇÕES DE CRIAÇÃO DE ARRAYS
# zeros(), ones(), full(), arange(), linspace()
# ============================================================


#4.1 np.zeros() -> array preenchido com zeros.

zeros = np.zeros(5)

print("\nArray de zeros:", zeros) #resultado: [0. 0. 0. 0. 0.]


#matriz de zeros:
matriz_zeros = np.zeros((2, 3))

print("\nMatriz de zeros:")
print(matriz_zeros)



# ------------------------------------------------------------
# 4.2 np.ones() -> array preenchido com 1
# ------------------------------------------------------------

uns = np.ones(4)

print("\nArray de uns:", uns) #resultado: [1. 1. 1. 1.]

# matriz 3x2 preenchida com 1:
matriz_uns = np.ones((3, 2))

print("\nMatriz de uns:")
print(matriz_uns)


# ------------------------------------------------------------
# 4.3 np.full() -> array preenchido com um valor escolhido
# np.full(formato, valor)
# ------------------------------------------------------------
cincos = np.full(5, 5)

print("\nArray preenchido com 5:", cincos) #resultado: [5 5 5 5 5]

# matriz de 2x3 preenchida com 10:
matriz_dez = np.full((2, 3), 10)

print("\nMatriz preenchida com 10:")
print(matriz_dez)

# ------------------------------------------------------------
# 4.4 np.arange() -> sequência de números com um intervalo definido.
# np.arange(inicio, fim, passo) -> o valor final não é incluído.
# ------------------------------------------------------------
seq = np.arange(0, 10)

print("\nSequência:", seq) #resultado: [0 1 2 3 4 5 6 7 8 9]

# numeros pares entre 0 e 10:
pares = np.arange(0, 11, 2)

print("Números pares:", pares) #resultado: [0 2 4 6 8 10]

multiplos = np.arange(5, 26, 5)

# ------------------------------------------------------------
# 4.5 np.linspace()
# quantidade definida de valores igualmente espaçados entre dois números, início e fim incluídos
# np.linspace(inicio, fim, quantidade)
# ------------------------------------------------------------
pontos = np.linspace(0, 10, 5)

print("\nPontos igualmente espaçados:", pontos) #resultado: [0. 2.5 5. 7.5 10.] -> passo(5) = (final(10)-inicial(0))/(quantidade(5)-1) = 2.5

# Criando 11 valores entre 0 e 1:
probabilidades = np.linspace(0, 1, 11) #resultado: [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ]

print("Probabilidades:", probabilidades)


# ============================================================
# 5. ESTATÍSTICA
# ============================================================

notas = np.array([7.5, 8.0, 6.5, 9.0, 7.0])

print("\n===== ANÁLISE DAS NOTAS =====")

# Quantidade de estudantes:
print("Quantidade:", notas.size)

# Média:
print("Média:", np.mean(notas))

# Mediana:
print("Mediana:", np.median(notas))

# Desvio padrão populacional:
print("Desvio padrão populacional:", np.std(notas))

# Desvio padrão amostral:
print("Desvio padrão amostral:", np.std(notas, ddof=1))

# Menor nota:
print("Mínimo:", np.min(notas))

# Maior nota:
print("Máximo:", np.max(notas))

# Soma das notas:
print("Soma:", np.sum(notas))
