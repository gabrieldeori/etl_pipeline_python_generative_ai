from request_from_api import get_users_one_by_one
from process.csv_user import return_user_ids

def main():
    ACTUAL_USER_DATA_PATH = 'data/user_info_2023.csv'
    user_ids = return_user_ids(ACTUAL_USER_DATA_PATH)
    get_users_one_by_one(user_ids)
