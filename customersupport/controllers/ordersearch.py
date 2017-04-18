from flask import jsonify
from flask import request

from customersupport import app
from customersupport.wrappers import sales

def get_param_from_request_if_not_empty(param_name):
    """Get a query parameter from the request, or None if the parameter is empty or missing."""
    value = request.args.get(param_name)
    if value is not None and value != "":
        return value
    else:
        return None

"""select which order search to use if order id exists use order search otherwise order info"""

@app.route('/api/order/search')
def select_search():

    # call order search
    if get_param_from_request_if_not_empty('order_id') is not None:
        orders = sales.get_order_info(
            order_id=get_param_from_request_if_not_empty('order_id'),
            incl_payment_info=get_param_from_request_if_not_empty('return_billing'),
            incl_shipping_info=get_param_from_request_if_not_empty('return_shipping'),
            incl_customer_info= get_param_from_request_if_not_empty('return_customer'),
            incl_items=get_param_from_request_if_not_empty('return_items'),
            mock=False

        )
    else:
        orders = sales.get_orders(
            address=get_param_from_request_if_not_empty('address'),
            billing_address= True, #check if radio button click,
            customer_id=get_param_from_request_if_not_empty('customer'),
            incl_payment_info=get_param_from_request_if_not_empty('return_billing'),
            incl_shipping_info=get_param_from_request_if_not_empty('return_shipping'),
            incl_customer_info=get_param_from_request_if_not_empty('return_customer'),
            incl_items=get_param_from_request_if_not_empty('return_items'),
            mock=False
        )

    """Call the Sales API to get matching . Used by the search-order"""

    if orders is not None:
        return jsonify([c.serialize() for c in orders])


@app.route('/api/orderitem')
def get_info():
    order_id = get_param_from_request_if_not_empty('order_id')
    if order_id is not None:
        order_info = sales.get_order_info(
            order_id=order_id, mock=False
        )
        order = order_info
        items_list = order.items
        return jsonify([c.serialize() for c in items_list])
    return jsonify([])



@app.route('/sales/ordersearch/stub')
def search_order_stubbed():
    return sales.get_orders(mock=True)


@app.route('/sales/orderinfo/real')
def get_order_info(mock=False):
    orders = sales.get_order_info(
        order_id=1,
        incl_items=True,
        mock=mock
    )

    if orders is not None:
        return jsonify([c.serialize() for c in orders])
    else:
        return jsonify([])


@app.route('/sales/orderinfo/stub')
def get_order_info_stubbed():
    return get_order_info(mock=True)
