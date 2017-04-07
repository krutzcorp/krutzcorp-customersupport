from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from customersupport.database import Base
import enum

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
        self._name = employee_dict["fname"] + " " + employee_dict["lname"]

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
        if "customerId" in customer_dict:
            self._id = customer_dict["customerId"]
        elif "id" in customer_dict:
            self._id = customer_dict["id"]
        else:
            raise KeyError("Couldn't extract customer ID from the customer response.")

        self._first_name = customer_dict["firstName"]
        self._last_name = customer_dict["lastName"]
        self._email = customer_dict["email"]

        if "phone" in customer_dict:
            self._phone_number = customer_dict["phone"]
        elif "phoneNumber" in customer_dict:
            self._phone_number = customer_dict["phoneNumber"]
        else:
            raise KeyError("Couldn't extract phone number from the customer response.")

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

class TicketType(enum.Enum):
    REFUND="REFUND"
    REPAIR="REPAIR"

class TicketStatus(enum.Enum):
    CLOSED="CLOSED"
    OPEN="OPEN"
    PENDING="PENDING"

class Ticket(Base):
    """
    This class stores tickets in the database.

    Tickets expose the following data
    Id of the ticket:           id
    Issue Enumeration:          issue
    Date Opened:                dateOpened
    Date Closed:                dateClosed
    Current Status Enumeration: currentStatus
    List of Call Sessions:      sessions
    Customer on Ticket:         customerId
    Order on Ticket:            orderId

    """
    __tablename__ = 'ticket'
    id = Column(Integer, primary_key=True, autoincrement=True)
    issue = Column(Enum(TicketType))
    dateOpened = Column(DateTime)
    dateClosed = Column(DateTime)
    currentStatus = Column(Enum(TicketStatus))
    sessions = relationship('CallLog',backref="post",cascade="all, delete-orphan",lazy="dynamic")
    customerId = Column(String(16)) 
#    orderId = Column(String(60),ForeignKey('order.id'))
    
    def __init__(self, ticket_dict):
        """
        Params come from API docs
        :param ticket_dict: dictionary for init ticket
        """
        self.issue = ticket_dict["issue"]
        self.dataOpened = ticket_dict["dateOpened"]
        self.dateClosed = ticket_dict["dateClosed"]
        self.currentStatus = ticket_dict["currentStatus"]
        self.sessions = ticket_dict["sessions"]
        self.customerId = ticket_dict["customerId"]
#        self._orderId = ticket_dict["orderId"]

    def __repr__(self):
        return '<Ticket %r %r %r %r %r %r>' %(self.id, self.issue, self.dateOpened, self.currentStatus, self.sessions, self.customerId)

    def serialize(self):
        sessions = []
        for session in self.sessions:
            print(session)
            sessions.append(session.serialize())
        return {
            "id": self.id,
            "issue": self.issue.name,
            "dateOpened": self.dateOpened,
            "dateClosed": self.dateClosed,
            "currentStatus": self.currentStatus.name,
            "sessions": sessions,
            "customerId": self.customerId
        #    "orderId": self.orderId
        }

class CallLog(Base):
    __tablename__ = "call_log"
    id = Column(Integer, primary_key=True, autoincrement=True)
    dateCalled = Column(DateTime)
    callingNumber = Column(String(60))
    callbackNumber = Column(String(60))
    notes = Column(String(500))
#    actionTaken = Column(ActionTaken)????
    employee = Column(String(16))
    ticket = Column(Integer, ForeignKey('ticket.id'))

    def __init__(self, call_dict):
        self.dateCalled = call_dict["dateCalled"]
        self.callingNumber = call_dict["callingNumber"]
        self.callbackNumber = call_dict["callbackNumber"]
        self.notes = call_dict["notes"]
        self.employee = call_dict["employee"]

    def __refr__(self):
        return '<CallLog %r $r $r $r %r %r>' %(self.dateCalled,self.callingNumber,self.callbackNumber,self.notes,self.employee)

    def serialize(self):
        return {
            "id":self.id,
            "dateCalled":self.dateCalled,
            "calllingNumber":self.callingNumber,
            "callbackNumber":self.callbackNumber,
            "notes":self.notes,
            "employee":self.employee,
            "ticket":self.ticket
        }
