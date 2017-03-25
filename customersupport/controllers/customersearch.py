from customersupport import app
from customersupport.wrappers import sales

from flask import Flask, request, render_template
from flask import request
from flask import render_template
from flask import jsonify
from flask import json


@app.route('/sales/customer/real')
def search_customer(mock=False):
    customers = sales.search_customer(first_name="John")
    if customers is not None:
        return jsonify([c.serialize() for c in sales.search_customer(first_name="John", mock=mock)])
    else:
        return jsonify([])


@app.route('/sales/customer/stub')
def search_customer_stubbed():
    return search_customer(mock=True)