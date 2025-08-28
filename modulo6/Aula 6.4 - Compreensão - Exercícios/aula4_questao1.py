"""Escreva um script python que use compreensão de listas para criar as seguintes listas:

Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]

Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]

Todos os números entre 1 e 100 que sejam divisíveis por 7

Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento
 (ex:['par', 'impar',… , 'impar']) """


pares=0
lista=[1,2,3,4,5,6,7,8,9]
lista7=0
quadrado=0
verifica=0
lista30=0
lista20=0
lista1=0

pares=[n for n in range(20,51) if n%2==0]
lista20=[n for n in range(20,51)]
print("Lista inicial")
print(lista20)
print("Numeros pares da lista inicial")
print(pares)
print()
print("Nova lista inicial")
print(lista)
quadrado=[n**2 for n in lista]
print("Elementos da nova lista inicial ao quadrado")
print(quadrado)
print()
lista1=[n for n in range(1,101)]
print("Nova lista inicial")
print(lista1)
lista7=[n for n in range(1,101) if n%7==0]
print("Apenas os numeros diviziveis por 7 da lista inicial")
print(lista7)
print()
lista30=[n for n in range(0,30,3)]
verifica=["par" if n%2==0 else "impar" for n in range(0,30,3)]
print("Nova lista inicial")
print(lista30)
print("Indicação se os numeros presentes na lista são pares ou impares")
print(verifica)