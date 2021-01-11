# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 09:05:56 2020

@author: Cleiton Kennedy de Morais Filho
"""

carros = ['bmw', 'toyota', 'volks', 'fiat', 'ford', 'renault', 'nissan', 'audi']




########################################################################################################################################################
#O método .sort() irá organizar uma lista em ordem alfabética de forma definitiva. 
#É possível utilizar o parâmetro .sort(Reverse=True) para organizar a lista de forma ao contrário da alfabética
#A função sorted() irá mostrar a lista organizada porém sem alterar a mesma.
########################################################################################################################################################

carros.sort()
print(carros)

carros.sort(reverse=True)
print(carros)

print(sorted(carros))

