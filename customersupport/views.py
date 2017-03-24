from flask import Flask, request, render_template
from flask import request
from flask import render_template
from flask import jsonify
from flask import json

from customersupport import app
from customersupport.database import db_session
from customersupport.session_controller import SessionController
# from customersupport.models import CallLog

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/session')
def sessionCall():
    return json.dumps(SessionController.getEmployeeStubbed().json())
