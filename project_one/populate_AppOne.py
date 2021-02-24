import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project_one.settings')

import django
django.setup()

import random
from AppOne.models import Users
from faker import Faker
faker = Faker()
from AppOne.models import Users

def populate(N=5):
    for n in range(N):
        fake_name = faker.name().split()
        fname = faker.first_name()
        lname = faker.last_name()
        mail = faker.email()

        user = Users.objects.get_or_create(first_name=fname,last_name=lname,email=mail)[0]

if __name__ == "__main__":
    print("Executing populate script")
    populate(10)
    print("Populate done!")