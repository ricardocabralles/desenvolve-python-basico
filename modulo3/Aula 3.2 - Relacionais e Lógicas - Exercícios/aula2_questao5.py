"""5 - 
Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu 
tempo de serviço (em anos) e escreva uma expressão que imprima True
se a pessoa já pode se aposentar, ou False caso contrário, de acordo
com as seguintes regras:

A: Para mulheres, ter mais de 60 anos. Para homens, 65.

B: Ou ter trabalhado pelo menos 30 anos

C: Ou ter 60 anos  e trabalhado pelo menos 25."""

sexo=input("qual o seu genero( escreva M para Masculino e F para Faminino):")

idade=int(input("qual a sua idade:" ))

tempo=int(input("qual seu tempo de serviço: "))

chave=(((sexo=="M") and (idade>=65) or ((sexo=="F") and(idade>=60))) or (tempo>=30) or ((idade>=60) and (tempo>=25) ))

print("O funcionario já pode se aposentar: ", chave)