import requests
import json

# Выполняем запрос Post - добавляем нового питомца

BASE_URL = 'https://petstore.swagger.io/v2'
new_pet = {
    "id": 123456786,
    "category": {
        "id": 1,
        "name": "Chikka"
    },
    "name": "cat",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
res = requests.post(f'{BASE_URL}/pet', headers=headers, data=json.dumps(new_pet))
print(res.status_code)
print(res.json())

# Выполняем запрос GET- ищем питомца по id

Pet_id = 123456786
res_2 = requests.get(f'{BASE_URL}/pet/{Pet_id}', headers={'accept': 'application/json'})
print(res_2.status_code)
print(res_2.json())


# Выполняем запрос PUT- изменяем кличку питомца

new_name = {
    "id": 123456786,
    "category": {
        "id": 1,
        "name": "Musya"
    },
    "name": "cat",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}
res_3 = requests.put(f'{BASE_URL}/pet', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=json.dumps(new_name))
print(res_3.status_code)
print(res_3.json())

#Выполняем запрос DELETE - удаялем питомца

Pet_id = 123456786
res_4 = requests.delete(f'{BASE_URL}/pet/{Pet_id}', headers={'accept': 'application/json', 'Content-Type': 'application/json'})
print(res_4.status_code)
print(res_4.json())