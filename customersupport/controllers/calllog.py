from customersupport import app
from customersupport.forms import NewCallForm
from customersupport.models import CallLog
from customersupport.database import db_session
from customersupport.wrappers.hr import requires_auth

from flask import request, render_template, flash, redirect, url_for


@app.route('/', methods=["GET", "POST"])
@requires_auth
def new_call():
    form = NewCallForm()
    if form.validate_on_submit():
        call_log = CallLog(
            calling_number=form.phone_called_from.data,
            callback_number=form.phone_call_back.data,
            notes=form.notes.data,
            ticket_id=form.ticket_id.data,
            employee="Corban"  # TODO: Add a real employee based on the session.
        )

        db_session.add(call_log)
        db_session.commit()
        flash("Call log added.")
        return redirect(url_for("new_call"))

    return render_template("new-call.html", form=form)
