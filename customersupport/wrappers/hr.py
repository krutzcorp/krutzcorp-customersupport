import requests_mock
import requests
from functools import wraps
import json
import urllib.parse
from flask import request, Response
from customersupport import app
from config import HR_URL
from customersupport.models import Employee
from customersupport.wrappers import mocked_responses


def get_employee(employee_id, mock=False):
    """Get the employee with the given ID."""
    get_employee_url = HR_URL + "/employee?employee_id={employee_id}".format(employee_id=employee_id)
    if mock:
        with requests_mock.Mocker() as m:
            m.get(get_employee_url, text=mocked_responses.hr_get_employee)
            r = requests.get(get_employee_url)
    else:
        try:
            r = requests.get(get_employee_url)
        except requests.exceptions.RequestException:
            return None

    try:
        json_resp = r.json()
    except ValueError:
        return None

    if "employee_array" not in json_resp:
        return None

    num_employees = len(json_resp["employee_array"])
    if num_employees > 1:
        print('The system returned multiple employees.')
        return None
    elif num_employees <= 0:
        print('No employee returned.')
        return None

    employee_resp = json_resp["employee_array"][0]
    # print(employee_resp)
    employee = Employee(employee_resp)

    return employee

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_authtoken():
            return Response('<p>You are not allowed to view this page</p>')
        return f(*args, **kwargs)
    return decorated

# oauth authentication token sent from hr to the main page
def check_authtoken():

    token = request.args.get('token')
    #authenticate the token by calling hr
    get_authtoken_url = HR_URL + "/confirm_login/CustomerService/{token}".format(token=token)

    try:
        r = requests.get(get_authtoken_url)
    except requests.exceptions.RequestException:
        return Response('<p>Login failed</p>')

    try:
        json_resp = r.json()
    except ValueError:
        return Response('<p>Login failed</p>')

    if "employee_id" not in json_resp:
        return Response('<p>Login failed</p>')

    employee_id = json_resp["employee_id"]

    return employee_id