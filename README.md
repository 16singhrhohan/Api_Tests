# API Tests - OrangeHRM Demo

This repository contains API tests for the [OrangeHRM Demo Application](https://opensource-demo.orangehrmlive.com), built using Python and the `requests` library.

---

## Folder Structure

api_tests/
├── tests/
│ ├── test_get_users.py
│ ├── test_post_users.py
│ ├── test_put_users.py
│ └── test_delete_users.py
├── requirements.txt
└── README.md

---

## How to Run Tests

### 1. Create virtual environment *(optional but recommended)*

python -m venv venv
# Activate:
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run all tests

pytest tests/

---

## Tech Stack

Python 3.x

requests library

pytest for test execution

---

## Test Coverage

GET users

POST create user

PUT update user

DELETE user
