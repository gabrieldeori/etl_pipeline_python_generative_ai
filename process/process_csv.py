import pandas as pd

def return_user_ids():
    user_csv_data = pd.read_csv('data/user_info_2023.csv')
    user_ids = user_csv_data['UserID'].tolist()
    return user_ids
