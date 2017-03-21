from flask import Flask, request, render_template
from flask import request
from flask import render_template
from flask import jsonify
from flask import json

from customersupport import app
from customersupport.database import db_session
# from customersupport.models import CallLog

@app.route('/')
def index():
    return render_template('index.html')
