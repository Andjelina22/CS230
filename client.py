import random
import requests

endpoint = random.randint(1, 3)

url = f"http://127.0.0.1:5000/endpoint{endpoint}"

message = f"Hello endpoint {endpoint}"
print("Poslata poruka:", message)

response = requests.get(url)

print("Odgovor servera:", response.text)