import json

unique = {}

with open("downtown-crosstown.json") as f:
    for line in f:
        data = json.loads(line)
        unique.setdefault(data["name"])

for key in iter(unique):
    print key 
