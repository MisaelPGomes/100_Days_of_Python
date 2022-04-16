import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "misael"
TOKEN = "sjkajskasjdlkaslkada"
graph_ID = "graph1"
user_paramers = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",

}

#response = requests.post(url=pixela_endpoint, json=user_paramers)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": graph_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",

}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

today = datetime.now()
print(today.strftime("%Y%m%d"))

post_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Km did you cycle today?: ") ,
}

response = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_ID}", json=post_pixel_config, headers=headers)

print(response.text)

update_pixel = {
    "quantity": "20",

}

#response = requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_ID}/{today.strftime('%Y%m%d')}", json=update_pixel, headers=headers)

#print(response.text)

#response = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/{graph_ID}/{today.strftime('%Y%m%d')}", headers=headers)

