import pytest
from playwright.sync_api import sync_playwright

BASE_URL = 'https://practicetestautomation.com'

@pytest.fixture(scope='function')
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

class TestLogin:

    def test_login_page_loads(self, page):
        page.goto(BASE_URL + '/practice-test-login/')
        assert 'Practice' in page.title()

    def test_valid_login(self, page):
        page.goto(BASE_URL + '/practice-test-login/')
        page.fill('#username', 'student')
        page.fill('#password', 'Password123')
        page.click('#submit')
        assert 'Logged In Successfully' in page.locator('h1').inner_text()

    def test_invalid_username(self, page):
        page.goto(BASE_URL + '/practice-test-login/')
        page.fill('#username', 'wronguser')
        page.fill('#password', 'Password123')
        page.click('#submit')
        assert page.locator('#error').is_visible()

    def test_invalid_password(self, page):
        page.goto(BASE_URL + '/practice-test-login/')
        page.fill('#username', 'student')
        page.fill('#password', 'wrongpassword')
        page.click('#submit')
        assert page.locator('#error').is_visible()

    def test_empty_credentials(self, page):
        page.goto(BASE_URL + '/practice-test-login/')
        page.click('#submit')
        assert page.locator('#error').is_visible()

    @pytest.mark.parametrize('username,password,expected', [
        ('student', 'Password123', True),
        ('wronguser', 'Password123', False),
        ('student', 'wrongpass', False),
    ])
    def test_login_data_driven(self, page, username, password, expected):
        page.goto(BASE_URL + '/practice-test-login/')
        page.fill('#username', username)
        page.fill('#password', password)
        page.click('#submit')
        if expected:
            assert 'Logged In Successfully' in page.locator('h1').inner_text()
        else:
            assert page.locator('#error').is_visible()
