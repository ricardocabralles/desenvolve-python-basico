"""Você está trabalhando em um sistema de mensagens instantâneas,
 que deve permitir o uso de emojis nas conversas entre pessoas. 
 Faça:

No terminal, instale a biblioteca emoji usando o gerenciador de
 pacotes pip

$ pip install emoji

 
Conheça a função emoji.emojize()

Seu programa deve apresentar para o usuário a lista de emojis 
disponíveis com o texto correspondente a cada emoji. Em seguida, 
solicite uma frase codificada ao usuário e apresente ela decodificada 
com a visualização de emojis (emojizada).

A seguir um exemplo de interação, com uma lista de emojis sugeridos.
 Você pode consultar o texto que codifica outros emojis indo nessa 
 página e passando o mouse por cima do emoji desejado. 

Emojis disponíveis:

❤️ - :red_heart:

👍 - :thumbs_up:

🤔 - :thinking_face:

🥳 - :partying_face:


Digite uma frase e ela será emojizada:

Olá mundo! :red_heart:

Frase emojizada:

Olá mundo! ❤️   """

import emoji

# Lista de emojis disponíveis
emojis_disponiveis = {
    "❤️": ":red_heart:",
    "👍": ":thumbs_up:",
    "🤔": ":thinking_face:",
    "🥳": ":partying_face:"
}

# Exibe os emojis disponíveis
print("Emojis disponíveis:\n")
for simbolo, codigo in emojis_disponiveis.items():
    print(f"{simbolo} - {codigo}")

# Solicita a frase ao usuário
frase = input("\nDigite uma frase e ela será emojizada:\n")

# Converte os códigos para emojis
frase_emojizada = emoji.emojize(frase, language='alias')

# Exibe a frase com emojis
print("\nFrase emojizada:\n")
print(frase_emojizada)