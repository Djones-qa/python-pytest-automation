# Python Pytest Automation

![CI](https://github.com/Djones-qa/python-pytest-automation/actions/workflows/pytest-tests.yml/badge.svg)

Python test automation framework using Pytest, Playwright, and Requests library covering UI and API testing.

## Tech Stack
- Python 3.14
- Pytest
- Playwright for Python
- Requests library
- pytest-html reporter
- GitHub Actions CI

## Test Coverage (22 tests)

### API Tests (14 tests)
- Get all users (10 records validated)
- Get single user with schema validation
- User schema field validation
- Invalid user returns 404
- Parametrized user tests (5 users)
- Get all posts (100 records validated)
- Create post (POST request)
- Update post (PUT request)
- Delete post (DELETE request)
- Response time validation

### UI Tests (8 tests)
- Login page loads correctly
- Valid credentials login successfully
- Invalid username shows error
- Invalid password shows error
- Empty credentials shows error
- Data driven login tests (3 parametrized scenarios)

## Project Structure
```
python-pytest-automation/
├── tests/
│   ├── api/
│   │   └── test_api.py
│   └── ui/
│       └── test_login.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── .github/workflows/
    └── pytest-tests.yml
```

## Run Tests
```bash
pip install -r requirements.txt
python -m playwright install chromium
python -m pytest tests/api -v
python -m pytest tests/ui -v
python -m pytest -v
```

## Author
Darrius Jones - github.com/Djones-qa
