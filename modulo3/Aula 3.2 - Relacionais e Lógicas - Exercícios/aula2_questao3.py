"""
Você está desenvolvendo um sistema de admissão para um clube 
juvenil de jogos de tabuleiro. Escreva um programa em Python que 
pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de 
tabuleiro (resposta deve ser True ou False) e quantas vezes venceu 
um jogo. O programa deve imprimir True se o participante tiver entre
16 e 18 anos, já tiver jogado pelo menos 3 jogos e já ter vencido 
pelo menos 1 jogo, permitindo seu ingresso no clube. Sua expressão
deve imprimir False caso contrário. Aqui está um exemplo de 
interação com seu código no terminal, com entradas de dados 
destacadas em laranja e as impressões de seu código em branco.

Terminal

Digite sua idade: 17

Já jogou pelo menos 3 jogos de tabuleiro? True

Quantos jogos já venceu? 2

Apto para ingressar no clube de jogos de tabuleiro: True"""

idade=int(input("Digite sua idade:"))

idade=(idade>=16 and idade<=18)

quantjogos=int(input("Já jogou quantos jogos de tabuleiro?"))

quantjogos=(quantjogos>=3)

vence=int(input("Quantos jogos já venceu?"))

vence=(vence>=1)

chave=(idade and quantjogos and vence)
print("apto para ingressar no clube de jogos de tabuleiro: ", chave )