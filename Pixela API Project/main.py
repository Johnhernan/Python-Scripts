import requests
import datetime as dt

USERNAME = "foo"
TOKEN = "foo"
ID = "foo"

if __name__ == '__main__':
    pixela_endpoint = "https://pixe.la/v1/users"

    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    # response = requests.post(url=pixela_endpoint, json=user_params)
    # print(response.text)

    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

    graph_config = {
        "id": ID,
        "name": "Coding Graph",
        "unit": "commit",
        "type": "float",
        "color": "sora"
    }

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    # response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    # print(response.text)

    graph_id_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"
    today = dt.datetime.now()

    pixel_data = {
        "date": today.strftime("%Y%m%d"),
        "quantity": "2",
    }

    response = requests.post(url=graph_id_endpoint, json=pixel_data, headers=headers)
    print(response.text)