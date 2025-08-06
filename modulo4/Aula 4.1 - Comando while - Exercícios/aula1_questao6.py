total = 0
sapos = 0
ratos = 0
coelhos = 0

N = int(input("Número de experimentos: "))
i = 0

while i < N:
    quantia = int(input(f"Quantidade de cobaias utilizada no{(i+1)}º experimento: "))
    tipo = input("Digite o tipo de cobaia utilizado (C: coelho, S: sapo ou R: rato):")

    total += quantia
    if tipo == 'S':
        sapos += quantia
    elif tipo == 'R':
        ratos += quantia
    elif tipo == 'C':
        coelhos += quantia
    
    i += 1 

percent_sapos = (sapos / total) * 100
percent_ratos = (ratos / total) * 100
percent_coelhos = (coelhos / total) * 100


print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {percent_coelhos:.2f} %")
print(f"Percentual de ratos: {percent_ratos:.2f} %")
print(f"Percentual de sapos: {percent_sapos:.2f} %")
