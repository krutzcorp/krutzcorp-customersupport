import requests_mock
import requests
from config import SALES_URL
from customersupport.wrappers import mocked_responses
from customersupport.models import Customer, Order, Item


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
        try:
            r = requests.get(search_customer_url, params=query_params)
        except requests.exceptions.RequestException:
            print("Request error.")
            raise

    try:
        json_resp = r.json()
    except ValueError:
        print("Response wasn't JSON.")
        raise

    customers = []
    for customer_resp in json_resp:
        customers.append(Customer(customer_resp))

    return customers


def initiate_refund(replace, order_id, serial_numbers, mock=False):
    payload = {"replace": replace, "orderId": order_id, "serialIds": serial_numbers}

    refund_url = SALES_URL + "/return"

    if mock:
        with requests_mock.Mocker() as m:
            m.post(requests_mock.ANY, text=mocked_responses.sales_initiate_refund)
            r = requests.post(refund_url, data=payload)
    else:
        try:
            r = requests.post(refund_url, data=payload)
        except requests.exceptions.RequestException:
            return None

    try:
        json_resp = r.json()
    except ValueError:
        return r

    # In the search order API, the "id" is the "orderId here.
    if "orderId" in json_resp and "id" not in json_resp:
        json_resp["id"] = json_resp["orderId"]

    try:
        order = Order(json_resp)
    except KeyError as ex:
        print("Error creating an Order.")
        raise ex

    return order


def get_orders(
        address=None, billing_address=False, customer_id=None, state=None,
        zipcode=None, city=None, first_name=None, last_name=None, mock=False):
    query_params = {
        "address": address, "state": state, "zipCode": zipcode, "city": city,
        "billingAddress": billing_address, "customerId": customer_id,
        "firstName": first_name, "lastName": last_name
    }

    search_order_url = SALES_URL + "/order/search"

    if mock:
        with requests_mock.Mocker() as m:
            m.get(requests_mock.ANY, text=mocked_responses.sales_search_orders)
            r = requests.get(search_order_url, params=query_params)
    else:
        try:
            r = requests.get(search_order_url, params=query_params)
        except requests.exceptions.RequestException:
            return None

    try:
        json_resp = r.json()
    except ValueError:
        return None

    orders = []
    for order in json_resp:
        orders.append(Order(order))

    return orders


def get_order_info(order_id, mock=False):
    query_params = {
        "orderId": order_id
    }

    order_info_url = SALES_URL + "/order"

    if mock:
        with requests_mock.Mocker() as m:
            m.get(requests_mock.ANY, text=mocked_responses.sales_get_order_info)
            r = requests.get(order_info_url, params=query_params)
    else:
        try:
            r = requests.get(order_info_url, params=query_params)
        except requests.exceptions.RequestException:
            return None

    try:
        json_resp = r.json()
    except ValueError:
        return None

    return Order(json_resp)
