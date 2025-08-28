"""Solicite uma frase do usuário e usando compreensão de listas imprima:

A lista de vogais da frase, ordenada alfabeticamente

A lista de consoantes da frase (remova espaços em branco)

Digite uma frase: Eu gosto de programar em Python

Vogais: ['a', 'a', 'e', 'e', 'o', 'o', 'o', 'o', 'u']

Consoantes: ['E', 'g', 's', 't', 'd', 'p', 'r', 'g', 'r', 'm', 'r', 'm', 'P', 'y', 't', 'h', 'n']"""

frase=str(input("Digite uma frase:"))

vogais = sorted([letra for letra in frase.lower() if letra in "aeiou"])
print(f"Vogais: {vogais}")

# A lista de consoantes da frase
consoantes = sorted([letra for letra in frase if letra.lower() not in "aeiou" and letra.isalpha()])
print(f"Consoantes: {consoantes}")

