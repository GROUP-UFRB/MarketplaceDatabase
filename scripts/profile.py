

import json
from faker import Faker
import random


fake = Faker()
profiles = []

def generate_cpf():
    numbers = [str(random.randint(0, 9)) for _ in range(11)]
    return ''.join(numbers)

for i in range(30000):  # CHANGE TO 30k
    profiles.append({
        "userId": "-1",
        "cpf": generate_cpf(),
        "name": fake.name(),
        "contact": {
            "email": fake.email(),
            "number": fake.phone_number()
        },
        "address": {
            "zipCode": fake.postcode(),
            "state": fake.country(),
            "city": fake.city(),
            "district": fake.street_suffix(),
            "street": fake.street_address(),
            "number": fake.building_number(),
        },
        "jobs": [],
        "availability": True
    })


with open("data/profiles.json", 'w', encoding='utf-8') as file:
    json.dump(profiles, file, ensure_ascii=False)
