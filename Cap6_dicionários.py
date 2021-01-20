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
