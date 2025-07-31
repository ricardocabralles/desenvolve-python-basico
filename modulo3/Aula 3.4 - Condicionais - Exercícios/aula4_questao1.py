"""
Escreva um programa que lê dois números e informa se a sua soma é
par ou ímpar. Critério: se o resto da divisão do número por 2 for 0,
o número é par, caso contrário é ímpar. Lembre-se do operador do
python % que retorna o resto de uma divisão. 
"""

n1=int(input("Digite um numero inteiro: "))

n2=int(input("Digite outro numero inteiro: "))
soma=n1+n2


if((soma)%2==0):
    print("O valor da soma dos numeros é: ", soma, ". A soma é par.")  
else:
       print("O valor da soma dos numeros é: ", soma, ". A soma é impar.")