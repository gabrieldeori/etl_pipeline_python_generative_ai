customers = [
    {
        'nome': 'Gabriel de Oliveira',
        'idade': 28,
        'interesses': ['games', 'viagem'],
        'objetivos': ['casa', 'carro'],
        'foco': ['captar cliente'],
    },
    {
        'nome': 'João da Silva',
        'idade': 45,
        'interesses': ['futebol', 'música'],
        'objetivos': ['aluguel', 'empreender'],
        'foco': ['empréstimo']
    }
]

for customer in customers:
    print(customer['nome'])
    print(customer['idade'])
    print(customer['interesses'])
    print(customer['objetivos'])
    print(customer['foco'])
    print('-------------------\n')

