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

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone_number
        }

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
        return self._phone_number

    # These properties require database calls to create.
    @property
    def orders(self):
        # TODO call sale api wrapper
        return None

    def support_tickets(self):
        # TODO query database for tickets
        return None


class Order:
    """
    Order is another class not stored in our database.

    An Order class exposes this data (properties of an order item included):
      Order ID    : id
      Order Date  : order_date
      Order Items : items
          Item ID      : id
          Item Status  : status
          Replace Date : replace_date
          Refund Date  : refund_date
    """
    _id = None
    _order_date = None
    _items = set()

    def __init__(self, order_dict):
        """
        All parameters come from api docs. An order dictionary should
        contain zero or more item dictionaries.

        :param item_dict: dictionary from API call
        """
        self._id = order_dict["id"]
        if "orderDate" in order_dict:  # This isn't in the refund response.
            self._order_date = order_dict["orderDate"]
        if "items" in order_dict:  # Items aren't always included
            for item in order_dict["items"]:
                self._items.add(Item(item))

    def serialize(self):
        """
        Serialize this object.

        :return: A dictionary containing values mapped to keys from api
        docs. The items key will map to a list of dictionaries.
        """
        items = []
        for item in self._items:
            items.append(item.serialize())

        return {
            "id": self._id,
            "orderDate": self._order_date,
            "items": items
        }

    @property
    def id(self):
        return self._id

    @property
    def order_date(self):
        return self._order_date

    @property
    def items(self):
        return self._items


class Item:
    """
    This is a helper class for Order to store data on individual
    items.

    Item ID      : id
    Item Status  : status
    Replace Date : replace_date
    Refund Date  : refund_date
    """
    _id = None
    _status = None
    _replace_date = None
    _refund_date = None

    def __init__(self, item_dict):
        """
        All parameters come from api docs
        :param item_dict: dictionary from api call
        """
        self._id = item_dict["serialId"]
        self._status = item_dict["status"]
        self._replace_date = item_dict["replaceDeadline"]
        self._refund_date = item_dict["refundDeadline"]

    def __hash__(self):
        """
        Overridden hash function so we can store items in a set
        for an Order.
        :return: item id
        """
        return self.id;

    def serialize(self):
        """
        Serialize this object.
        :return: A dictionary containing values mapped to keys from api docs.
        """
        return {
            "serialId": self._id,
            "status": self._status,
            "replaceDeadline": self._replace_date,
            "refundDeadline": self.refund_date
        }

    @property
    def id(self):
        return self._id

    @property
    def status(self):
        return self._status

    @property
    def replace_date(self):
        return self._replace_date

    @property
    def refund_date(self):
        return self._refund_date
