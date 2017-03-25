from customersupport import app
from customersupport.wrappers import sales

from flask import Flask, request, render_template
from flask import request
from flask import render_template
from flask import jsonify
from flask import json


@app.route('/sales/refund/real')
def refund_order(mock=False):
    return jsonify(sales.initiate_refund(
        replace=True,
        order_id=1,
        serial_numbers=[
            123,
            456,
            789
        ],
        mock=mock))


@app.route('/sales/refund/stub')
def refund_order_stubbed():
    return refund_order(mock=True)