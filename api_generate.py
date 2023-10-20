from generate_message import generate_customers_message


def exampleCustomer():
    customers = [
        {
            'nome': 'Gabriel de Oliveira',
            'objetivos': ['casa', 'carro'],
            'foco': ['captar cliente'],
        },
        {
            'nome': 'João da Silva',
            'objetivos': ['aluguel', 'empreender'],
            'foco': ['empréstimo']
        }
    ]

    customers_message = generate_customers_message(customers)
    return customers_message
