import mysql.connector
import requests

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

cur = conn.cursor()

cur.execute("create database if not exists pokemon")
cur.execute("use pokemon")

cur.execute("""
CREATE TABLE IF NOT EXISTS pokemon (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    weight INT,
    height INT
)
""")

for i in range(1, 152):
    url = f"https://pokeapi.co/api/v2/pokemon/{i}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        poke_id = data["id"]
        name = data["name"]
        weight = data["weight"]
        height = data["height"]

        cur.execute(
            "INSERT INTO pokemon (id, name, weight, height) VALUES (%s, %s, %s, %s)",
            (poke_id, name, weight, height)
        )
    else:
        print(f"Fout bij Pokémon {i}")

conn.commit()
conn.close()
print("Succes! Alle pokemon zijn gevangen!")
