import requests
from datetime import datetime
USERNAME = ""  # your username
TOKEN = ""  # your token
ID = ""  # your ID
pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# create the user first
# response = requests.post(pixela_endpoint, json=parameters)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_configuration = {
    "id": ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}
headers = {"X-USER-TOKEN": TOKEN}

# create the graph
# response = requests.post(
#     url=graph_endpoint, json=graph_configuration, headers=headers)
# print(response.text)


upload_pixel = f"{graph_endpoint}/{ID}"
now = datetime.now()
pixel_configuration = {
    "date": now.strftime("%Y%m%d"),
    "quantity": "15.1"
}
# add a pixel into the graph
# response = requests.post(
#     url=upload_pixel, json=pixel_configuration, headers=headers)
# print(response.text)

# detele the pixel, if you want to uodate it use put
body = {
    "quantity": "10.5"
}
response = requests.delete(url=f"{upload_pixel}/{now.strftime('%Y%m%d')}",
                           headers=headers)
print(response.text)
