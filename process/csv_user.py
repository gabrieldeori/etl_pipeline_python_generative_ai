import pandas as pd

def return_user_ids(path):
    user_csv_data = pd.read_csv(paths)
    user_ids = user_csv_data['UserID'].tolist()
    return user_ids
