from customersupport import app
from customersupport.wrappers import sales
from customersupport.util import get_param_from_request_if_not_empty

from flask import Flask, request, render_template
from flask import request
from flask import render_template
from flask import jsonify
from flask import json


@app.route('/sales/customer/real')
def search_customer(mock=False):
    customers = sales.search_customer(first_name="John", mock=mock)
    if customers is not None:
        return jsonify([c.serialize() for c in customers])
    else:
        return jsonify([])


@app.route('/sales/customer/stub')
def search_customer_stubbed():
    return search_customer(mock=True)


# @app.route('/customer/search')
# def get_customer_search_form():
#     return render_template('search-customer.html')

@app.route('/api/customer/search')
def get_matching_customers():
    """Call the Sales API to get matching customers. Used by the search-customer modal."""
    use_mock = request.args.get("use_mock") is not None

    customers = sales.search_customer(
        first_name=get_param_from_request_if_not_empty('first_name'),
        last_name=get_param_from_request_if_not_empty('last_name'),
        email=get_param_from_request_if_not_empty('email'),
        phone_number=get_param_from_request_if_not_empty('phone'),
        mock=use_mock
    )
    if customers is not None:
        return jsonify([c.serialize() for c in customers])
    else:
        return jsonify([])
