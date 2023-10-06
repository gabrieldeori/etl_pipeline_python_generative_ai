from openai_request import generate_ai_marketing_message

def generate_customers_message(customers):
    customers_message = []
    for customer in customers:
        message = generate_ai_marketing_message(customer)
        customers_message.append(message)
    return customers_message
