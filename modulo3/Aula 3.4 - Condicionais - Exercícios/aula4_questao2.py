""""
Você está criando um sistema de classificação de filmes com base nas
avaliações dos usuários. Escreva um programa em Python que solicita
ao usuário para inserir a avaliação de um filme em uma escala 
de 1 a 5. O programa deve imprimir uma mensagem correspondente
à classificação do filme:

Se a avaliação for 5, imprima "Excelente!"

Se a avaliação for 4, imprima "Muito Bom!"

Se a avaliação for 3, imprima "Bom!"

Se a avaliação for 2, imprima "Regular."

Se a avaliação for 1, imprima "Ruim." """

nome=input("Digite o nome do filme que deseja avaliar:")

aval=int(input("De 1 a 5 qual a sua avaliação do filme:"))

if (aval==5):
    print("Você classificou o filme:", nome, "como Excelente!")
if (aval==4):
    print("Você classificou o filme:", nome, "como Muito Bom!")
if (aval==3):
    print("Você classificou o filme:", nome, "como Bom!")
if (aval==2):
    print("Você classificou o filme:", nome, "como Regular!")
if (aval==1):
    print("Você classificou o filme:", nome, "como Ruim!")