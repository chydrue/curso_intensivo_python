# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:47:51 2020

@author: Cleiton Kennedy de Morais Filho
"""


########################################################################################################################################################
# Utilizar o índice -1 em uma lista retorna o último valor da mesma. De forma análoga para os números -2, -3,etc
########################################################################################################################################################

bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
print(bicicletas[-1].title())




########################################################################################################################################################
# o método .append() insere um valor na última posição da lista
########################################################################################################################################################

bicicletas.append('monark')
print(bicicletas)



########################################################################################################################################################
 # o método .insert(x, 'y') insere um valor y na posição x da lista
########################################################################################################################################################
bicicletas.insert(2, 'caloi')
print(bicicletas)


########################################################################################################################################################
# Para retirar um elemento de maneira definitiva de uma lista podemos utilizar o comando del
########################################################################################################################################################

del bicicletas[5]
print(bicicletas)


########################################################################################################################################################
 # Para retirar um elemento e ainda utilizá-lo usamos o método .pop(x) que irá retirar o elemento x da lista mas este elemento ainda poderá ser usado.
########################################################################################################################################################

popped_bicicletas = bicicletas.pop(3)
print(popped_bicicletas)
print(bicicletas)

x=1
for k in range(x):
    pop_bikes=bicicletas.pop(0)                  #ATENÇÃO: como o elemento será retirado o índice dos valroes irá mudar a cada incremento
    print(pop_bikes)
    print(bicicletas)


########################################################################################################################################################
#Caso não saiba a posição do elemento mas saiba o valor podemos utilizar o método .remove()
#Podemos armazenar o valor retirado em uma variável para justificar sua retirada, por exemplo.
#Este método retira apenas um valor, caso existam valores repetidos será necessário implementar um loop
########################################################################################################################################################

muito_cara = 'specialized'
bicicletas.remove(muito_cara)
print(bicicletas)
print('\n\tA ' + muito_cara.title() + ' é uma bicicleta cara demais e por isso foi retirada da lista.')



bicicletas.append('bmx')
bicicletas.append('speed')
bicicletas.append('lazer')

print(bicicletas)

marcas= ['caloi', 'cannondale']
for i in range(2):
    bicicletas.remove(marcas[i])
print(bicicletas)



















