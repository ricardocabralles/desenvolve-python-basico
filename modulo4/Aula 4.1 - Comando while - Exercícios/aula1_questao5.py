quant=int(input("Digite o numero de pessoas que responderão:"))
cont=0
idade=0
idadetot=0
while(cont<quant):
    idade=int(input(f"digite a idade do{cont+1}º respondente:"))
    idadetot+=idade
    cont+=1
mediaidade=idadetot/quant
print(f"a media de idade dos respondentes é:{mediaidade}")

