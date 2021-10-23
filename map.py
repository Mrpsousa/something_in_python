#using map

lista = [
    {'nome':'maria', 'idade':31},
    {'nome':'joao', 'idade':12},
    {'nome':'pedro', 'idade':65}
]

so_nomes = map(lambda pessoa: pessoa['nome'], lista)

print(list(so_nomes))