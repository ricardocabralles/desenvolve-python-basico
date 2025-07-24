"""
1 - Faça um programa para ler as dimensões de um terreno em inteiros 
(comprimento e largura), bem como o preço do metro quadrado da região
em ponto flutuante. Calcule o valor do terreno e imprima o resultado 
como mostra o exemplo a seguir:

O terreno possui 250m2 e custa R$512,490.50

Comente na linha acima de cada instrução uma breve descrição da instrução.
Fórmulas:
area_m2 = comprimento * largura

preco_total = preco_m2 * area_m2
"""

comprimento = int(input("Digite o comprimento do terreno (em metros): ")) #entrada do valor do comprimento do terreno

largura = int(input("Digite a largura do terreno (em metros): ")) #entrada do valor da largura do terreno

preco_m2 = float(input("Digite o preço do m2 do terreno: ")) #entrada do valor do preço m2 do terreno

area_m2= float(comprimento)*float(largura) #calculo da area em metros quadrado a partir da multiplicação do cumprimento pela largura.

preco_total = preco_m2 * area_m2 #calcula o preço total do terreno a partir da multiplicação do preço do metro quadrado pela area.


print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")#imprime a saida conforme solicitado no enunciado

