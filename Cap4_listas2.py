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