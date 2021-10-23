#using reduce
#!/usr/local/bin/python3

from functools import reduce

lista = [
    {'nome':'maria', 'idade':31},
    {'nome':'joao', 'idade':12},
    {'nome':'pedro', 'idade':45},
    {'nome':'marcia', 'idade':11},
    {'nome':'italo', 'idade':22},
    {'nome':'talita', 'idade':90}
]

# 0 = valor inicial do acumulador 'idades'
idades = reduce(lambda idades, pessoa: idades + pessoa['idade'], lista, 0)

print(idades)