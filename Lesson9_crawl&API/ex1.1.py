## ex1 weather

import requests
import json

url = 'https://www.metaweather.com/api/location/2306179/'
response = requests.get(url)

with open('weather.json','w+', encoding='utf-8-sig') as f:
    f.write(response.text)

with open('weather.json',encoding='utf-8-sig') as f:
    res = json.load(f)    
    with open('weather.txt','w+',encoding='utf-8-sig') as g:
        for i in range(len(res['consolidated_weather'])):
            weather=res['consolidated_weather'][i]['weather_state_name']
            line = weather+"\n"
            a=str(i+18)
            text=a+": "+line
            g.write(text)
            
