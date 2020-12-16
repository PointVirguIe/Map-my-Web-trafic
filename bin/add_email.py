import json, sys

def add_email(email, frenquence, website):
    data_to_dump = {}

    try:
        with open('data/data.json') as json_file:
            data = json.load(json_file)
    except:
        with open('data/data.json', 'w') as json_file:
            json.dump(data_to_dump, json_file)

if len(sys.argv) != 2:
    exit(f"usage : {sys.argv[0]} fr_FR.json")

with open(sys.argv[1]) as fp:
    Keys1 = json.load(fp).keys()

with open("en_US.json") as fp:
    for key in json.load(fp).keys():
        if not key in Keys1:
            print(key)