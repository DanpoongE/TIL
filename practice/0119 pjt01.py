# 서버로부터 데이터 가져오기
# https://fakestoreapi.com/carts

import requests

url = 'https://fakestoreapi.com/carts'
data = requests.get(url).json()
print(data)
