import random

n = random.random() #gera um float de 0 a 1
print(n)

x = random.randint(1, 10)
print(x) #gera um int de 1 a 10

#import ctrl+espaço abre uma lista de todas as bibliotecas nativas importáveis, fora as de fora que pode baixar

#no site do python.org, na aba PyPI, eu tenho uma lista comunitária de pacotes de bibliotecas. lá, eu baixo a que eu
#quiser

#importar bibliotecas dentro do pycharm é MUITO fácil. boto o "import <biblioteca>" e ao colocar o nome da biblioteca
#já posso clicar com o botão direito em cima dela e pedir pro computador baixa, sem ir ao site.

import emoji
print(emoji.emojize('Hello World! :earth_americas:', use_aliases=True))

#emojize transforma os códigos de emojis entre :: em emojis.
#use_aliases=True permite que a variável comporte essa transformação

#pra ver quais bibliotecas externas eu tenho instaladas, ir em Settings > Project > Project Interpreter