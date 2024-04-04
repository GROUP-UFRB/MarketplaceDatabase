

import json

jobs = []

with open('seeds/jobs_names.json') as file:
    data = json.load(file)
    print(f"JOBS:{len(data)}")
    for name in data:
        jobs.append({
            "name": name,
            "area": "Construção Civil"
        })


with open("data/jobs.json", 'w',encoding='utf-8') as file:
    json.dump(jobs, file,ensure_ascii=False)
