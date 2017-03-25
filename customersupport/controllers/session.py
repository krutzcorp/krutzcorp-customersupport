import requests_mock
from customersupport.hrwrapper_spec import Stubber
from customersupport.wrappers import hr as hr_wrapper
import json


def get_employee():
    """Get an employee."""
    hr_wrapper.get_employee(1)


def get_employee_stubbed():
    """Use the stubbed version of the wrapper."""
    expected_response = json.loads("""
        {
          "employee_array": [
            {
              "address": "123 Main St.",
              "birth_date": "1994-03-19",
              "company_start_date": "2017-01-01",
              "department": "Customer Support",
              "employee_id": 1,
              "is_active": true,
              "name": "Corban Mailloux",
              "role": "Support Rep",
              "salary": 999999,
              "team_start_date": "2017-01-01"
            }
          ]
        }
    """)

    with requests_mock.mock() as m:
        Stubber.stubMock(m, json=expected_response)
        return hr_wrapper.get_employee(1)
