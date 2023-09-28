import openai

from decouple import config

api_key = config('OPENAI_API_KEY')


def generate_ai_marketing_message(customer):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Especialista marketing bancário"
            },
            {
                "role": "user",
                "content": f"""
                Gere uma mensagem para o cliente {customer['nome']}.
                Foque em {customer['foco']}
                para ele alcançar seus objetivos: {customer['objetivos']}.
                Seja convincente em 200 caracteres. Retorne APENAS a MENSAGEM.
                """
            }
        ]
    )
    return completion.choices[0].message.content.strip('\"')


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

customers_message = []

if api_key:
    print(f'Sua chave de API é: {api_key}')
    openai.api_key = api_key

    for customer in customers:
        message = generate_ai_marketing_message(customer)
        customers_message.append(message)

else:
    print('A variável de ambiente API_KEY não está configurada.')
