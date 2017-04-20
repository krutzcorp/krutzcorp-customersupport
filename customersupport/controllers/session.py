from customersupport import app
from customersupport.wrappers import hr, sales
import json

from flask import Flask, request, render_template
from flask import request
from flask import render_template
from flask import jsonify
from flask import json


@app.route('/listing')
def index():
    return render_template('api-route-listing.html')


@app.route('/employee/real')
def get_employee(mock=False):
    """Get an employee."""
    employee = hr.get_employee(1, mock=mock)

    if employee is not None:
        return jsonify(employee.serialize())
    else:
        return jsonify([])


@app.route('/employee/stub')
def get_employee_stubbed():
    """Use the stubbed version of the wrapper."""
    return get_employee(mock=True)
