import requests

# Log in the user
login_url = 'http://127.0.0.1:8010/login/'
login_data = {
    "username": 'siraj',
    "password": '6014'
}
login_response = requests.post(login_url, json=login_data)
headers = {}
# Check if the login was successful
if login_response.status_code == 200:
    access_token = login_response.json().get('access')

    # Make a request to the /employee/employees/ endpoint
    url = 'http://127.0.0.1:8010/employee/employees/'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    response = requests.get(url, headers=headers)
    print(response.json())
else:
    print("Login failed:", login_response.text)


create_employee = 'http://127.0.0.1:8010/employee/employees/'

employee_data = {
    "job_title": "developer",
    "department": "software",
    "hire_date": "2022-01-01",
    "phone_number": "+971503950224",
    "address": "dubai"
}
response = requests.post(create_employee, headers=headers, json=employee_data)
print("hello")