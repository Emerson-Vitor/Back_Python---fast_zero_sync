from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_should_return_ok_and_ola_mundo():
    # triple A - test
    client = TestClient(app)  # Arrange (oranização )
    response = client.get('/')  # act (ação)
    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'olá mundo'}
