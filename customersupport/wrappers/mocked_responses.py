"""Mocked responses for the APIs."""

# HR
hr_get_employee = """
    {
  "employee_array": [
    {
      "address": "42 Wallaby Way, Rochester, New York 14623",
      "birth_date": "1995-04-25",
      "department": "Human Resources",
      "employee_id": 1,
      "is_active": true,
      "name": "Wendy Williams",
      "role": "HR Admin",
      "salary": "60000",
      "start_date": "2017-03-28",
      "team_start_date": "2006-11-10"
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
    "phoneNumber": "123-123-1234"
  },
  {
    "email": "dan@gmail.com",
    "firstName": "Dan",
    "id": 2,
    "isCompany": true,
    "lastName": "Fisher",
    "phoneNumber": "123-123-1234"
  },
  {
    "email": "Joe@gmail.com",
    "firstName": "Joe",
    "id": 3,
    "isCompany": false,
    "lastName": "Campione",
    "phoneNumber": "123-123-1234"
  },
  {
    "email": "Cailin@gmail.com",
    "firstName": "Cailin",
    "id": 4,
    "isCompany": true,
    "lastName": "Li",
    "phoneNumber": "123-123-1234"
  },
  {
    "email": "Nick@gmail.com",
    "firstName": "Nick",
    "id": 5,
    "isCompany": true,
    "lastName": "Swanson",
    "phoneNumber": "123-123-1234"
  },
  {
    "email": "nottheotherjohn@email.com",
    "firstName": "John",
    "id": 6,
    "isCompany": true,
    "lastName": "Verizon",
    "phoneNumber": "123-123-1234"
  },
  {
    "email": "successewDan@gmail.com",
    "firstName": "Justin",
    "id": 7,
    "isCompany": false,
    "lastName": "Nietzel",
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
              "id":2,
              "serialNumber":120134,
      "modelId":"B",
      "price":160.85,
      "replacementDeadline":"1970-01-17T22:54:46.000Z",
      "refundDeadline":"1970-01-29T15:23:47.000Z",
      "refunded":null,
      "bogoSerialNumber":null,
      "orderId":1
            },
            {
              "id":1,
      "serialNumber":120133,
      "modelId":"B",
      "price":550.58,
      "replacementDeadline":"1970-01-20T02:52:45.000Z",
      "refundDeadline":"1970-01-26T07:17:54.000Z",
      "refunded":null,
      "bogoSerialNumber":null,
      "orderId":1
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
