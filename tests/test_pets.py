import os.path

import pytest
import requests

from api import Pets

pet = Pets()


# Positive scenario: to check Registration and Deleting of user
@pytest.mark.smoke
def test_register_and_delete_user():
    status = pet.register_user_and_delete()
    assert status == 200

# Negative scenario: to check twice attempts to register the same user
@pytest.mark.regression
def test_double_register_user():
    status = pet.double_register_user()[0]
    returning_response = pet.double_register_user()[1]
    assert status == 400
    assert returning_response == "Username is taken or pass issue"

# Negative scenario: to check Registration without confirmation password
@pytest.mark.regression
def test_negative_register_user_without_confirmation_password():
    status = pet.register_user_without_confirmation_password()
    assert status == 422

# Negative scenario: to check Registration with different passwords
@pytest.mark.regression
def test_negative_register_user_with_dif_password():
    status = pet.register_user_with_dif_passwords()[0]
    returning_response = pet.register_user_with_dif_passwords()[1]
    assert status == 400
    assert returning_response == "Username is taken or pass issue"


# Positive scenario: to check Login and Receiving token
@pytest.mark.smoke
def test_get_token():
    status = pet.get_token()[2]
    token = pet.get_token()[0]
    assert token
    assert status == 200


# Negative scenario: to check Login attempt with invalid email
@pytest.mark.regression
def test_login_with_invalid_email():
    status = pet.login_with_invalid_email()[1]
    returned_response = pet.login_with_invalid_email()[0]
    assert status == 400
    assert returned_response == "Username is taken or pass issue"


# Negative scenario: to check Login attempt with invalid password
@pytest.mark.regression
def test_login_with_invalid_password():
    status = pet.login_with_invalid_password()[1]
    returned_response = pet.login_with_invalid_password()[0]
    assert status == 400
    assert returned_response == "Username is taken or pass issue"


# Positive scenario: to check Receiving usedID
@pytest.mark.smoke
def test_get_users_list():
    status = pet.get_list_users()[0]
    user_id = pet.get_list_users()[1]
    assert status == 200
    assert user_id


# Positive scenario: to check Creation pet
@pytest.mark.smoke
def test_add_pet():
    status = pet.add_pet()[0]
    pet_id = pet.add_pet()[1]
    assert status == 200
    assert pet_id


# Negative scenario: to check Creation pet without required data
@pytest.mark.regression
def test_negative_add_pet():
    status = pet.add_pet_without_required_data()
    assert status == 422


# Positive scenario: to check Editing pet
@pytest.mark.smoke
def test_edit_pet():
    status = pet.edit_pet()[0]
    pet_id = pet.edit_pet()[1]
    assert status == 200
    assert pet_id


# Positive scenario: to check Receiving pet details
@pytest.mark.smoke
def test_get_pet():
    status_get = pet.get_pet()[0]
    pet_data = pet.get_pet()[1]
    returned_pet_id = pet.get_pet()[2]
    assert status_get == 200
    assert pet_data
    assert returned_pet_id


# Positive scenario: to check Deletion pet
@pytest.mark.regression
def test_delete_pet():
    status = pet.delete_pet()[0]
    returned_response = pet.delete_pet()[1]
    assert status == 200
    assert len(returned_response) == 0


# Positive scenario: to check possibility to add like for pet (also check that after creation of pet likes count = 0, after adding like likes coint =1
@pytest.mark.smoke
def test_add_like_pet():
    status = pet.add_pet_like()[0]
    start_like_count = pet.add_pet_like()[1]
    final_like_count = pet.add_pet_like()[3]
    assert status == 200
    assert start_like_count == 0
    assert final_like_count == 1


# Negative scenario: to check possibility to add double like for pet
@pytest.mark.regression
def test_pet_double_like():
    status = pet.add_pet_double_like()[0]
    returned_response = pet.add_pet_double_like()[1]
    assert status == 403
    assert returned_response == "You already liked it"


# Positive scenario: to check possibility to add comment for pet
@pytest.mark.smoke
def test_add_comment_pet():
    status = pet.add_pet_comment()[0]
    pet_comment = pet.add_pet_comment()[2]
    assert status == 200
    assert pet_comment == "test string comment"


# Positive scenario: to check possibility to add photo for pet
@pytest.mark.smoke
def test_add_pet_photo():
    status = pet.add_pet_photo()[0]
    link = pet.add_pet_photo()[1]
    assert status == 200
    assert link
    





