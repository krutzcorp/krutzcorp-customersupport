from sqlalchemy import Column, BigInteger, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from customersupport.database import Base


# class CallLog(Base):
#     __tablename__ = "call_log"

class Customer:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.address = None
        self.phone_number = None

class Employee:
    def __init__(self):
        self.name = None
        self.id = None

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }