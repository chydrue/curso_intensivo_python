# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:13:59 2020

@author: Cleiton Kennedy de Morais Filho
"""

mensagem1 = 'Espaço em branco no lado direito '
print(mensagem1)
mensagem1 = mensagem1.rstrip()     #rstrip retira os espaços em branco do ladi direito da string

mensagem2 = ' Espaço em branco no lado esquerdo'     #lstrip retira os espaços em branco do ladi esquerdo da string
mensagem2= mensagem2.lstrip()
print(mensagem2)

mensagem3 = ' Espaço em branco dos dois lados '
mensagem3 = mensagem3.strip()                       #strip() retira o espaço em branco dos dois lados da string
print(mensagem3)

#ESSES MÉTODOS SÃO UTILIZADOS PARA LIMPAR UMA ENTRADA DE USUÁRIO
