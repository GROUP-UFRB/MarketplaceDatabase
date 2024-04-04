import json

services = []

with open('seeds/services.json') as file:
    data = json.load(file)
    count=0
    for item in data:
        for service in item["services"]:
            count=count+1
            services.append({
            "name":service,
            "job_name":item["job"]
            })
    print(f"Services:{count}")


with open("data/services.json", 'w',encoding='utf-8') as file:
    json.dump(services, file,ensure_ascii=False)
