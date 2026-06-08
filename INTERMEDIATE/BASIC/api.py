# json api  get post http 
import requests
url =""
response = requests.get(url)
if response.status_code ==200:
  data = response.json()
  temperature = data['main']['temp']
  print(f" the temperature in the indore is {temperature}")
else :
  print("failed to retrieve data.")