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

POSTS_CSV_HEADERS = ['title', 'body', 'user_id']
USERS_CSV_HEADERS = ['email', 'username', 'profile_pic', 'bio', 'first_name', 'last_name', 'location']
TAGS_CSV_HEADERS = ['post_id', 'tag_id']
NUM_USERS = 1000
NUM_POST = 5000
POST_TAGS = 10000
tags_list = [
    "Starfleet",
    "Warp",
    "Captain",
    "Enterprise",
    "Phaser",
    "Transporter",
    "Alien",
    "Federation",
    "Klingon",
    "Spock",
    "Vulcan",
    "Communicator",
    "Tribble",
    "Tricorder",
    "Borg",
    "Holodeck",
    "Romulan",
    "Warp Core",
    "Redshirt",
    "Q",
    "Tribble",
    "Holodeck",
    "Trill",
    "Cardassian",
    "Ferengi",
    "Andorian",
    "Bajoran",
    "Gorn",
    "Jem'Hadar",
    "Klingon Bird-of-Prey",
    "Vorta",
    "Xenomorph",
    "Zefram Cochrane",
    "Kobayashi Maru",
    "Prime Directive",
    "Omega Particle",
    "Temporal Prime Directive",
    "Ketracel White",
    "Dilithium",
    "Latinum",
    "PADD",
    "Starship",
    "Phaser Array",
    "Pon Farr",
    "Trill Symbiont",
    "Gamma Quadrant",
    "Delta Quadrant",
    "Neutral Zone",
    "Wormhole",
    "Chroniton",
    "Qapla'",
]

trek = JSONTrek()

def generate_users_csv(file_path):
    image_urls = [
        f"https://randomuser.me/api/portraits/{kind}/{i}.jpg"
        for kind, count in [("lego", 10), ("men", 100), ("women", 100)]
        for i in range(count)
    ]

    # if the file already exists, then exit
    try:
        with open(file_path, 'r') as users_csv:
            print("File already exists, exiting.")
            return
    except FileNotFoundError:
        pass
    
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
            
def generate_posts_csv(file_path):
    # if the file already exists, then exit
    
    try:
        with open(file_path, 'r') as posts_csv:
            print("File already exists, exiting.")
            return
    except FileNotFoundError:
        pass
    with open(file_path, 'w') as posts_csv:
        posts_writer = csv.DictWriter(posts_csv, fieldnames=POSTS_CSV_HEADERS)
        posts_writer.writeheader()
        for i in range(5000):
            random_user = random.randint(1, NUM_USERS + 1)
            title = trek.ipsum(10)
            body = random.randint(1, 10) * trek.ipsum(100)
            posts_writer.writerow(dict(
                title=title,
                body=body,
                user_id=random_user,
            ))
            
import random

def generate_post_tags_csv(file_path):
    total_tags = len(tags_list)
    tags_weights = [1] * total_tags # Equal weights to start
    # Modify weights to create a roulette-like distribution
    for i in range(total_tags):
        tags_weights[i] = total_tags - i 
    # try:
    #     with open(file_path, 'r') as tags_csv:
    #         print("File already exists, exiting.")
    #         return
    # except FileNotFoundError:
    #     pass
    
    with open(file_path, 'w') as tags_csv:
        tags_writer = csv.DictWriter(tags_csv, fieldnames=TAGS_CSV_HEADERS)
        tags_writer.writeheader()
        
        for i in range(1000000):
            post_id = random.randint(1, NUM_POST + 1)
            
            tag_id = random.choices(range(1, total_tags + 1), weights=tags_weights)[0]
            
            tags_writer.writerow(dict(
                post_id=post_id,
                tag_id=tag_id
            ))

if __name__ == '__main__':
    generate_users_csv('app/seeds/users.csv')
    generate_posts_csv('app/seeds/posts.csv')
    generate_post_tags_csv('app/seeds/post_tags.csv')