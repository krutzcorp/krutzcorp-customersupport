from flask_wtf import FlaskForm
from wtforms import validators, IntegerField, SelectField, TextAreaField
from wtforms.fields.html5 import TelField


class NewCallForm(FlaskForm):
    customer_id = IntegerField(
        "Customer ID",
        validators=[
            validators.Optional()
        ]
    )

    order = IntegerField(
        "Order Number",
        validators=[
            validators.Optional()
        ]
    )

    phone_called_from = TelField(
        "Called From",
        validators=[
            validators.InputRequired()
        ]
    )

    phone_call_back = TelField(
        "Call Back",
        validators=[
            validators.InputRequired()
        ]
    )

    ticket_id = IntegerField(
        "Ticket ID",
        validators=[
            validators.Optional()
        ]
    )

    ticket_type = SelectField(
        "Ticket Type",
        choices=[
            ("Refund", "Refund"), ("Replace", "Replace")
        ]
    )

    notes = TextAreaField(
        "Notes",
        validators=[
            validators.Optional()
        ]
    )
