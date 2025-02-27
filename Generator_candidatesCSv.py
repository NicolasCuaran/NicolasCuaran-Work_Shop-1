import csv
import random
import os
from faker import Faker

fake = Faker()

seniority_levels = ["Junior", "Mid", "Senior"]
technologies = ["Python", "Java", "JavaScript", "C++", "Ruby", "PHP", "C#", "Go", "Swift","Html",""]

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "candidates.csv")

with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([
        "First Name", "Last Name", "Email", "Country",
        "Application Date", "Yoe", "Seniority", "Technology",
        "Code Challenge Score", "Technical Interview"
    ])
    
    for _ in range(50000):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        country = fake.country()
        application_date = fake.date_between(start_date='-2y', end_date='today')
        yoe = random.randint(0, 30)
        seniority = random.choice(seniority_levels)
        technology = random.choice(technologies)
        code_challenge_score = random.randint(0, 100)
        technical_interview = random.randint(0, 10)
        
        writer.writerow([
            first_name, last_name, email, country,
            application_date.strftime("%Y-%m-%d"), yoe, seniority, technology,
            code_challenge_score, technical_interview
        ])
