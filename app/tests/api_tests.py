from currency.models import Source, Rate

from decimal import Decimal

def test_get_rates(api_client_auth):
    url = '/api/v1/rates/'
    response = api_client_auth.get(url)
    assert response.status_code == 200
    assert response.json()

def test_post_invalid_rates(api_client_auth):
    url = '/api/v1/rates/'
    response = api_client_auth.post(url, json={})
    assert response.status_code == 400
    assert response.json() == {
        'buy': ['This field is required.'], 
        'sale': ['This field is required.'], 
        'source': ['This field is required.'], 
        'type': ['This field is required.']}

def test_post_valid_rates(api_client_auth):
    source = Source.objects.last()
    url = '/api/v1/rates/'
    json_data = {'buy': 1, 'sale': 1, 'source': source.pk, 'type': 'USD'}
    response = api_client_auth.post(url, data=json_data) 

    assert response.status_code == 201
    assert response.json()['buy'] == '1.00'
    assert response.json()['sale'] == '1.00'
    assert response.json()['source_obj']['id'] == 1
    assert response.json()['type'] == 'USD'

def test_update_rates(api_client_auth):
    source = Source.objects.last()
    rate = Rate.objects.last()
    url = f'/api/v1/rates/{rate.pk}/'
    json_data = {
            "buy": 1,
            "sale": 1,
            "type": "USD",
            "source": source.pk}
            
    response = api_client_auth.put(url, json_data, format='json')
    assert response.status_code == 200
    assert response.json()['buy'] == '1.00'
    assert response.json()['sale'] == '1.00'
    assert response.json()['source_obj']['id'] == source.pk
    assert response.json()['type'] == "USD"

    assert Rate.objects.last().buy == Decimal(1)
    assert Rate.objects.last().sale == Decimal(1)
    assert Rate.objects.last().source.pk == source.pk
    assert Rate.objects.last().type == "USD"


def test_delete(api_client_auth):
    initial_num_of_rates = Rate.objects.count()
    rate = Rate.objects.last()
    url = f'/api/v1/rates/{rate.pk}/'

    response = api_client_auth.delete(url)

    assert Rate.objects.count() == initial_num_of_rates - 1

