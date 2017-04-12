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
[
  {
    "email": "jrj2211@rit.edu",
    "firstName": "Joe",
    "id": 1,
    "isCompany": true,
    "lastName": "Jankowiak",
    "password": "5f4dcc3b5aa765d61d8327deb882cf99",
    "phoneNumber": "123-123-1234"
  },
  {
    "email": "dan@gmail.com",
    "firstName": "Dan",
    "id": 2,
    "isCompany": true,
    "lastName": "Fisher",
    "password": "5f4dcc3b5aa765d61d8327deb882cf99",
    "phoneNumber": "123-123-1234"
  },
  {
    "email": "Joe@gmail.com",
    "firstName": "Joe",
    "id": 3,
    "isCompany": false,
    "lastName": "Campione",
    "password": "5f4dcc3b5aa765d61d8327deb882cf99",
    "phoneNumber": "123-123-1234"
  },
  {
    "email": "Cailin@gmail.com",
    "firstName": "Cailin",
    "id": 4,
    "isCompany": true,
    "lastName": "Li",
    "password": "5f4dcc3b5aa765d61d8327deb882cf99",
    "phoneNumber": "123-123-1234"
  },
  {
    "email": "Nick@gmail.com",
    "firstName": "Nick",
    "id": 5,
    "isCompany": true,
    "lastName": "Swanson",
    "password": "5f4dcc3b5aa765d61d8327deb882cf99",
    "phoneNumber": "123-123-1234"
  },
  {
    "email": "nottheotherjohn@email.com",
    "firstName": "John",
    "id": 6,
    "isCompany": true,
    "lastName": "Verizon",
    "password": "5f4dcc3b5aa765d61d8327deb882cf99",
    "phoneNumber": "123-123-1234"
  },
  {
    "email": "successewDan@gmail.com",
    "firstName": "Justin",
    "id": 7,
    "isCompany": false,
    "lastName": "Nietzel",
    "password": "5f4dcc3b5aa765d61d8327deb882cf99",
    "phoneNumber": "123-123-1234"
  }
]
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
