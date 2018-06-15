import json

with open('local.json', 'r') as f:
    dict = json.load(f)
print(dict)