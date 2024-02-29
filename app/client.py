import requests

response = requests.post('http://127.0.0.1:5000/hello/world',
                         json={"name": "user_1", "password": "1234"},
                         params={"name": "Alex", "age": "28"},
                         headers={"token": "some_token"})
print(response.status_code)
print(response.text)
