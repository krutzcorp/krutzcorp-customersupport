from flask_wtf import FlaskForm
from wtforms import validators, IntegerField, SelectField, TextAreaField, DateTimeField
from wtforms.fields.html5 import TelField
from wtforms.widgets import HiddenInput


class NewCallForm(FlaskForm):
    date_called = DateTimeField(
        "Date Called",
        validators=[
            validators.InputRequired()
        ],
        widget=HiddenInput()  # Hide this field. We are using it directly in the template.
    )

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
