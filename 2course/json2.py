import json

task = ["oleg",24,["Belarus","Russia"]]

with open("surname_1.json", "w") as f:
    json.dump({"name": task[0], "age": task[1], "countries": task[2]}, f, indent=4)
