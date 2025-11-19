import requests

nummer = input("Typ een getal:")
url = f"https://jsonplaceholder.typicode.com/todos/{38}"
response = requests.get(url)
data = response.json()
print(data["title"])
