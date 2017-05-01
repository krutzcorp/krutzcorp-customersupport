from flask import Flask
from customersupport.database import db_session

app = Flask(__name__)

from customersupport.controllers import session, customersearch, ticket, ordersearch, calllog


@app.template_filter('datetime')
def filter_datetime(value, format_string="%Y-%m-%d %I:%M:%S %p"):
    return value.strftime(format_string)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
