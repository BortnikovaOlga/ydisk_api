import requests

url = "https://cloud-api.yandex.net/v1/disk/"

payload = {}
headers = {'Authorization': 'OAuth y0_AgAAAABqM4PDAAnOqQAAAADhuCtW-neeWjrGT0yMkBb3sHTppvj6Faw'}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
