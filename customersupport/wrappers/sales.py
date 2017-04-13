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
            return None

    try:
        json_resp = r.json()
    except ValueError:
        return None

    if "customers" not in json_resp:
        return None

    customers = []
    for customer_resp in json_resp["customers"]:
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
        return None

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
        address=None, billing_address=False, customer_id=None, incl_payment_info=False,
        incl_shipping_info=False, incl_customer_info=False, incl_items=False, mock=False):
    query_params = {
        "address": address, "billingAddress": billing_address, "customerId": customer_id,
        "paymentInfo": incl_payment_info, "shippingInfo": incl_shipping_info,
        "customerInfo": incl_customer_info, "items": incl_items
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

    if "orders" not in json_resp:
        return None

    orders = []
    for order in json_resp["orders"]:
        orders.append(Order(order))

    return orders


def get_order_info(
        order_id, incl_payment_info=False, incl_shipping_info=False, incl_customer_info=False,
        incl_items=False, mock=False):
    query_params = {
        "orderId": order_id, "paymentInfo": incl_payment_info, "shippingInfo": incl_shipping_info,
        "customerInfo": incl_customer_info, "items": incl_items
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

    # if "orders" not in json_resp:
    #     return None

    return Order(json_resp)
    # orders = []
    # for order in json_resp:
    #     orders.append(Order(order))

    # return orders
