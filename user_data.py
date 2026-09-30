
from faker import Faker

fake = Faker()

class Credentials:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

def generate_random_credentials(user_name):
        email = fake.email()
        password = fake.password(length=10, special_chars=False, digits=True)

        return Credentials(name=user_name, email=email, password=password)

def get_static_credentials():
        
        return Credentials(name='Татьяна', email='TatianaAseeva54@yandex.ru', password='testUIstart')
        