import json
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="")
cur = conn.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS python_novice")
cur.execute("USE python_novice")
cur.execute("""CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    gender CHAR(1),
    age INT,
    fav_color VARCHAR(50)
)""")

with open("gebruikers.json") as f:
    for u in json.load(f):
        cur.execute("INSERT INTO users (name, gender, age, fav_color) VALUES (%s, %s, %s, %s)",
                    (u["name"], u["gender"], u["age"], u["fav_color"]))

conn.commit()
conn.close()
print("Geslaagd!")
