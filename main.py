import requests
from datetime import datetime

USERNAME = "prashantkumar"
TOKEN = "hruirr3mnn4dkmf5jm6j"
GRAPH_ID = "kumar123"
pixela_endpoint ="https://pixe.la/v1/users"

user_paramas ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor": "yes"

}

#response = requests.post(url=pixela_endpoint,json=user_paramas)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Daily running Graph ",
    "unit": "km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
#response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
#print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
#print(today.strftime("%Y%m%d"))
pixela_data ={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many km did you run today? "),

}

response=requests.post(url=pixel_creation_endpoint,json=pixela_data,headers=headers)
print(response.text)

update_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_data ={
     "quantity":"5.00"
}
#response= requests.put(url=update_endpoint,json=update_data,headers=headers)
#print(response.text)

delete_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

#response = requests.delete(url=delete_endpoint,headers=headers)
#print(response.text)
