alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
print(aliens)

aliens_verdes = []
print("\nCriação de aliens verdes:")
for alien_v in range(30):
    novo_alien_verde = {'color': 'green', 'points': 5}
    aliens_verdes.append(novo_alien_verde)

for aliens in aliens_verdes[:5]:
    print(aliens)
print('...')
print("Número total de aliens verdes: " + str(len(aliens_verdes)))

for alien in aliens_verdes[:3]:
    if alien['color'] == 'green':
        alien['color'] == 'yellow'
        alien['points'] == 10

print(aliens_verdes[0:5])