from flask import Flask, request, render_template
from flask import request
from flask import render_template
from flask import jsonify
from flask import json

from customersupport import app
from customersupport.database import db_session
from customersupport.controllers import session as session_controller

@app.route('/')
def index():
    return render_template('index.html')


# Search customer
# @app.route()


# Get Employee
@app.route('/employee/real')
def get_employee():
    return jsonify(session_controller.get_employee().json())


@app.route('/employee/stub')
def get_employee_stub():
    return jsonify(session_controller.get_employee_stubbed().serialize())


