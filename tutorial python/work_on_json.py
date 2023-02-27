import json

data = '{"var1":"Herry", "var2":"56 subhash"}'

parsed = json.loads(data)
print(parsed)
# # s= json.load("s.json","r")
# # print(s) galat trika h
# print(parsed['var1'])

# # Task 1= json.load?
# print(type(parsed))


# import json

print("Started Reading JSON file")
with open("s.json", "r") as read_file:
    print("Converting JSON encoded data into Python dictionary")
    developer = json.load(read_file)

    print("Decoded JSON Data From File")
    for key, value in developer.items():
        print(key, ":", value)
    print("Done reading json file")


#     import json

developerJsonString = """{
    "name": "jane doe",
    "salary": 9000,
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "JaneDoe@pynative.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}
"""

# print("Started converting JSON string document to Python dictionary")
# developerDict = json.loads(developerJsonString)

# print("Printing key and value")
# print(developerDict["name"])
# print(developerDict["salary"])
# print(developerDict["skills"])
# print(developerDict["email"])
# print(developerDict["projects"])

# print("Done converting JSON string document to a dictionary")

data2 = {
    "Channel_name": "CodeWithHerry",
    "cars":['bmd','audi a8','ferrari'],
    "fridge":('roti', 540,'chawal'),
    "isbad": False
}

jscop = json.dumps(data2)
print(jscop)

# Task2 = what is shot_keys parameter in dumps

with open("sample.json", "w") as outfile:
    json.dump(data2, outfile)