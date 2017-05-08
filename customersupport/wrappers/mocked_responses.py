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
[  
  {
    "id": 1,
    "repId": null,
    "totalItemCost": 2029.8,
    "shippingCost": 3.99,
    "orderDate": "1970-01-27T07:59:20.000Z",
    "isPaid": true,
    "taxPercentage": 0.01,
    "shippingAddress": {
      "id": 2,
      "firstName": "Dan",
      "lastName": "Fisher",
      "city": "Heritage Park",
      "address": "286 Broadway",
      "zip": "10578",
      "customerId": 2,
      "state": {
        "id": 31,
        "state": "Nebraska",
        "rate": 0.1
      }
    },
    "paymentMethod": {
      "cardNumber": "6561",
      "id": 2,
      "CVC": "639",
      "expirationDate": "1970-02-05T10:58:47.118Z",
      "billingAddressId": 2,
      "billingAddress": {
        "id": 2,
        "firstName": "Dan",
        "lastName": "Fisher",
        "city": "Heritage Park",
        "address": "286 Broadway",
        "zip": "10578",
        "customerId": 2,
        "state": {
          "id": 31,
          "state": "Nebraska",
          "rate": 0.1
        }
      }
    },
    "customer": {
      "password": null,
      "id": 7,
      "email": "newDan@gmail.com",
      "phoneNumber": "123-123-1234",
      "company": null
    },
    "items": []
  },
  {
    "id": 2,
    "repId": null,
    "totalItemCost": 1324.22,
    "shippingCost": 3.99,
    "orderDate": "1970-01-22T03:43:37.402Z",
    "isPaid": true,
    "taxPercentage": 0.04,
    "shippingAddress": {
      "id": 2,
      "firstName": "Dan",
      "lastName": "Fisher",
      "city": "Heritage Park",
      "address": "286 Broadway",
      "zip": "10578",
      "customerId": 2,
      "state": {
        "id": 31,
        "state": "Nebraska",
        "rate": 0.1
      }
    },
    "paymentMethod": {
      "cardNumber": "6561",
      "id": 2,
      "CVC": "639",
      "expirationDate": "1970-02-05T10:58:47.118Z",
      "billingAddressId": 2,
      "billingAddress": {
        "id": 2,
        "firstName": "Dan",
        "lastName": "Fisher",
        "city": "Heritage Park",
        "address": "286 Broadway",
        "zip": "10578",
        "customerId": 2,
        "state": {
          "id": 31,
          "state": "Nebraska",
          "rate": 0.1
        }
      }
    },
    "customer": {
      "password": null,
      "id": 7,
      "email": "newDan@gmail.com",
      "phoneNumber": "123-123-1234",
      "company": null
    },
    "items": [
      {
        "id": 1,
        "serialNumber": 120133,
        "modelId": "A",
        "price": 253.09,
        "replacementDeadline": "1970-01-18T21:45:40.819Z",
        "refundDeadline": "1970-01-20T18:57:47.978Z",
        "refunded": null,
        "bogoSerialNumber": null,
        "orderId": 2
      },
      {
        "id": 3,
        "serialNumber": 120135,
        "modelId": "A",
        "price": 224.44,
        "replacementDeadline": "1970-01-18T14:23:11.319Z",
        "refundDeadline": "1970-01-24T13:24:06.767Z",
        "refunded": null,
        "bogoSerialNumber": null,
        "orderId": 2
      }
    ]
  },
  {
    "id": 3,
    "repId": null,
    "totalItemCost": 1726.15,
    "shippingCost": 3.99,
    "orderDate": "1970-02-02T13:34:13.347Z",
    "isPaid": true,
    "taxPercentage": 0.07,
    "shippingAddress": {
      "id": 2,
      "firstName": "Dan",
      "lastName": "Fisher",
      "city": "Heritage Park",
      "address": "286 Broadway",
      "zip": "10578",
      "customerId": 2,
      "state": {
        "id": 31,
        "state": "Nebraska",
        "rate": 0.1
      }
    },
    "paymentMethod": {
      "cardNumber": "6561",
      "id": 2,
      "CVC": "639",
      "expirationDate": "1970-02-05T10:58:47.118Z",
      "billingAddressId": 2,
      "billingAddress": {
        "id": 2,
        "firstName": "Dan",
        "lastName": "Fisher",
        "city": "Heritage Park",
        "address": "286 Broadway",
        "zip": "10578",
        "customerId": 2,
        "state": {
          "id": 31,
          "state": "Nebraska",
          "rate": 0.1
        }
      }
    },
    "customer": {
      "password": null,
      "id": 7,
      "email": "newDan@gmail.com",
      "phoneNumber": "123-123-1234",
      "company": null
    },
    "items": [
      {
        "id": 2,
        "serialNumber": 120134,
        "modelId": "C",
        "price": 247.32,
        "replacementDeadline": "1970-01-23T07:44:07.395Z",
        "refundDeadline": "1970-01-30T06:11:12.412Z",
        "refunded": null,
        "bogoSerialNumber": null,
        "orderId": 3
      },
      {
        "id": 4,
        "serialNumber": 120136,
        "modelId": "B",
        "price": 356.37,
        "replacementDeadline": "1970-01-27T05:49:46.100Z",
        "refundDeadline": "1970-01-18T02:06:58.488Z",
        "refunded": null,
        "bogoSerialNumber": null,
        "orderId": 3
      }
    ]
  },
  {
    "id": 10,
    "repId": null,
    "totalItemCost": 0,
    "shippingCost": 0,
    "orderDate": "2017-05-08T15:52:16.257Z",
    "isPaid": true,
    "taxPercentage": 0.06,
    "shippingAddress": {
      "id": 2,
      "firstName": "Dan",
      "lastName": "Fisher",
      "city": "Heritage Park",
      "address": "286 Broadway",
      "zip": "10578",
      "customerId": 2,
      "state": {
        "id": 31,
        "state": "Nebraska",
        "rate": 0.1
      }
    },
    "paymentMethod": {
      "cardNumber": "6561",
      "id": 2,
      "CVC": "639",
      "expirationDate": "1970-02-05T10:58:47.118Z",
      "billingAddressId": 2,
      "billingAddress": {
        "id": 2,
        "firstName": "Dan",
        "lastName": "Fisher",
        "city": "Heritage Park",
        "address": "286 Broadway",
        "zip": "10578",
        "customerId": 2,
        "state": {
          "id": 31,
          "state": "Nebraska",
          "rate": 0.1
        }
      }
    },
    "customer": {
      "password": null,
      "id": 2,
      "email": "dan@gmail.com",
      "phoneNumber": "123-123-1234",
      "company": "Verizon"
    },
    "items": []
  }
]
"""

sales_get_order_info = """
{
  "id": 1,
  "repId": null,
  "totalItemCost": 2029.8,
  "shippingCost": 3.99,
  "orderDate": "1970-01-27T07:59:20.000Z",
  "isPaid": true,
  "taxPercentage": 0.01,
  "shippingAddress": {
    "id": 2,
    "firstName": "Dan",
    "lastName": "Fisher",
    "city": "Heritage Park",
    "address": "286 Broadway",
    "zip": "10578",
    "customerId": 2,
    "state": {
      "id": 31,
      "state": "Nebraska",
      "rate": 0.1
    }
  },
  "paymentMethod": {
    "cardNumber": "6561",
    "id": 2,
    "CVC": "639",
    "expirationDate": "1970-02-05T10:58:47.118Z",
    "billingAddressId": 2,
    "billingAddress": {
      "id": 2,
      "firstName": "Dan",
      "lastName": "Fisher",
      "city": "Heritage Park",
      "address": "286 Broadway",
      "zip": "10578",
      "customerId": 2,
      "state": {
        "id": 31,
        "state": "Nebraska",
        "rate": 0.1
      }
    }
  },
  "customer": {
    "password": null,
    "id": 7,
    "email": "newDan@gmail.com",
    "phoneNumber": "123-123-1234",
    "company": null
  },
  "items": []
}
"""
