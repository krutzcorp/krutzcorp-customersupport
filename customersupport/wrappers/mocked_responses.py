"""Mocked responses for the APIs."""

# HR
hr_get_employee = """
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
"""

# Sales
sales_search_customer = """
    {
      "customers": [
        {
          "customerId": 0,
          "firstName": "John",
          "lastName": "Smith",
          "email": "johnsmith@email.com",
          "phone": "5451112222"
        },
        {
          "customerId": 42,
          "firstName": "John",
          "lastName": "Johnson",
          "email": "nottheotherjohn@email.com",
          "phone": "5451112222"
        }
      ]
    }
"""
