"""
Dada uma lista de endereços web (URLs) que sempre começam com "www." e sempre terminam com ".com",
use o conceito de fatiamento de listas para criar uma lista dominios com o nome principal de todos
os domínios, conforme exemplo a seguir. 

URLs: ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

dominios:  ["google", "gmail", "github", "reddit", "yahoo"] """

# Lista original de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Lista para armazenar os domínios
dominios = []

# Loop através de cada URL na lista
for url in urls:
  # Fatiamento da string: remove os 4 primeiros caracteres ("www.")
  # e os 4 últimos (".com")
  dominio = url[4:-4]
  
  # Adiciona o domínio à nova lista
  dominios.append(dominio)

# Imprime a lista de domínios resultante
print(dominios)