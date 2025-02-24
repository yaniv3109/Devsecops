import requests

todos_url = "https://jsonplaceholder.typicode.com/todos"


response = requests.get(todos_url)

if 200 <= response.status_code < 300:
    data = response.json()
    for task in data:
        print(f'title = {task["title"]}. status = {task["completed"]}.', end= "")

        url_user = f'https://jsonplaceholder.typicode.com/users/{task["userId"]}'
        user_response = requests.get(url_user)
        user = user_response.json()
        print(f'user name: {user["name"]}')
else:
    print("Check the request")