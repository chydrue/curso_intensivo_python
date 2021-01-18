
###########################################################################################
#Usando um laço para trabalhar a lista
###########################################################################################
magicians = ['crowley', 'fortune', 'motta']
for magician in magicians:
    print(magician)

###########################################################################################
#Exibindo uma mensagem para cada mágico
###########################################################################################

magicians2 = ['grant', 'agrippa', 'salomão']
for magician2 in magicians2:
    print(magician2.title() + ", essa macumba foi muito boa!!")
    print("Mal posso esperar para ver seu próximo truque, " + magician2.title() + ".\n")

print("Obrigado a todos, está sendo uma aventura incrível! Amor é a Lei, Amor sob Vontade!\n")

###########################################################################################
#Exercícios (4.1 e 4.2)
###########################################################################################
print('\n>>>Exercício 4.1<<<')
pizzas = ['fragobacon', 'cheddar', 'calabresa']
for pizza in pizzas:
    print('A pizza de ' + pizza + 'está em promoção hoje!')
print('Vou comprar uma de cada para aproveitar!!!\n')


print('>>>Exercício 4.2<<<')
gatos = ['max', 'eusébio', 'morpheu']
for gato in gatos:
    k = gatos.index(gato)+1
    print('O ' + gato.title() + ' foi o {K}º animal de estimação a ser adotado!'.format(K=k))
print("\nAdotar animais é muito bom!\n")

###########################################################################################
#Usando a função range() e list() para criar e manipular listas de números
###########################################################################################

números = list(range(1,31))
print(números)

números_pares = list(range(2,31,2))
print(números_pares)

números_impares = list(range(1,32,2))
print(números_impares)

quadrados = []
for valor in range(1,21):
    quadrados.append(valor**2)
print(quadrados)

