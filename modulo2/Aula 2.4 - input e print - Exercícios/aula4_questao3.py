"""
3 - Você está desenvolvendo um programa para calcular o preço total de uma
compra em uma loja online. O preço dos produtos é calculado multiplicando a
quantidade pelo preço unitário. Escreva um programa em Python que solicite
do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados
e imprima ao final o preço total da compra. Note no exemplo a seguir que:

Cada entrada de dados tem uma mensagem indicando o dado solicitado 
(mensagens em itálico, dado de entrada em negrito)

A saída deve estar formatada exatamente como indicado (a string "Total: R$"
 e o preço com um separador de milhar e duas casas decimais).




Entrada

Saída

Digite o nome do produto 1:calça

Digite o preço unitário do produto 1:199.90

Digite a quantidade do produto 1: 3

Digite o nome do produto 2:camisa

Digite o preço unitário do produto 2:49.95

Digite a quantidade do produto 2:10

Digite o nome do produto 3:cinto

Digite o preço unitário do produto 3:25

Digite a quantidade do produto 3:3

Total: R$1,174.20
"""
#produto 1
produto1=input("digite o nome do produto 1:") #entrada do nome do produto
valor1=float(input("digite o valor do produto 1:")) #entrada do valor do produto
quantidade1=int(input("digire a quantidade do produto 1:"))#entrada da quantidade do produto

#produto 2
produto2=input("digite o nome do produto 2:") #entrada do nome do produto
valor2=float(input("digite o valor do produto 2:")) #entrada do valor do produto
quantidade2=int(input("digire a quantidade do produto 2:"))#entrada da quantidade do produto

#produto 3
produto3=input("digite o nome do produto 3:") #entrada do nome do produto
valor3=float(input("digite o valor do produto 3:")) #entrada do valor do produto
quantidade3=int(input("digire a quantidade do produto 3:"))#entrada da quantidade do produto


#processamento
valortot=(valor1*quantidade1)+(valor2*quantidade2)+(valor3*quantidade3)

#saida

print(f"Total: R${valortot:,.2f}")