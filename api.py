import json
from settings import VALID_EMAIL, VALID_PASSWORD, PASSWORD_FOR_REGISTRATION, EMAIL_FOR_REGISTRATION
import requests


class Pets:  # API library for http://34.141.58.52:8000/#/

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def register_user(self) -> json:  # Request to Swagger for new user creation
        data = {"email": EMAIL_FOR_REGISTRATION,
                "password": PASSWORD_FOR_REGISTRATION, "confirm_password": PASSWORD_FOR_REGISTRATION}
        response = requests.post(self.base_url + 'register', data=json.dumps(data))
        status = response.status_code
        user_data = response.json()
        registered_user_id = response.json()['id']
        # user_token = response.json()['token']
        # user_email = response.json()['email']
        print(user_data, registered_user_id)
        return status, registered_user_id

    def get_token_for_created_user(self) -> json:  # Request to Swagger for receiving token for just created user
        data = {"email": EMAIL_FOR_REGISTRATION,
                "password": PASSWORD_FOR_REGISTRATION}
        print(data)
        response = requests.post(self.base_url + "login", data=json.dumps(data))
        user_token = response.json()['token']
        user_id = response.json()['id']
        status = response.status_code
        print(user_token, user_id)
        return status, user_token, user_id

    def delete_user(self) -> json:  # Request to Swagger for user deleting
        user_token = Pets().get_token_for_created_user()[1]
        user_id = Pets().get_token_for_created_user()[2]
        headers = {'Authorization': f'Bearer {user_token}'}
        response = requests.delete(self.base_url + f'users/{user_id}', headers=headers)
        user_data = response.json()
        status = response.status_code
        print(user_data)
        return user_data, status

    def double_register_user(self) -> json:
        data = {"email": EMAIL_FOR_REGISTRATION,
                "password": PASSWORD_FOR_REGISTRATION, "confirm_password": PASSWORD_FOR_REGISTRATION}
        response = requests.post(self.base_url + 'register', data=json.dumps(data))
        status = response.status_code
        returning_response = response.json()['detail']
        print(returning_response)
        return status, returning_response

    def register_user_without_confirmation_password(self) -> json:
        data = {"email": EMAIL_FOR_REGISTRATION,
                "password": PASSWORD_FOR_REGISTRATION}
        response = requests.post(self.base_url + 'register', data=json.dumps(data))
        status = response.status_code
        returning_response = response.json()
        print(returning_response)
        return status, returning_response

    def register_user_with_dif_passwords(self) -> json:
        data = {"email": EMAIL_FOR_REGISTRATION,
                "password": PASSWORD_FOR_REGISTRATION, "confirm_password": f'invalid/{PASSWORD_FOR_REGISTRATION}'}
        response = requests.post(self.base_url + 'register', data=json.dumps(data))
        status = response.status_code
        returning_response = response.json()['detail']
        print(returning_response)
        return status, returning_response




    def get_token(self) -> json:  # Request to Swagger for receiving: user-token for existing user using email and password
        data = {
            "email": VALID_EMAIL,
            "password": VALID_PASSWORD
        }
        response = requests.post(self.base_url + "login", data=json.dumps(data))
        user_token = response.json()['token']
        user_id = response.json()['id']
        status = response.status_code
        print(user_token)
        print(response.json())
        return user_token, user_id, status

    def login_with_invalid_email(self) -> json:
        data = {
            "email": f'invalid/{VALID_EMAIL}',
            "password": VALID_PASSWORD
        }
        response = requests.post(self.base_url + "login", data=json.dumps(data))
        returned_response = response.json()['detail']
        status = response.status_code
        print(response.json())
        return returned_response, status

    def login_with_invalid_password(self) -> json:
        data = {
            "email": VALID_EMAIL,
            "password": f'invalid/{VALID_PASSWORD}'
        }
        response = requests.post(self.base_url + "login", data=json.dumps(data))
        returned_response = response.json()['detail']
        status = response.status_code
        print(response.json())
        return returned_response, status

    def get_list_users(self):  # Request to Swagger for receiving: ID user
        user_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {user_token}'}
        response = requests.get(self.base_url + 'users', headers=headers)
        status = response.status_code
        user_id = response.text
        print(response.json())
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
        print(pet_id)
        print(response.json())
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
        pet_response = response.json()
        print(pet_response)
        print(response.json())
        return status, pet_response

    def get_pet(self):  # Request to Swagger for receiving: created pet
        user_token = Pets().get_token()[0]
        user_id = Pets().get_token()[1]
        pet_id = Pets().add_pet()[1]
        headers = {'Authorization': f'Bearer {user_token}'}
        response = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        status_get = response.status_code
        returned_pet_details = response.json()
        pet_data = response.json()['pet']
        returned_pet_id = pet_data['id']
        likes_count = pet_data['likes_count']
        print(pet_data)
        print(returned_pet_id)
        print(likes_count)
        return status_get, pet_data, returned_pet_id, returned_pet_details, likes_count

    def edit_pet(self):
        user_token = Pets().get_token()[0]
        user_id = Pets().get_token()[1]
        pet_id = Pets().add_pet()[1]
        headers = {'Authorization': f'Bearer {user_token}'}
        data = {"id": pet_id,
                "name": 'UpdatePet', "type": 'hamster', "age": 8, "owner_id": user_id
                }
        response = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        status = response.status_code
        pet_id = response.json()['id']
        print(pet_id)
        print(response.json())
        return status, pet_id

    def delete_pet(self):
        user_token = Pets().get_token()[0]
        user_id = Pets().get_token()[1]
        pet_id = Pets().add_pet()[1]
        returned_pet_id = Pets().get_pet()[2]
        headers = {'Authorization': f'Bearer {user_token}'}
        response = requests.delete(self.base_url + f'pet/{returned_pet_id}', headers=headers)
        status = response.status_code
        returned_response = response.json()
        print(returned_response)
        return status, returned_response

    def add_pet_like(self):
        user_token = Pets().get_token()[0]
        user_id = Pets().get_token()[1]
        pet_id = Pets().add_pet()[1]
        headers = {'Authorization': f'Bearer {user_token}'}
        response = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        status = response.status_code
        returned_response = response.json()
        print(returned_response)
        return status, returned_response

    def add_pet_double_like(self):
        user_token = Pets().get_token()[0]
        pet_like = Pets().add_pet_like()[0]
        returned_pet_id = Pets().get_pet()[2]
        likes_count = Pets().get_pet()[4]
        headers = {'Authorization': f'Bearer {user_token}'}
        response = requests.put(self.base_url + f'pet/{returned_pet_id}/like', headers=headers)
        status = response.status_code
        returned_response = response.json()
        print(returned_response)
        return status, returned_response

    def add_pet_comment(self):
        user_token = Pets().get_token()[0]
        user_id = Pets().get_token()[1]
        pet_id = Pets().add_pet()[1]
        headers = {'Authorization': f'Bearer {user_token}'}
        data = {"message": "test string comment"}
        response = requests.put(self.base_url + f'pet/{pet_id}/comment', data=json.dumps(data), headers=headers)
        status = response.status_code
        returned_response = response.json()
        print(returned_response)
        return status, returned_response

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
        print(response.json())
        return status, link
