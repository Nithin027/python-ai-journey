import requests 

response = requests.get("https://api.github.com")
print(response.status_code)
print(type(response))


import requests

response = requests.get("https://api.github.com")
print(response.status_code)
data = response.json()
print(data)

import requests

response = requests.get("https://api.github.com")
data = response.json()

# print specific keys instead of everything
for key, value in data.items():
    print(f"{key}: {value}")

import requests

username = "Nithin027"
response = requests.get(f"https://api.github.com/users/{username}")
data = response.json()

print(f"Name: {data['name']}")
print(f"Username: {data['login']}")
print(f"Public Repos: {data['public_repos']}")
print(f"Followers: {data['followers']}")

username = "Nithin027"
response = requests.get(f"https://api.github.com/users/{username}")

if response.status_code == 200:
    data = response.json()
    print(f"Username: {data['login']}")
    print(f"Public Repos: {data['public_repos']}")
    print(f"Followers: {data['followers']}")
else:
    print(f"Error: {response.status_code}")    

