import pytest
from currency.models import ContactUs

CONTACTUS_URL = '/currency/contactus/create/'


def test_get_contactus(client):
    response = client.get(CONTACTUS_URL)
    assert response.status_code == 200


def test_post_empty_form(client):
    contactus_initial_count = ContactUs.objects.count()
    response = client.post(CONTACTUS_URL, data={})

    #Everything worked (nothing worked that`s good!) because if django form is wrong, django returns 200
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
    'email_to': ['This field is required.'], 
    'subject': ['This field is required.'], 
    'body': ['This field is required.']
    }
    assert  ContactUs.objects.count() == contactus_initial_count


def test_invalid_form(client):
    contactus_initial_count = ContactUs.objects.count()
    form_data = {
        'email_to': "invalid/email",
        'subject': 'test_subject' * 100,
        'body': 'test body'        
    }
    response = client.post(CONTACTUS_URL, data=form_data)

    #Everything worked (nothing worked that`s good!) because if django form is wrong, django returns 200
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email_to': ['Enter a valid email address.'], 'subject' : ['Ensure this value has at most 32 characters (it has 1200).']
    }
    assert  ContactUs.objects.count() == contactus_initial_count


def test_valid_form(client):
    contactus_initial_count = ContactUs.objects.count()
    form_data = {
        'email_to': "test_email@example.com",
        'subject': 'test_subject',
        'body': 'test body'        
    }
    response = client.post(CONTACTUS_URL, data=form_data)

    assert response.status_code == 302
    assert response.url == '/'
    assert ContactUs.objects.count() == (contactus_initial_count+1)
    contact_us_obj = ContactUs.objects.last()
    assert contact_us_obj.email_to == form_data['email_to']
    assert contact_us_obj.subject == form_data['subject']    
    assert contact_us_obj.body == form_data['body']