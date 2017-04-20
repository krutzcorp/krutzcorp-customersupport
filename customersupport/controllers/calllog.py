from customersupport import app
from customersupport.forms import NewCallForm

from flask import Flask, request, render_template


@app.route('/', methods=["GET", "POST"])
def get_new_call_form():
    form = NewCallForm()
    if form.validate_on_submit():
        pass

    return render_template('new-call.html', form=form)
