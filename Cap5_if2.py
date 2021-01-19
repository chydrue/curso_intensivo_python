
########################################################################################################################
#Instruções if-elif-else possibilitam 3 saídas diferentes para o teste.
#Pode-se usar quantos elif quiser e não é necessário usar o else
########################################################################################################################

idade = 90

if idade < 4:
    preço = 0.0
elif idade < 18:
    preço = 5.0
elif idade < 65:
    preço = 10.0
else:
    preço = '5.0 com o desconto para idosos.'

print('O valor do seu ingresso é: R$' + str(preço) )

########################################################################################################################
#Exercícios 5.3 até 5.7
########################################################################################################################
print('\n>>>Exercício 5.3<<<')
alien_color = 'green'
if alien_color == 'green':
    print("Você ganhou 5 pontos")

alien_color = 'red'
if alien_color == 'green':
    print("Você ganhou 5 pontos")

print('\n>>>Exercício 5.4<<<')
alien_color = 'red'
if alien_color == 'green':
    print("Você ganhou 5 pontos")
else:
    print("Você ganhou 10 pontos")

print('\n>>>Exercício 5.5<<<')
alien_color = 'yellow'
if alien_color == 'green':
    print("Você ganhou 5 pontos")
elif alien_color == 'yellow':
    print("Você ganhou 10 pontos")
else:
    print("Você ganhou 15 pontos")

if alien_color == 'red':
    pontos = 15
if alien_color == 'yellow':
    pontos = 10
if alien_color == 'green':
    pontos =5
print('Você ganhou ' + str(pontos) + ' pontos!')