from flask import jsonify

from customersupport import app
from customersupport.wrappers import sales


@app.route('/sales/ordersearch/real')
def search_order(mock=False):
    orders = sales.get_orders(
        customer_id=1,
        incl_items=True,
        mock=mock
    )

    if orders is not None:
        return jsonify([c.serialize() for c in orders])
    else:
        return jsonify([])


@app.route('/sales/ordersearch/stub')
def search_order_stubbed():
    return search_order(mock=True)


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
