import requests

url = 'https://zvdeeqox1g.execute-api.eu-west-1.amazonaws.com/test/predict'  # Access restricted to my own IP address

data = {'url': 'https://upload.wikimedia.org/wikipedia/commons/1/18/Vombatus_ursinus_-Maria_Island_National_Park.jpg'}

result = requests.post(url, json=data).json()
print(result)
