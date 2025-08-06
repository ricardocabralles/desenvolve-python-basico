n=int(input("Digite o um numero inteiro:"))
maior=0

while (n>0):
    x=int(input("digite um outro numero inteiro:"))
    if (x>maior):
        maior=x
    n-=1

print(maior)
