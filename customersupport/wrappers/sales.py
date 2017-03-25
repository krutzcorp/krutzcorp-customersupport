import requests
from config import SALES_URL


def search_customer(first_name=None, last_name=None, email=None, phone_number=None):
    r = requests.get(SALES_URL)
    return r


def initiate_refund(replace, order_id, serial_numbers):
    r = requests.get(SALES_URL)
    return r


def get_orders(address=None, billing_address=None, customer_id=None, incl_payment_info=False,
               incl_shipping_info=False, incl_customer_info=False, incl_items=False):
    r = requests.get(SALES_URL)
    return r

def get_order_info(order_id, incl_payment_info=False, incl_shipping_info=False,
                   incl_customer_info=False, incl_items=False):
    r = requests.get(SALES_URL)
    return r