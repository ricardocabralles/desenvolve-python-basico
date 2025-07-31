"""1 - 
Juliana e Cris querem entrar em um bar, 
mas só podem se ambos forem maiores de idade (>17).
 Escreva um programa que solicite as idades de Juliana e Cris
   e imprima True se ambas forem maiores de 17 anos, indicando
     que podem entrar no bar, e False caso contrário.
"""

idjul=int(input("digite a idade de Juliana:"))
    
idcris=int(input("digite a idade de Cris"))

entrada=(idjul>17 and idcris>17) 

print(entrada)