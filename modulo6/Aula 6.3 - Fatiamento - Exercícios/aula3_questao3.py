"""
Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. Em seguida encontre o
intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del.
Você deve imprimir a lista antes e depois da deleção.

Original: [9, 2, -1, 4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6]

Editada:  [9, 2, -1, 4, -2, -3, 5, 6, 6, 8, -3, -6]"""

import random
lista=[]
iniciofatia, tamanhofatia= -1,0
iniciomaiorf, tamanhomaiorf= -1,0
for i in range(20):
    lista.append(random.randint(-10,10))

print(lista)

for i in range(20):
    if lista[i]<0:
        tamanhofatia+=1
        if tamanhofatia==1:
            print(f"iniciando nova fatia. Inicio: {tamanhofatia}")
            iniciofatia=i
        
    else:
        if tamanhofatia>tamanhomaiorf:
            print(f"maior fatia ate agora {tamanhofatia}")
            tamanhomaiorf = tamanhofatia
            iniciomaiorf=iniciofatia
        tamanhofatia=0
    if tamanhofatia>tamanhomaiorf:
                tamanhomaiorf=tamanhofatia
                iniciomaiorf=iniciofatia
    

print(f"quantidade de numeros na maior fatia {tamanhomaiorf}, indice do primeiro numero da maior fatia {iniciomaiorf}")

del lista[iniciomaiorf: iniciomaiorf+tamanhomaiorf]

print(lista)