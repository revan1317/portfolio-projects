import json

with open('gras_blok.json', 'r') as file:
    data = json.load(file)

block = data['block']

block['snow'] = True

block['coordinates'] ['y'] += 66

block['coordinates']['z'] *= 3

with open('sneeuw_blok.json', 'w') as file:
    json.dump({"block": block}, file, indent=4)
