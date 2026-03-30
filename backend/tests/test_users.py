import pytest

""" TODO:
- Create tests for creating user (valid, partial, invalid, edge cases?)
"""


# happy path
def test_new_user_creation_success(client):
    # valid params only for this test
    res = client.post(
        "/users/",
        json={
            "id": 1,
            first_name: "John",
            last_name: "Smith",
            email: "johnsmith@gmail.com",
        },
    )
