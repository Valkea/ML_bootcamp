import requests

# docker run -it --rm -p 8080:8080 dogs-cats:latest
url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

data = {'url': 'https://upload.wikimedia.org/wikipedia/commons/1/18/Vombatus_ursinus_-Maria_Island_National_Park.jpg'}

result = requests.post(url, json=data).json()
print(result)
