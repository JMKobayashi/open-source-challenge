import pytest
import requests
import json

def test_empty_list_organizations():

    response = requests.get('http://localhost:8000/api/orgs/')
    assert response.status_code == 404


@pytest.mark.parametrize(
    'login,status',[
        ('instruct-br',200), # Succes
        ('adobe',200), # Succes
        ('Netflix',200), # Succes
        ('instruct',200), # Succes Nome vazio
        ('twitter',200), # Succes
        ('RedHatOfficial',200), # Succes
        ('adsgser',404), # Error 404 Organização não encontrada
        ('123456',404), # Error 404 Organização não encontrada
        ('testestestestes',404), # Error 404 Organização não encontrada
        ('fase5qwe',404) # Error 404 Organização não encontrada
    ]
)

def test_get_organization(login,status):

    response = requests.get('http://localhost:8000/api/orgs/'+login)
    assert response.status_code == status

def test_list_organization():

    response = requests.get('http://localhost:8000/api/orgs/')
    assert response.status_code == 200

@pytest.mark.parametrize(
    'login,status',[
        ('instruct-br',204), # Succes
        ('adobe',204), # Succes
        ('Netflix',204), # Succes
        ('instruct',204), # Succes Nome vazio
        ('twitter',204), # Succes
        ('RedHatOfficial',204), # Succes
        ('adsgser',404), # Error 404 Organização não encontrada
        ('123456',404), # Error 404 Organização não encontrada
        ('testestestestes',404), # Error 404 Organização não encontrada
        ('fase5qwe',404) # Error 404 Organização não encontrada
    ]
)

def test_delete_organization(login,status):

    response = requests.delete('http://localhost:8000/api/orgs/'+login)
    assert response.status_code == status