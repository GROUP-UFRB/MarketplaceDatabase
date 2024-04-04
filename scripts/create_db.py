import pymongo
import json
import os
from collections import OrderedDict


DATA_BASE_URL = "mongodb://root:root@localhost:27017/"
DATA_BASE_NAME = "test"

client = pymongo.MongoClient(DATA_BASE_URL)
db = client[DATA_BASE_NAME]

def get_validations(folder_path:str):
    json_data = {}
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.endswith('.json'):
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                json_data[filename.split(".")[0]]=data

    return json_data



def run():
    validations = get_validations("../validations")
    for schame_name in validations:
        db[str(schame_name)].drop()
        db.create_collection(str(schame_name))
        cmd = OrderedDict([('collMod', schame_name),('validator', validations[str(schame_name)]),('validationLevel', 'moderate')])
        db.command(cmd)
        print(f"{schame_name}....OK")



if __name__ == "__main__":
    run()
