import pytest

def test_sanity():
    assert 200 == 200


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200