import pytest
from API_actions.login_api import login_api, get_token
from API_actions.user_api import get_user_profile
from utils.csv_reader import read_csv


@pytest.mark.parametrize("user", read_csv("testdata/api/test_data.csv"))
def test_user_flow(user):
    login_response = login_api(user["username"], user["password"])
    print("Login Response:", login_response.text)

    assert login_response.status_code == 200

    token = get_token(login_response)
    print("Token:", token)

    assert token is not None

    profile_response = get_user_profile(token)
    print("Profile Response:", profile_response.text)

    assert profile_response.status_code == 200