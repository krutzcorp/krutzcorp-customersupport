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
          "fname": "Corban",
          "lname": "Mailloux",
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

sales_initiate_refund = """
    {
      "items": [
        {
          "price": 100,
          "refundDeadline": "2017-03-01T20:51:26.908Z",
          "replaceDeadline": "2017-03-01T20:51:26.908Z",
          "serialId": 20,
          "status": "return"
        },
        {
          "price": 200,
          "refundDeadline": "2017-03-01T20:51:26.909Z",
          "replaceDeadline": "2017-03-01T20:51:26.909Z",
          "serialId": 21,
          "status": "return"
        }
      ],
      "orderId": 24
    }
"""

sales_search_orders = """
    {
      "orders": [
        {
          "billingInfo": {
            "address": "1111 street",
            "ccLastFourDigets": "1234",
            "firstName": "john",
            "lastName": "doe",
            "state": "NY",
            "zip": "14586"
          },
          "cost": 200,
          "customerId": 1,
          "customerInfo": {
            "customerId": 42,
            "email": "nottheotherjohn@email.com",
            "firstName": "John",
            "lastName": "Johnson",
            "phone": "5451112222"
          },
          "id": 1000,
          "isPaid": false,
          "items": [
            {
              "price": 100,
              "refundDeadline": "2017-03-01T20:51:26.908Z",
              "replaceDeadline": "2017-03-01T20:51:26.908Z",
              "serialId": 20,
              "status": "original|return|replace"
            },
            {
              "price": 200,
              "refundDeadline": "2017-03-01T20:51:26.909Z",
              "replaceDeadline": "2017-03-01T20:51:26.909Z",
              "serialId": 21,
              "status": "original|return|replace"
            }
          ],
          "orderDate": "2017-03-01T20:51:26.905Z",
          "repId": 99,
          "shippingInfo": {
            "address": "1111 street",
            "firstName": "john",
            "lastName": "doe",
            "state": "NY",
            "zip": "14586"
          },
          "taxPercentage": 8
        }
      ]
    }
"""

sales_get_order_info = """
    {
      "orders": [
        {
          "billingInfo": {
            "address": "1111 street",
            "ccLastFourDigets": "1234",
            "firstName": "john",
            "lastName": "doe",
            "state": "NY",
            "zip": "14586"
          },
          "cost": 200,
          "customerId": 1,
          "customerInfo": {
            "customerId": 42,
            "email": "nottheotherjohn@email.com",
            "firstName": "John",
            "lastName": "Johnson",
            "phone": "5451112222"
          },
          "id": 1000,
          "isPaid": false,
          "items": [
            {
              "price": 100,
              "refundDeadline": "2017-03-01T20:51:26.908Z",
              "replaceDeadline": "2017-03-01T20:51:26.908Z",
              "serialId": 20,
              "status": "original|return|replace"
            },
            {
              "price": 200,
              "refundDeadline": "2017-03-01T20:51:26.909Z",
              "replaceDeadline": "2017-03-01T20:51:26.909Z",
              "serialId": 21,
              "status": "original|return|replace"
            }
          ],
          "orderDate": "2017-03-01T20:51:26.905Z",
          "repId": 99,
          "shippingInfo": {
            "address": "1111 street",
            "firstName": "john",
            "lastName": "doe",
            "state": "NY",
            "zip": "14586"
          },
          "taxPercentage": 8
        }
      ]
    }
"""
