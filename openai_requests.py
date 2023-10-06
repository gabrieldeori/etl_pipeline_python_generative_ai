import openai
from decouple import config

def generate_ai_marketing_message(customer):
    api_key = config('OPENAI_API_KEY')

    if api_key:
        openai.api_key = api_key

    else:
        print('A variável de ambiente API_KEY não está configurada.')
        return 0

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
