#using filter

lista = [
    {'nome':'maria', 'idade':31},
    {'nome':'joao', 'idade':12},
    {'nome':'pedro', 'idade':45},
    {'nome':'marcia', 'idade':11},
    {'nome':'italo', 'idade':22},
    {'nome':'talita', 'idade':90}
]

idades = filter(lambda pessoa: pessoa['idade'] < 18, lista)

print(list(idades))