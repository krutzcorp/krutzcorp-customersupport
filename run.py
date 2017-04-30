from customersupport import app
import os


app.secret_key = "TESTING SECRET KEY"

app.run(debug=True)
