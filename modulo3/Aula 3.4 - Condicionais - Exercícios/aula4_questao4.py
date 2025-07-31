"""Você está implementando um sistema de entrega expressa e precisa
calcular o valor do frete com base na distância e no peso do pacote.
Escreva um código que solicita a distância da entrega em 
quilômetros e o peso do pacote em quilogramas. O programa deve 
calcular e imprimir o valor do frete de acordo com as seguintes 

regras:

Distância até 100 km: R$1 por kg.
Distância entre 101 e 300 km: R$1.50 por kg.
Distância acima de 300 km: R$2 por kg.
Acrescente uma taxa de R$10 para pacotes com peso superior
a 10 kg
"""

distancia=int(input("digite a distancia do frete em Km"))
peso=int(input("digite o peso da encomenda em Kg"))

if(distancia<=100):
    if(peso>10):
        frete=(peso*1)+10
    else:
        frete=(peso*1)
if(101<=distancia<=300):
    if(peso>10):
        frete=(peso*1.5)+10
    else:
        frete=(peso*1.5)
if(distancia>=300):
    if(peso>10):
        frete=(peso*2)+10
    else:
        frete=(peso*2)       

print(f"O valor do frete é de: R$ {frete:.2f}")