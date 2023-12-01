from faker import Faker

VALID_EMAIL = "mankevichalina2+10@gmail.com"
VALID_PASSWORD = "tester1"

EMAIL_FOR_REGISTRATION = "mankevichalina2+13@gmail.com"
PASSWORD_FOR_REGISTRATION = "tester2"

fake = Faker()

REGISTER_USER_EMAIL = fake.email()
REGISTER_USER_PASSWORD = fake.password()



