########################################################################################################################
#Dicionários são uma forma de armazenar diversos tipos de informação e relacioná-las através de palavas chave-valor.
#Onde cada palavra chave é atribuída à um valor.
########################################################################################################################

print('Exemplo de dicionário:')
alien_0={'cor': 'verde', 'pontos':'5'}
print("A cor do alien é: " + alien_0['cor'] + ".")
print("O alien possui " + alien_0['pontos'] + " pontos.")

########################################################################################################################
#Acrescentando chaves-valor no dicionário.
#Muitas vezes o ideal é iniciar o dicionário vazio e acrescentar as chaves e valores através deste método.
########################################################################################################################

alien_0['posição_x'] = 0
alien_0['posição_y'] = 25
print(alien_0)

########################################################################################################################
#Modificando as chaves-valor para medir a posição de uma nave alienígena
########################################################################################################################

alien_0['velocidade'] = 'fast'
print('Posição original da nave: ' + str(alien_0['posição_x']))
for posição in range(1,10):
    if alien_0['velocidade'] == 'slow':
        incremento_x = 1
    elif alien_0['velocidade'] == 'medium':
        incremento_x = 2
    elif alien_0['velocidade'] == 'fast':
        incremento_x = 3
    alien_0['posição_x'] = alien_0['posição_x'] + incremento_x
    print('A nova posição da nave é: ' + str(alien_0['posição_x']))

########################################################################################################################
#Identando dicionários de diferentes objetos
########################################################################################################################

linguagem_favorita = \
    {
    'cleiton': 'python',
    'rubens': 'python',
    'júlio': 'java',
    'fernanda': 'cpp',
    'pedro': 'java'
     }
print(linguagem_favorita)

########################################################################################################################
#Exercícios 6.1 até 6.3
########################################################################################################################

print("\n>>>Exercício 6.1<<<")
pessoa_n = \
    {
    'Nome': 'José',
    'Sobrenome': 'Buendía',
    'Idade': '283 anos',
    'Cidade': 'Macondo'
    }
print(pessoa_n)

print("\n>>>Exercício 6.2<<<")
n_favoritos = \
    {
        'pessoa 1': '1657',
        'pessoa 2': '9609',
        'pessoa 3': '2323',
        'pessoa 4': '9512',
        'pessoa 5': '5918'
    }
print(n_favoritos)

print("\n>>>Exercício 6.3<<<")
dicionário1 = \
    {
        'palavra1': 'significado1',
        'palavra2': 'significado2',
        'palavra3': 'significado3'
    }
print(dicionário1)
print('\n')


########################################################################################################################
#Utilizar o método .items() .keys() e .values() para criar laços que percorrem o dicionário inteiro.
########################################################################################################################

for i, t in n_favoritos.items():
    print("Chave: " + i)
    print('Valor: ' + t)

print("\nPrecisamos dos seguintes dados: ")
for dados in sorted(pessoa_n.keys()):
     print(dados)

for pessoas in pessoa_n.values():
    print(pessoas)
