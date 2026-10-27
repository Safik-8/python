import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print(response)
print(response.status_code)
print(response.text)

data = response.json()[0]

print(type(data))

# Access individual fields

print(data["id"])
print(data["name"])
print(data["email"])
print(data["phone"])
print(data["website"])