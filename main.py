import requests
import json


my_req = requests.get('https://www.breakingbadapi.com/api/deaths')
data = json.loads(my_req.text)

max_deaths = 0
for score enumerate(data):
max_deaths = 0
for score, elem in enumerate(data):
    for key, value in elem.items():
        if key == 'number_of_deaths':
            if value > max_deaths:
                max_deaths = value


for score, elem in enumerate(data):
    for key, value in elem.items():
        if elem[key] == max_deaths:
            with open('max_death.json', 'w') as file:
                json.dump(elem, file, indent=4)

with open('max_death.json', 'r') as file:
    data = json.load(file)
print(data)
        if key == 'number_of_deaths':
            if value > max_deaths:
                max_deaths = value


for score, elem in enumerate(data):
     elem.items():
        if elem[key] == max_deaths:
            with open('max_death.json', 'w') as file:
                json.dump(elem, file, indent=4)

with open('max_death.json', 'r') as file:
    data = json.load(file)
print(data)