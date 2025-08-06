n1=int(input("Digite o primeiro numero inteiro(de 0 a 100):"))
n2=int(input("Digite o segundo numero inteiro(de 0 a 100):"))
n3=int(input("Digite o terceiro numero inteiro(de 0 a 100):"))

m=((n1+n2+n3)/3)

if (m>=60):
    print("Aprovado")
elif (m>=40):
    print("recuperação")
else:
    (print("reprovado"))

print("fim")