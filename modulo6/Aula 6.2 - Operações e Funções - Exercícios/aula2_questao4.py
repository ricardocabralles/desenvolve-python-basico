"""Crie um programa em Python que receba duas listas de números
do usuário, podendo cada lista ter uma quantidade diferente de
valores. Em seguida, combine essas duas listas de forma alternada
para formar uma terceira lista. Intercale os elementos até o final
da primeira lista, adicionando ao final os elementos remanescentes
da maior lista.

Exemplo de interação via terminal (entradas em laranja): 

Digite a quantidade de elementos da lista 1: 4

Digite os 4 elementos da lista 1:

1

2

3

4

Digite a quantidade de elementos da lista 2: 6

Digite os 6 elementos da lista 2:

5

6

7

8

9

10

Lista intercalada: 1 5 2 6 3 7 4 8 9 10"""

qtd1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []

print(f"Digite os {qtd1} elementos da lista 1:")
for _ in range(qtd1):
    valor = int(input())
    lista1.append(valor)


qtd2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = []

print(f"Digite os {qtd2} elementos da lista 2:")
for _ in range(qtd2):
    valor = int(input())
    lista2.append(valor)


lista_intercalada = []


for i in range(min(qtd1, qtd2)):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])


if qtd1 > qtd2:
    lista_intercalada.extend(lista1[qtd2:])
else:
    lista_intercalada.extend(lista2[qtd1:])

print(lista1)
print(lista2)
print("\nLista intercalada:", *lista_intercalada)
 