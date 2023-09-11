from rest_framework.test import APIClient
from currency.models import Source

def test_get_rates():
    client = APIClient()
    url = '/api/v1/rates/'
    response = client.get(url)
    assert response.status_code == 200
    assert response.json()

def test_post_invalid_rates():
    client = APIClient()
    url = '/api/v1/rates/'
    response = client.post(url, json={})
    assert response.status_code == 400
    assert response.json() == {
        'buy': ['This field is required.'], 
        'sale': ['This field is required.'], 
        'source': ['This field is required.'], 
        'type': ['This field is required.']}

def test_post_valid_rates():
    client = APIClient()
    source = Source.objects.last()
    url = '/api/v1/rates/'
    json_data = {'buy': 1, 'sale': 1, 'source': source.pk, 'type': 'USD'}
    response = client.post(url, data=json_data) 

    assert response.status_code == 201
    assert response.json()['buy'] == '1.00'
    assert response.json()['sale'] == '1.00'
    assert response.json()['source_obj']['id'] == 1
    assert response.json()['type'] == 'USD'