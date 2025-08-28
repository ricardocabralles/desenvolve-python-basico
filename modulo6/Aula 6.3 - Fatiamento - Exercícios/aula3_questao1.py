"""
Escreva um script em Python que solicita do usuário uma quantidade
indefinida de números inteiros (com pelo menos 4 valores), os armazena
em uma lista e, usando fatiamento de listas, imprima:

A lista original

Os 3 primeiros elementos

Os 2 últimos elementos

A lista invertida (do fim para o começo)

Os elementos de índice par (0, 2, 4 … )

Os elementos de índice ímpar (1, 3, 5, … )"""

import random
lista=[]
numero=0
quant=int(input("Digite uma quantidade de numeros para uma lista - a menor quantidade possivel é 4"))

if quant<4:
        print("A quantidade mínima é 4. Usando 4 como valor padrão.")
        quant=4
for i in range(quant):
    numero=int(input(f"Digite o numero corespondente a posição{i+1}"))
    lista.append(numero)

print(lista)
print(lista[0:3])
print(lista[-2:])
print(lista[::-1])
print(lista[::2])
print(lista[1:quant:2])
