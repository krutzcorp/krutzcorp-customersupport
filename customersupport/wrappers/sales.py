import requests_mock
import requests
from config import SALES_URL
from customersupport.wrappers import mocked_responses
from customersupport.models import Customer


def search_customer(first_name=None, last_name=None, email=None, phone_number=None, mock=False):
    query_params = dict()
    if first_name is not None:
        query_params["firstName"] = first_name
    if last_name is not None:
        query_params["lastName"] = last_name
    if email is not None:
        query_params["email"] = email
    if phone_number is not None:
        query_params["phone"] = phone_number

    search_customer_url = SALES_URL + "/customer"

    if mock:
        with requests_mock.Mocker() as m:
            m.get(requests_mock.ANY, text=mocked_responses.sales_search_customer)
            r = requests.get(search_customer_url, params=query_params)
    else:
        r = requests.get(search_customer_url, params=query_params)

    json_resp = r.json()
    if "customers" not in json_resp:
        return None

    customers = []
    for customer_resp in json_resp["customers"]:
        customers.append(Customer(customer_resp))

    return customers


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