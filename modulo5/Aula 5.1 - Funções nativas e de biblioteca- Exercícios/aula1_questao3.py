"""
Escreva um programa em Python que utiliza a biblioteca random
para gerar um número aleatório entre 1 e 10 e peça ao usuário para
adivinhar o número. Forneça feedback se o palpite é muito alto, 
muito baixo ou correto. Interrompa a execução somente quando o 
usuário acertar o palpite.

Exemplo de interação:

Adivinhe o número entre 1 e 10: 5

Muito alto, tente novamente!

Adivinhe o número entre 1 e 10: 3

Correto! O número é 3."""
import random
valor=random.randint(1,10)
palpite=0

while (palpite!=valor):
    palpite=int(input("Foi gerado um valor aleatório de 1 a 10, de um chute de qual numero foi gerado:"))

    if ((palpite>=1) and (palpite<valor)):
        print("Seu palpite foi muito baixo.")
    elif ((palpite>valor) and (palpite<=10)):
        print("Seu palpite foi muito alto.")
    elif (palpite==valor):
        print(f"Correto! o numero é {valor}")
    else:
        print ("Voce não digitou um numero entre 1 e 10")