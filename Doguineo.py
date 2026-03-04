import requests
import webbrowser

API = "https://dog.ceo/api/breeds/image/random"

data = requests.get(API, timeout=10).json()

print(data)

image_url = data["message"]
 
webbrowser.open(image_url)