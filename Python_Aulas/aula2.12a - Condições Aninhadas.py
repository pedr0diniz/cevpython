#programar a melhor condições mas sempre explorar alternativas

#if - primeira condição, que vai validar iniciar as análises de condições
#elif - senão se, exceção ao primeiro if ou a elifs passados, mas sem ser a exceção a tudo
#else - senão, exceção a todas as condições vistas antes

nome = str(input('Qual é seu nome? '))
if nome == 'ziniD':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana Mariana Catherine Amanda':
    print('Belo nome feminino!')
elif nome == 'Juanilson':
    print('Você é meu! Eu mando em você!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))