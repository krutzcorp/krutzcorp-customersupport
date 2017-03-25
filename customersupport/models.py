from sqlalchemy import Column, BigInteger, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from customersupport.database import Base

# class CallLog(Base):
#     __tablename__ = "call_log"


"""
An Employee's data will not be stored in our database, so our
Employee class does not implement Model.

An employee class is a glorified struct for the following data:
  Employee ID : id
  Full Name   : name
"""
class Employee:
    _id = None
    _name = None

    """
    Constructor. Super basic.
    Dictionary names are based on API docs. If these don't work
    HR either changed or ignored their documents.
    """
    def __init__(self, employeeDict):
        self._id = employeeDict["employee_id"]
        self._name = employeeDict["name"]

    """
    Start read-only properties.
    """
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name


"""
A customer's data will not be stored in our database, so our
Customer class does not implement Model.

A customer class exposes this data:
  Employee ID  : id
  First Name   : first_name
  Last Name    : last_name
  Email        : email
  Phone number : phone_number
  Order List   : orders
  Ticket List  : support_tickets
"""
class Customer:
    _id = None
    _first_name = None
    _last_name = None
    _email = None
    _phone_number = None

    """
    Constructor.
    Everything is based off of API docs.
    Same thing as Employee from HR, but this time we
    yell at Sales if it doesn't work.
    """
    def __init__(self, customerDict):
        self._id = customerDict["customerId"]
        self._first_name = customerDict["firstName"]
        self._last_name = customerDict["lastName"]
        self._email = customerDict["email"]
        self._phone_number = customerDict["phone"]

    """
    Start read-only properties.
    """
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

    """
    These properties require database calls to create.
    """
    @property
    def orders(self):
        #TODO call sale api wrapper
        return None

    def support_tickets(self):
        #TODO query database for tickets
        return  None

