from customersupport import app
from customersupport.forms import NewCallForm
from customersupport.models import CallLog
from customersupport.database import db_session

from flask import request, render_template, flash, redirect, url_for

from datetime import datetime


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/calls/new/', methods=["GET", "POST"])
def new_call():
    form = NewCallForm()
    if form.validate_on_submit():
        call_log = CallLog(
            customer_id=form.customer_id.data,
            order_id=form.order.data,
            calling_number=form.phone_called_from.data,
            callback_number=form.phone_call_back.data,
            notes=form.notes.data,
            ticket_id=form.ticket_id.data,
            date_called=form.date_called.data,
            employee="Corban"  # TODO: Add a real employee based on the session.
        )

        db_session.add(call_log)
        db_session.commit()
        flash("Call log added.")
        return redirect(url_for("index"))

    # If the date hasn't been set (normal page load), set the current time.
    if form.date_called.data is None:
        form.date_called.data = datetime.today()

    return render_template("new-call.html", form=form)


@app.route('/calls/', methods=["GET"])
def call_log_index():
    call_logs = db_session.query(CallLog)
    return render_template('call-log-index.html', call_logs=call_logs)
