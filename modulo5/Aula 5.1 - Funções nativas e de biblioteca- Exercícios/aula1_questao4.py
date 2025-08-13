"""Escreva um programa em Python que utiliza a biblioteca datetime 
para exibir a data e hora atuais com a formatação apresentada 
a seguir:

Data: 15/03/2023 

Hora: 14:05

Você pode consultar esse  tutorial da Alura sobre a biblioteca 
datetime. Existem várias maneiras de resolver essa questão. 
Uma sugestão é:

Função datetime.datetime.now() cujo retorno possui os atributos:
day, month, year, hour, minute

Usar a formatação com f-strings no momento de imprimir.
Atenção para os atributos que devem sempre ter 2 dígitos precedidos
 por zero se necessário."""

from datetime import datetime

agora = datetime.now()

dia = agora.day
mes = agora.month
ano = agora.year
hora = agora.hour
minuto = agora.minute


print(f"Data: {dia:02d}/{mes:02d}/{ano}")
print(f"Hora: {hora:02d}:{minuto:02d}")