import requests
import json
import global_configs as gc

def get_user(id):
    response = requests.get(f'{gc.API_URL}/users/{id}')
    if response.status_code == 200:
        return response.json()

def get_users_one_by_one(user_ids):
    users = [user for id in user_ids if (user := get_user(id)) is not None]
    print(json.dumps(users, indent=2))
    return users
