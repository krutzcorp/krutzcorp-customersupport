import requests
import json
import urllib.parse
from config import HR_URL
from customersupport.models import Employee


def get_employee(employee_id):
    """Get the employee with the given ID."""
    # get_employee_url_format = HR_URL + "/employees?employee_id={employee_id}"
    #
    # r = requests.get(get_employee_url_format.format(employee_id=employee_id))

    r = requests.get(HR_URL)

    json_resp = r.json()
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
    employee = Employee()
    employee.id = employee_resp["employee_id"]
    employee.name = employee_resp["name"]

    return employee
