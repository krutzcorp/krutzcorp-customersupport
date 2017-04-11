from customersupport import app
from customersupport.wrappers import sales
from customersupport.models import Ticket, CallLog
from customersupport.database import db_session
from customersupport.util import get_param_from_request_if_not_empty

from flask import Flask, request, render_template
from flask import request
from flask import render_template
from flask import jsonify
from flask import json

@app.route('/sales/refund/real')
def refund_order(mock=False):
    order = sales.initiate_refund(
        replace=True,
        order_id=1,
        serial_numbers=[
            123,
            456,
            789
        ],
        mock=mock
    )

    if order is not None:
        return jsonify(order.serialize())
    else:
        return jsonify([])


@app.route('/sales/refund/stub')
def refund_order_stubbed():
    return refund_order(mock=True)


@app.route('/api/ticket/customer')
def get_tickets_for_customer():
    customer_id=get_param_from_request_if_not_empty('customer_id')
    ticket_id=get_param_from_request_if_not_empty('ticket_id')

    res = []
    if customer_id is not None:
        res = Ticket.query.filter_by(customer_id=customer_id).all()
    elif ticket_id is not None:
        res = Ticket.query.filter_by(id=ticket_id).all()
    else:
        res = Ticket.query.all()
    return jsonify([r.serialize() for r in res])

