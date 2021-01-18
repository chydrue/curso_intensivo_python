###########################################################################################
#Trabalhando com partes de uma lista
###########################################################################################

nomes = ['cleiton', 'josé', 'lívia', 'luís', 'amanda', 'luíza', 'eleonora', 'camila', 'morais']
print(nomes[0:6])
print(nomes[:3])
print(nomes[3:])
print(nomes[-3:])
print(nomes[:-2])

###########################################################################################
#Exercícios 4.10 até 4.12
###########################################################################################

print("\n>>>Exercício 4.10<<<")
print("Os 3 primeiros nomes são: " + str(nomes[:3]))
print("Os 3 nomes do meio são: " + str(nomes[3:6]))
print("Os 3 últimos nomes são: " + str(nomes[-3:]))

print("\n>>>Exercício 4.11<<<")
from Cap4_listas import pizzas
pizzas_amigo = pizzas[:]
pizzas_amigo.append('toscana')
pizzas.append('chocolate')
print(f"Minhas pizzas favoritas são: {pizzas}")
print(f"As pizzas favoritas do meu amigo são: {pizzas_amigo}")

