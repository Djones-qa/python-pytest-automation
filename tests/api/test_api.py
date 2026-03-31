import pytest
import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'

class TestUsersAPI:

    def test_get_all_users(self):
        response = requests.get(BASE_URL + '/users')
        assert response.status_code == 200
        assert len(response.json()) == 10

    def test_get_single_user(self):
        response = requests.get(BASE_URL + '/users/1')
        assert response.status_code == 200
        data = response.json()
        assert data['id'] == 1
        assert 'name' in data
        assert 'email' in data

    def test_user_schema(self):
        response = requests.get(BASE_URL + '/users/1')
        data = response.json()
        required_fields = ['id', 'name', 'username', 'email', 'phone', 'website']
        for field in required_fields:
            assert field in data

    def test_invalid_user_returns_404(self):
        response = requests.get(BASE_URL + '/users/9999')
        assert response.status_code == 404

    @pytest.mark.parametrize('user_id', [1, 2, 3, 4, 5])
    def test_multiple_users(self, user_id):
        response = requests.get(BASE_URL + '/users/' + str(user_id))
        assert response.status_code == 200
        assert response.json()['id'] == user_id

class TestPostsAPI:

    def test_get_all_posts(self):
        response = requests.get(BASE_URL + '/posts')
        assert response.status_code == 200
        assert len(response.json()) == 100

    def test_create_post(self):
        payload = {'title': 'Python Test Post', 'body': 'Created by pytest', 'userId': 1}
        response = requests.post(BASE_URL + '/posts', json=payload)
        assert response.status_code == 201
        assert response.json()['title'] == 'Python Test Post'

    def test_update_post(self):
        payload = {'title': 'Updated Title', 'body': 'Updated body', 'userId': 1}
        response = requests.put(BASE_URL + '/posts/1', json=payload)
        assert response.status_code == 200
        assert response.json()['title'] == 'Updated Title'

    def test_delete_post(self):
        response = requests.delete(BASE_URL + '/posts/1')
        assert response.status_code == 200

    def test_response_time(self):
        response = requests.get(BASE_URL + '/posts')
        assert response.elapsed.total_seconds() < 2.0
