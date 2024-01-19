# 서버로부터 데이터 가져오기 requests.get()

import requests
import pprint

api_key = 'e1e57090b37e24b798c041ec1c68e074'

city_name = "Seoul"

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
data = requests.get(url).json()

# #온도만 가져오기
# k = data['main']['temp']
# c = data['main']['temp'] - 273.15

# pprint.pprint(f'캘빈 온도: {k}')
    
# pprint.pprint(f'섭씨 온도: {c}')


#날씨 설명만 가져오기
description_data = data['weather'][0]['description']

pprint.pprint(f'날씨 설명: {description_data}')