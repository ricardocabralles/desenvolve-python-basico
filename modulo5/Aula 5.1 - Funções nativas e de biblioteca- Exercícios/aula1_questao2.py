"""Escreva um código que gere n valores inteiros aleatórios entre
 0 e 100 e calcule a raíz quadrada da soma dos valores. Peça ao 
 usuário o valor de n

Biblioteca random: Função randint()

Biblioteca math:  Função sqrt()"""

import random
import math
soma=0

n=int(input("Digite uma quantidade de numeros(n) para serem gerados aleatoriamente:"))

for i in range(n):
    valor=random.randint(0,100)
    print(valor)
    soma+=valor
    

raiz=math.sqrt(soma)

print(f"A soma dos valorese aleatórios é igual a {soma}")
print(f"A raiz quadrada da soma é igual a {round(raiz,2)}")