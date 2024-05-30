import requests

r = requests.get('http://127.0.0.1:8000/api/v1/women')
r2 = requests.get('http://127.0.0.1:8000/api/v1/women/3')
print(r.text)
print(r2.text)
