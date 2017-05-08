from flask import jsonify
from flask import request, abort

from customersupport import app
from customersupport.wrappers import sales
from customersupport.util import get_param_from_request_if_not_empty


def check_address(address):
    """Check if the address field of the request is set to billing."""
    value = request.args.get(address)
    if value == 'billing':
        return True
    else:
        return False


@app.route('/api/order/search')
def select_search():
    """Search for an order by address and/or customer."""
    orders = sales.get_orders(
        address=get_param_from_request_if_not_empty('street_address'),
        billing_address=check_address('address'),  # check if radio button click,
        city=get_param_from_request_if_not_empty('city'),
        state=get_param_from_request_if_not_empty('state'),
        zipcode=get_param_from_request_if_not_empty('zipcode'),
        first_name=get_param_from_request_if_not_empty('first_name'),
        last_name=get_param_from_request_if_not_empty('last_name'),
        customer_id=get_param_from_request_if_not_empty('customer'),
        mock=False
    )

    if orders is not None:
        return jsonify([c.serialize() for c in orders])

    return jsonify([])


@app.route('/api/orderid/search')
def search_order_id():
    """Search for an order by order ID."""
    order = sales.get_order_info(
        order_id=get_param_from_request_if_not_empty('order_id'),
        mock=False
    )

    if order is not None:
        return jsonify([order.serialize()])

    return jsonify([])


@app.route('/api/orderitem')
def get_info():
    order_id = get_param_from_request_if_not_empty('order_id')
    mocked = get_param_from_request_if_not_empty('mocked')
    if order_id is not None:
        try:
            order_info = sales.get_order_info(order_id = order_id, mock=mocked)
            order = order_info
            items_list = order.items
            return jsonify([c.serialize() for c in items_list])
        except Exception as ex:
            print(ex)
            abort(503)
    return jsonify([])
