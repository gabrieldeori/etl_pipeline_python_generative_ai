import pandas as pd

user_csv_data = pd.read_csv('data/user_info_2023.csv')
user_ids = user_csv_data['UserID'].tolist()
print(user_ids)
