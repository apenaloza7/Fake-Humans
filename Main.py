from faker import Faker
from random import randint

"""
Module used to generate fake humans/tuples (names, addresses, emails, phone numbers, etc)
and write them to a text file

Author - Alejandro Penaloza UNCG
"""


def date_of_birth():
    dob: str = str(randint(1, 12)) + '-' + str(randint(1, 31)) + '-19' + str(randint(70, 99))
    return dob


def generate_data(n):
    # Initiating a constructor for the Faker library
    fake = Faker()

    # Open the file that's to be written to
    fake_humans_file = open("FakeHumans.txt", "w+")

    # Generates 'n' number of random people
    for i in range(0, n):
        fake_humans_file.write(str(fake.ssn()) + ','
                               + date_of_birth() + ','
                               + str(fake.first_name()) + ','
                               + str(fake.first_name()) + ','
                               + str(fake.last_name()) + ','
                               + str(fake.street_address()) + '\n')

    # Closing the file after done writing data
    fake_humans_file.close()


def run():
    # Variable for the number of people wanted
    num_of_people = 10

    # Calling method to generate text file
    generate_data(num_of_people)

    print("Done")


run()
