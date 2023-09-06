import requests
import json
import openai

import pandas as pd

from decouple import config

API_URL = 'none'
OPENAI_API_KEY = 'none'
openai.api_key = OPENAI_API_KEY


def extract_user_data(user_data_path):
    def return_user_ids(path):
        user_csv_data = pd.read_csv(path)
        user_ids = user_csv_data['UserID'].tolist()
        return user_ids

    def get_user(id):
        response = requests.get(f'{API_URL}/users/{id}')
        return response.json() if response.status_code == 200 else None

    def get_all_users(user_ids):
        users = [user for id in user_ids if (user := get_user(id)) is not None]
        return users

    user_ids = return_user_ids(user_data_path)
    data = get_all_users(user_ids)
    return data


def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="davinci",
        messages=[{
            "role": "system",
            "content": "Você é um especialista em markting bancário."
        }, {
            "role": "user",
            "content": f"""Crie uma mensagem para {user['name']} sobre a
            importância dos investimentos (máximo de 100 caracteres)"""
        }]
    )
    return completion.choices[0].message.content.strip('\"')


def generate_news_to_users(users):
    for user in users:
        news = generate_ai_news(user)
        user['news'].append({
            "icon": "",
            "description": news
        })
        print(f'Generated news for {user["name"]}')
        print(f'News: {news}')
    return users


def update_user(user):
    response = requests.put(f"{API_URL}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False


def update_all_users(users):
    for user in users:
        success = update_user(user)
        print(f"User {user['name']} updated? {success}!")


def main():
    USER_DATA_PATH = 'data/user_info_2023.csv'
    users = extract_user_data(USER_DATA_PATH)
    users_generated_news = generate_news_to_users(users)
    update_all_users(users_generated_news)


main()
