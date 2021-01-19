########################################################################################################################
#Laços condicionais usando if
########################################################################################################################

carros = ('chevrolet', 'subaru', 'ford', 'ferrari', 'fiat', 'mitsubishi', 'toyota supra')

for carro in carros:
    if carro == 'fiat':
        print(carro.upper())
    else:
        print(carro.title())

########################################################################################################################
#Exercícios 5.1 e 5.2
########################################################################################################################

print("\n>>>Exercício 5.1<<<")

for carro in carros:
    if carro == 'toyota supra':
        print(carro.title() + ": THAT'S A SUPRAAAAAA YOOOOOO????")
    else:
        print(carro.title() + ": it's not a supra :(")

print('\n>>>Exercício 5.2<<<')
#teste1
for carro2 in carros:
    if carro2.upper() == 'FIAT':
        print(carro2)

#teste2
carro3='corsinha amarelo'
print(carro3 == 'brasília amarela')

#teste3
carro4 = 'jeep'
if carro4 not in carros:
    print(carro4.title() + ' não é um bom carro.')

#teste4
carro5 = 'nissan'
if 'nissan' in carros:
    print('Nissan é brabo.')
else:
    print('Esqueceram do Nissan')
