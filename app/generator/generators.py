"""
This is the user_seed module.
Intended to contain all user-related functionality for the Trek project user blueprint.
Populates the database with users made from a csv file of phony user data.
"""
import csv
import random
import requests
from datetime import datetime
import string
from json_trek import JSONTrek 


USERS_CSV_HEADERS = ['email', 'username', 'profile_pic', 'bio', 'first_name', 'last_name', 'location']
NUM_USERS = 1000

trek = JSONTrek()

def generate_users_csv(file_path):
    image_urls = [
        f"https://randomuser.me/api/portraits/{kind}/{i}.jpg"
        for kind, count in [("lego", 10), ("men", 100), ("women", 100)]
        for i in range(count)
    ]

    with open(file_path, 'w') as users_csv:
        users_writer = csv.DictWriter(users_csv, fieldnames=USERS_CSV_HEADERS)
        users_writer.writeheader()

        for i in range(NUM_USERS):
            first_name = trek.user_profile(['first_name'])
            last_name = trek.user_profile(['last_name'])
            email = trek.email()
            address = trek.address()
            city = address['city']
            
            users_writer.writerow(dict(
                email=email,
                username=trek.username(),
                profile_pic=random.choice(image_urls),
                bio=trek.ipsum(100),
                first_name=first_name,
                last_name=last_name,
                location=city
            ))

if __name__ == '__main__':
    generate_users_csv('app/seed/users.csv')
