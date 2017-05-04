"""Mocked responses for the APIs."""

# HR
hr_get_employee = """
   {
  "employee_array": [
    {
      "address": "0 Lomb Memorial Drive, Rochester, New York 14623",
      "birth_date": "1992-02-12",
      "department": "Sales",
      "employee_id": 1,
      "is_active": true,
      "name": "Joseph Campione",
      "role": "Developer",
      "salary": "88083",
      "start_date": "2017-01-23",
      "team_start_date": "2017-01-23"
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
      “orderId”: 24,
        “items”: [
          {
            "serialNumber": 20,
            "price": 100,
            "status": "return",
            "replaceDeadline": "2017-03-01T20:51:26.908Z",
            "refundDeadline": "2017-03-01T20:51:26.908Z",
            "bogoSerialId": 25
          },
          {
            "serialNumber": 25,
            "price": 200,
            "status": "return",
            "replaceDeadline": "2017-03-01T20:51:26.909Z",
            "refundDeadline": "2017-03-01T20:51:26.909Z",
            "bogoSerialId": null
          }  
      ]
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
[
    {
      "id": 1,
      "repId": null,
      "totalItemCost": 1769.45,
      "shippingCost": 3.99,
      "orderDate": "1970-01-21T02:39:21.000Z",
      "isPaid": true,
      "taxPercentage": 0.07,
      "shippingAddress": {
    "id": 1,
    "firstName": "Joe",
    "lastName": "Jankowiak",
    "city": "Rancho Cordova",
    "address": "48 Washington Avenue",
    "zip": "81678",
    "customerId": 1,
    "state": {
      "id": 56,
      "state": "Washington",
      "rate": 0.05
    }
  },
  "paymentMethod": {
    "cardNumber": "2198",
    "id": 1,
    "CVC": 1047,
    "expirationDate": "1970-01-27T13:43:16.000Z",
    "billingAddressId": 1,
    "billingAddress": {
      "id": 1,
      "firstName": "Joe",
      "lastName": "Jankowiak",
      "city": "Rancho Cordova",
      "address": "48 Washington Avenue",
      "zip": "81678",
      "customerId": 1,
      "state": {
        "id": 56,
        "state": "Washington",
        "rate": 0.05
      }
    }
  },
  "customer": {
    "password": null,
    "id": 1,
    "firstName": "Joe",
    "lastName": "Jankowiak",
    "email": "jrj2211@rit.edu",
    "phoneNumber": "123-123-1234",
    "isCompany": false
  },
  "items": [
    {
      "id": 1,
      "serialNumber": 120133,
      "modelId": "A",
      "price": 150.99,
      "replacementDeadline": "1970-01-26T13:21:47.000Z",
      "refundDeadline": "1970-01-18T01:17:11.000Z",
      "refunded": null,
      "bogoSerialNumber": null,
      "orderId": 1
    }
  ]
]
"""
