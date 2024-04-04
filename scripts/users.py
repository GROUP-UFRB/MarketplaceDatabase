

import json
from faker import Faker
import random


fake = Faker()
users = []

userTypes = ['admin',
             'manager',
             'client',
             'teamMember']

def generate_password():
    numbers = [str(random.randint(0, 9)) for _ in range(11)]
    return ''.join(numbers)


for i in range(100): 
    users.append({
        "password": generate_password(),
        "email": fake.email(),
        "userType":random.choice(userTypes)
    })


with open("data/users.json", 'w', encoding='utf-8') as file:
    json.dump(users, file, ensure_ascii=False)
