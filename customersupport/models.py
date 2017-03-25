from sqlalchemy import Column, BigInteger, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from customersupport.database import Base

# class CallLog(Base):
#     __tablename__ = "call_log"


class Employee:
    """
    An Employee's data will not be stored in our database, so our
    Employee class does not implement Model.

    An employee class is a glorified struct for the following data:
      Employee ID : id
      Full Name   : name
    """
    _id = None
    _name = None

    def __init__(self, employee_dict):
        """
        Constructor. Super basic.
        Dictionary names are based on API docs. If these don't work
        HR either changed or ignored their documents.
        """
        self._id = employee_dict["employee_id"]
        self._name = employee_dict["name"]

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

    # Start read-only properties.

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name


class Customer:
    """
    A customer's data will not be stored in our database, so our
    Customer class does not implement Model.

    A customer class exposes this data:
      Customer ID  : id
      First Name   : first_name
      Last Name    : last_name
      Email        : email
      Phone number : phone_number
      Order List   : orders
      Ticket List  : support_tickets
    """
    _id = None
    _first_name = None
    _last_name = None
    _email = None
    _phone_number = None

    def __init__(self, customer_dict):
        """
        Constructor.
        Everything is based off of API docs.
        Same thing as Employee from HR, but this time we
        yell at Sales if it doesn't work.
        """
        self._id = customer_dict["customerId"]
        self._first_name = customer_dict["firstName"]
        self._last_name = customer_dict["lastName"]
        self._email = customer_dict["email"]
        self._phone_number = customer_dict["phone"]

    # Start read-only properties.
    @property
    def id(self):
        return self._id

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def email(self):
        return self._email

    @property
    def phone_number(self):
        return  self._phone_number

    # These properties require database calls to create.
    @property
    def orders(self):
        # TODO call sale api wrapper
        return None

    def support_tickets(self):
        # TODO query database for tickets
        return None
