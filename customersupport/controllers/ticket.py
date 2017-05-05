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
    replace = get_post_data("replace") == "true"
    ticket_type = TicketType.REFUND
    if replace:
        ticket_type = TicketType.REPLACE
    status = get_post_data("status")
    current_status = TicketStatus.CLOSED_PASS
    if status == "open":
        current_status = TicketStatus.OPEN
    elif status == "pend":
        current_status = TicketStatus.PENDING
    elif status == "pass":
        current_status = TicketStatus.CLOSED_PASS
    elif status == "fail":
        current_status = TicketStatus.CLOSED_FAIL
    order_id = get_post_data("order_id")
    serial_ids = get_post_data("serial_ids")
    customer_id = get_post_data("customer_id")

    ticket = Ticket(
        ticket_type=ticket_type,
        customer_id=customer_id,
        order_id=order_id,
        current_status=current_status
    )

    db_session.add(ticket)
    db_session.commit()

    try:
        status_is_good = sales.initiate_refund(
            replace=replace,
            order_id=order_id,
            serial_numbers=serial_ids,
            mock=use_mock
        )
        if status_is_good:
            """
            Yay, we came back successfully, now go tell hr we made a refund/return.
            Blind fire for now, we do not care if this is delivered or not.
            TODO: Actually pass an employeeId
            """
            hr.report_action(replace, order_id, serial_ids, "1")
            # Return the ticket created ealier
            return jsonify(ticket.serialize())
    except Exception as ex:
        print(ex)
        abort(500)

    else:
        abort(500)
        return jsonify({})


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
