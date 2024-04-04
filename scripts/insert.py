import pymongo
import json
import random
from faker import Faker

DATA_BASE_URL = "mongodb://root:root@localhost:27017/"
DATA_BASE_NAME = "test"

client = pymongo.MongoClient(DATA_BASE_URL)
db = client[DATA_BASE_NAME]
fake = Faker()


def insert_profiles(jobs, services):
     with open('data/profiles.json') as file:
        data = json.load(file)
        payload_profile = []
        payload_users=[]
        count=0
        size=len(data)-1
        for profile in data:
            print(f"Profiles...{count}/{size}")
            count=count+1
            select_jobs=[]
            n_jobs = random.randint(1, 5)
            for i in range(n_jobs):
                job_index=random.randint(0, len(jobs)-1)
                job=dict(jobs[job_index])
                job["id"]=job["_id"]
                del job["_id"]
                select_services=[]
                n_services=random.randint(1, 3)
                job_services_type = list(filter( lambda item: item["job_id"]==job["id"], services))
                for i in range(n_services):
                    service_index=random.randint(0, len(job_services_type)-1)
                    service=dict(job_services_type[service_index])
                    service["id"]=service["_id"]
                    del service["job_id"]
                    del service["_id"]
                    select_services.append(service)
                job["services"]=select_services
                select_jobs.append(job)
            profile["jobs"]=select_jobs
            payload_users.append({
                "email":profile["contact"]["email"],
                "password": fake.phone_number(),
                "userType":"employee"
            })
            payload_profile.append(profile)

        db_result_users = db["users"].insert_many(payload_users)
        index = 0
        profiles_to_insert=[]
        for id in db_result_users.inserted_ids:
            item = payload_profile[index]
            item["userId"] = id
            profiles_to_insert.append(item)
            index = index+1        
        db_result_profiles = db["profile"].insert_many(profiles_to_insert)





def insert_services(jobs):
    result = []
    with open('data/services.json') as file:
        data = json.load(file)
        payload = []
        for service in data:
            job = next(
                (item for item in jobs if item["name"] == service["job_name"]), False)
            if job:
                payload.append({
                    "name": service["name"],
                    "job_id": job["_id"],
                })
        db_result = db["service"].insert_many(payload)
        index = 0
        for id in db_result.inserted_ids:
            item = payload[index]
            item["_id"] = id
            result.append(item)
            index = index+1
    return result


def insert_jobs():
    result = []
    with open('data/jobs.json') as file:
        data = json.load(file)
        payload = db["jobs"].insert_many(data)
        index = 0
        for id in payload.inserted_ids:
            item = data[index]
            item["_id"] = id
            result.append(item)
            index = index+1
    return result

def insert_users():
    result = []
    with open('data/users.json') as file:
        data = json.load(file)
        payload = db["users"].insert_many(data)
        index = 0
        for id in payload.inserted_ids:
            item = data[index]
            item["_id"] = id
            result.append(item)
            index = index+1
    return result



def run():
    jobs = insert_jobs()
    services = insert_services(jobs)
    insert_profiles(jobs, services)
    insert_users()

if __name__ == "__main__":
    run()
