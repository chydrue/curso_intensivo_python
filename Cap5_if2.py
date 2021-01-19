
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
#Exercícios 5.3 até 5.6
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

print('\n>>>Exercício 5.6<<<')
idade = 89123
if idade < 2:
    print('A pessoa é um bebê.')
elif idade < 4:
    print("A pessoa é uma criança.")
elif idade < 13:
    print("A pessoa é uma garota(o)")
elif idade < 20:
    print("A pessoa é um adolescente.")
elif idade < 65:
    print("A pessoa é adulta.")
elif idade >= 65:
    print("A pessoa é idosa.")

########################################################################################################################
#Exercícios 5.8 até 5.11
########################################################################################################################

print("\n>>>Exercício 5.8<<<")

usuários = ['cleiton', 'caroline', 'valdirene', 'juliana', 'admin']
for login in usuários:
    if login == 'admin':
        print("Olá caro administrador, gostaria de tomar uma xícara de café?")
    else:
        print('Olá ' + login.title() + ', que bom que voltou!!')


print("\n>>>Exercício 5.9<<<")
usuários2 = []
if usuários2:
    print("Já temos algum usuário")
else:
    print("Precisamos encontrar novos usuários!!!")

print("\n>>>Exercício 5.10<<<")
usuários3 = ['josé', 'claudia', 'juliana', 'camila', 'cleiton']

for usuário in usuários3:
    for usuário2 in usuários:
        if usuário.lower() == usuário2.lower():
            print("O nome " + usuário + " já está sendo utilizado. Por favor, escolha outro.")

print('\n>>>Exercício 4.11<<<')
números_ordinais = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for números in números_ordinais:
    if números == '1':
        print("1st")
    elif números == '2':
        print("2nd")
    elif números == '3':
        print("3rd")
    else:
        print(números + 'th')

