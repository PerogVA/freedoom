import requests


print('hello world')
print('Good morning'*50)
response = requests.get("https://api.thecatapi.com/v1/images/search").json()
random_cat = response[0].get('url')
print(random_cat)
