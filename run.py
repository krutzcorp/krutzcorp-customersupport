from customersupport import app
import os

if('ENV' in os.environ and os.environ['ENV'] == 'production'):
    app.run('0.0.0.0', port=80, debug=False)
else:
    app.run(debug=True)
