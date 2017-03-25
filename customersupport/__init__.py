from flask import Flask
from customersupport.database import db_session

app = Flask(__name__)

from customersupport.controllers import session, customersearch, ticket


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
