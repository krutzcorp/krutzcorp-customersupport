from customersupport import app
from customersupport.wrappers import hr, sales
import json

from flask import Flask, request, render_template
from flask import request
from flask import render_template
from flask import jsonify
from flask import json


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/employee/real')
def get_employee(mock=False):
    """Get an employee."""
    return jsonify(hr.get_employee(1, mock=mock).serialize())


@app.route('/employee/stub')
def get_employee_stubbed():
    """Use the stubbed version of the wrapper."""
    return get_employee(mock=True)
