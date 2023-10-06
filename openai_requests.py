import openai
api_key = config('OPENAI_API_KEY')
from decouple import config

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
