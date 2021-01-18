###########################################################################################
#Estatística simples com uma lista de números
###########################################################################################

dígitos = list(range(1,35))
menor_valor = min(dígitos)
maior_valor = max(dígitos)
soma = sum(dígitos)
print("Lista:" + str(dígitos))
print('Menor valor:' + str(menor_valor) +'\nMaior valor' + str(maior_valor) + '\nSoma: ' + str(soma))

quadrados = [valor**2 for valor in range(1,11)]
print('\nQuadrados: ' + str(quadrados))

###########################################################################################
#Exercícios 4.3 até 4.9
###########################################################################################

print('\n>>>Exercício 4.3<<<')
ex43 = [valor for valor in list(range(1,21))]
print(ex43)

print('\n>>>Exercício 4.4<<<')
ex44 = [valor2 for valor2 in list(range(1,100))]
print(ex44)

print('\n>>>Exercício 4.5<<<')
ex45 = [valor3 for valor3 in list(range(1,1000001))]
menor = min(ex45)
maior = max(ex45)
soma2 = sum(ex45)
print("Menor valor: " + str(menor) + "\nMaior valor: " + str(maior) + "\nSoma: " + str(soma2))

print('\n>>>Exercício 4.6<<<')
ex46 = [valor4 for valor4 in list(range(1,21,2))]
print(ex46)

print("\n>>>Exercício 4.7<<<")
ex47 = []
for valor5 in list(range(3,31,3)):
    ex47.append(valor5)
print(ex47)

