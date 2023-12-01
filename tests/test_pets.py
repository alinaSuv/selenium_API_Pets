import os.path

import pytest
import requests

from api import Pets

pet = Pets()


def test_register_user():
    status = pet.register_user()[0]
    assert status == 200

def test_double_register_user():
    status = pet.double_register_user()[0]
    returning_response = pet.double_register_user()[1]
    assert status == 400
    assert returning_response == "Username is taken or pass issue"

def test_delete_user():
    status = pet.delete_user()[1]
    #user_data = pet.delete_user()[0]
    assert status == 200

def test_negative_register_user_without_confirmation_password():
    status = pet.register_user_without_confirmation_password()[0]
    assert status == 422

def test_negative_register_user_with_dif_password():
    status = pet.register_user_with_dif_passwords()[0]
    returning_response = pet.register_user_with_dif_passwords()[1]
    assert status == 400
    assert returning_response == "Username is taken or pass issue"

def test_get_token():
    status = pet.get_token()[2]
    token = pet.get_token()[0]
    assert token
    assert status == 200

def test_login_with_invalid_email():
    status = pet.login_with_invalid_email()[1]
    returned_response = pet.login_with_invalid_email()[0]
    assert status == 400
    assert returned_response == "Username is taken or pass issue"

def test_login_with_invalid_password():
    status = pet.login_with_invalid_password()[1]
    returned_response = pet.login_with_invalid_password()[0]
    assert status == 400
    assert returned_response == "Username is taken or pass issue"

def test_get_users_list():
    status = pet.get_list_users()[0]
    user_id = pet.get_list_users()[1]
    assert status == 200
    assert user_id

def test_add_pet():
    status = pet.add_pet()[0]
    pet_id = pet.add_pet()[1]
    assert status == 200
    assert pet_id

def test_negative_add_pet():
    status = pet.add_pet_without_required_data()[0]
    assert status == 422

def test_edit_pet():
    status = pet.edit_pet()[0]
    pet_id = pet.edit_pet()[1]
    assert status == 200
    assert pet_id

def test_get_pet():
    status_get = pet.get_pet()[0]
    pet_data = pet.get_pet()[1]
    returned_pet_id = pet.get_pet()[2]
    assert status_get == 200
    assert pet_data
    assert returned_pet_id

def test_delete_pet():
    status = pet.delete_pet()[0]
    returned_response = pet.delete_pet()[1]
    assert status == 200
    assert len(returned_response) == 0

def test_add_like_pet():
    status = pet.add_pet_like()[0]
    returned_response = pet.add_pet_like()[1]
    assert status == 200

def test_pet_double_like():
    status = pet.add_pet_double_like()[0]
    #total_like_amount = pet.get_pet()[4]
    assert status == 200
    #assert total_like_amount == 1

def test_add_comment_pet():
    status = pet.add_pet_comment()[0]
    returned_pet_id = pet.add_pet_comment()[1]
    assert status == 200
    assert returned_pet_id

def test_add_pet_photo():
    status = pet.add_pet_photo()[0]
    link = pet.add_pet_photo()[1]
    assert status == 200
    assert link
    





