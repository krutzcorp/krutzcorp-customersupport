from customersupport import app
from customersupport.wrappers import sales, hr
from customersupport.models import Ticket, CallLog, TicketType, TicketStatus
from customersupport.database import db_session
from customersupport.util import get_param_from_request_if_not_empty, get_post_data

from flask import Flask, request, render_template, abort
from flask import request
from flask import render_template
from flask import jsonify
from flask import json

@app.route('/api/refund', methods=['POST'])
def refund_order():

    use_mock = get_post_data("use_mock") is not None
    replace = get_post_data("replace")
    ticket_type = TicketType.REFUND
    if replace:
        ticket_type = TicketType.REPLACE
    status = get_post_data("status")
    current_status = TicketStatus.CLOSED
    if status == "open":
        current_status = TicketStatus.OPEN
    elif status == "pend":
        current_status = TicketStatus.PENDING
    elif status == "pass" or status == "fail":
        current_status = TicketStatus.CLOSED
    order_id = get_post_data("order_id")
    serial_ids = get_post_data("serial_ids")
    customer_id = get_post_data("customer_id")
    print(order_id)
    print(customer_id)
    ticket = Ticket(
        ticket_type=ticket_type,
        current_status=current_status,
        customer_id=customer_id,
        order_id=order_id
    )

    db_session.add(ticket)
    db_session.commit()
    """
    # TODO: Call sales
    try:
        order = sales.initiate_refund(
            replace=True,
            order_id=1,
            serial_numbers=[
                123,
                456,
                789
            ],
            mock=use_mock
        )
    except Exception as ex:
        print(ex)
        abort(500) 
    """
    return jsonify(ticket.serialize())


@app.route('/sales/refund/stub')
def refund_order_stubbed():
    return refund_order(mock=True)


@app.route('/api/ticket')
def get_ticket():
    customer_id=get_param_from_request_if_not_empty('customer_id')
    ticket_id=get_param_from_request_if_not_empty('ticket_id')

    res = []
    if ticket_id is not None:
        res = Ticket.query.filter_by(id=ticket_id).all()
    elif customer_id is not None:
        res = Ticket.query.filter_by(customer_id=customer_id).all()
    else:
        res = Ticket.query.all()
    return jsonify([r.serialize() for r in res])

@app.route('/api/refund/report', methods=["POST"])
def report_refund():
    employee_id = "1"
    replace = get_param_from_request_if_not_empty('replace')
    order_id = get_param_from_request_if_not_empty('orderId')
    serial_numbers = get_param_from_request_if_not_empty('serialIds')
    mocked = get_param_from_request_if_not_empty('mocked')

    res = hr.report_action(replace,order_id,serial_numbers,employee_id,mocked)
    if res is None:
        return jsonify({})
    return jsonify(res)
