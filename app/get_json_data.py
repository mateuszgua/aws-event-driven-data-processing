import requests
import json

from app.save_json_file import save_json_file


def get_api_get_random_users(number_of_users):

    try:
        response = requests.get(
            f"https://randomuser.me/api/?results={number_of_users}&inc=name,email,login,registered")
        list_of_user_datas = response.json()["results"]

        json_object = json.dumps(list_of_user_datas, indent=4)
        save_json_file(json_object)
    except:
        return "Error with load data and save it in json file."
    else:
        return f"Data with {number_of_users} of results successfully added to json."
