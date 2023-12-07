import json
from settings import LoginData
import requests


LD = LoginData()

class Pets:  # API library for http://34.141.58.52:8000/#/

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def register_user_and_delete(self) -> json:  # Request to Swagger for new user creation
        data = {"email": LD.REGISTER_USER_EMAIL,
                "password": LD.REGISTER_USER_PASSWORD, "confirm_password": LD.REGISTER_USER_PASSWORD}
        response = requests.post(self.base_url + 'register', data=json.dumps(data))
        registered_user_id = response.json()['id']
        user_token = response.json()['token']
        headers = {'Authorization': f'Bearer {user_token}'}
        params = {'id': registered_user_id}
        response = requests.delete(self.base_url + f'users/{registered_user_id}', headers=headers, params=params)
        status = response.status_code
        return status

    def double_register_user(self) -> json:
        data = {"email": LD.EMAIL_FOR_REGISTRATION,
                "password": LD.PASSWORD_FOR_REGISTRATION, "confirm_password": LD.PASSWORD_FOR_REGISTRATION}
        response = requests.post(self.base_url + 'register', data=json.dumps(data))
        status = response.status_code
        returning_response = response.json()['detail']
        return status, returning_response

    def register_user_without_confirmation_password(self) -> json:
        data = {"email": LD.REGISTER_USER_EMAIL,
                "password": LD.REGISTER_USER_PASSWORD}
        response = requests.post(self.base_url + 'register', data=json.dumps(data))
        status = response.status_code
        return status

    def register_user_with_dif_passwords(self) -> json:
        data = {"email": LD.REGISTER_USER_EMAIL,
                "password": LD.REGISTER_USER_PASSWORD, "confirm_password": f'invalid/{LD.REGISTER_USER_PASSWORD}'}
        response = requests.post(self.base_url + 'register', data=json.dumps(data))
        status = response.status_code
        returning_response = response.json()['detail']
        return status, returning_response


    def get_token(self) -> json:  # Request to Swagger for receiving: user-token for existing user using email and password
        data = {
            "email": LD.VALID_EMAIL,
            "password": LD.VALID_PASSWORD
        }
        response = requests.post(self.base_url + "login", data=json.dumps(data))
        user_token = response.json()['token']
        user_id = response.json()['id']
        status = response.status_code
        return user_token, user_id, status

    def login_with_invalid_email(self) -> json:
        data = {
            "email": f'invalid/{LD.VALID_EMAIL}',
            "password": LD.VALID_PASSWORD
        }
        response = requests.post(self.base_url + "login", data=json.dumps(data))
        returned_response = response.json()['detail']
        status = response.status_code
        return returned_response, status

    def login_with_invalid_password(self) -> json:
        data = {
            "email": LD.VALID_EMAIL,
            "password": f'invalid/{LD.VALID_PASSWORD}'
        }
        response = requests.post(self.base_url + "login", data=json.dumps(data))
        returned_response = response.json()['detail']
        status = response.status_code
        return returned_response, status

    def get_list_users(self):  # Request to Swagger for receiving: ID user
        user_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {user_token}'}
        response = requests.get(self.base_url + 'users', headers=headers)
        status = response.status_code
        user_id = response.text
        return status, user_id

    def add_pet(self):  # Request to Swagger for creation new pet
        user_token = Pets().get_token()[0]
        user_id = Pets().get_token()[1]
        headers = {'Authorization': f'Bearer {user_token}'}
        data = {"id": 0,
                "name": 'APet', "type": 'parrot', "age": 10, "owner_id": user_id
                }
        response = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        status = response.status_code
        pet_id = response.json()['id']
        return status, pet_id

    def add_pet_without_required_data(self):
        user_token = Pets().get_token()[0]
        user_id = Pets().get_token()[1]
        headers = {'Authorization': f'Bearer {user_token}'}
        data = {"id": 0,
                "type": 'parrot', "age": 10, "owner_id": user_id
                }
        response = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        status = response.status_code
        return status

    def get_pet(self):  # Request to Swagger for receiving: created pet
        user_token = Pets().get_token()[0]
        pet_id = Pets().add_pet()[1]
        headers = {'Authorization': f'Bearer {user_token}'}
        response = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        status_get = response.status_code
        returned_pet_details = response.json()
        pet_data = response.json()['pet']
        returned_pet_id = pet_data['id']
        likes_count = pet_data['likes_count']
        return status_get, pet_data, returned_pet_id, returned_pet_details, likes_count

    def edit_pet(self):
        user_token = Pets().get_token()[0]
        pet_id = Pets().add_pet()[1]
        headers = {'Authorization': f'Bearer {user_token}'}
        data = {"id": pet_id,
                "name": 'UpdatePet', "type": 'hamster', "age": 8
                }
        response = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        status = response.status_code
        pet_id = response.json()['id']
        return status, pet_id

    def delete_pet(self):
        user_token = Pets().get_token()[0]
        returned_pet_id = Pets().get_pet()[2]
        headers = {'Authorization': f'Bearer {user_token}'}
        response = requests.delete(self.base_url + f'pet/{returned_pet_id}', headers=headers)
        status = response.status_code
        returned_response = response.json()
        return status, returned_response

    def add_pet_like(self):
        user_token = Pets().get_token()[0]
        pet_id = Pets().get_pet()[2]
        like_count_after_creation = Pets().get_pet()[4]
        headers = {'Authorization': f'Bearer {user_token}'}
        response = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        status = response.status_code
        response = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        pet_data = response.json()['pet']
        returned_pet_id = pet_data['id']
        likes_count_final = pet_data['likes_count']
        return status, like_count_after_creation, returned_pet_id, likes_count_final

    def add_pet_double_like(self):
        user_token = Pets().get_token()[0]
        pet_id = Pets().add_pet_like()[2]
        headers = {'Authorization': f'Bearer {user_token}'}
        response = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        status = response.status_code
        returned_response = response.json()['detail']
        return status, returned_response

    def add_pet_comment(self):
        user_token = Pets().get_token()[0]
        pet_id = Pets().add_pet()[1]
        headers = {'Authorization': f'Bearer {user_token}'}
        data = {"message": "test string comment"}
        response = requests.put(self.base_url + f'pet/{pet_id}/comment', data=json.dumps(data), headers=headers)
        status = response.status_code
        response = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        pet_comment_data = response.json()['comments']
        pet_comment = pet_comment_data[0]
        pet_comment_text = pet_comment['message']
        return status, pet_comment_data, pet_comment_text

    def add_pet_photo(self):
        user_token = Pets().get_token()[0]
        pet_id = Pets().add_pet()[1]
        headers = {'Authorization': f'Bearer {user_token}'}
        files = {'pic': (
            'cat.jpg', open(r'C:/Users/manke/PycharmProjects/selenium_API_Pets/tests/photo/cat.jpg', 'rb'),
            'image/jpg')}
        response = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = response.status_code
        link = response.json()['link']
        return status, link


# Pets().register_user_and_delete()
# Pets().double_register_user()
# Pets().register_user_without_confirmation_password()
# Pets().register_user_with_dif_passwords()
# Pets().get_token()
# Pets().login_with_invalid_email()
# Pets().login_with_invalid_password()
# Pets().get_list_users()
# Pets().add_pet()
# Pets().add_pet_without_required_data()
# Pets().get_pet()
# Pets().edit_pet()
# Pets().delete_pet()
# Pets().add_pet_like()
# Pets().add_pet_double_like()
# Pets().add_pet_comment()
# Pets().add_pet_photo()