print('\033[0;33;44mHello World!')
#primeira casa - estilo do texto (normal, sublinhado, negrito, etc)
#segunda casa - cor do texto
#terceira casa - cor do fundo do texto

#estilo
#0 = sem estilo
#1 = negrito
#4 = underline
#7 = negativo

#texto
#30 - branco
#31 - vermelho
#32 - verde
#33 - amarelo
#34 - azul
#35 - roxo
#36 - ciano
#37 - cinza

#fundo
#40 - branco
#41 - vermelho
#42 - verde
#43 - amarelo
#44 - azul
#45 - roxo
#46 - ciano
#47 - cinza

print('\033[0;30;41mTeste')
print('\033[4;33;44mTeste')
print('\033[1;35;43mTeste')
print('\033[30;42mTeste') #sem padrão de estilo
print('\033[mTeste') #padrão do terminal
print('\033[7;30mTeste')