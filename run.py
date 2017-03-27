from customersupport import app
import os

if('ENV' in os.environ and os.environ['ENV'] == 'production'):
    app.run('129.21.208.178', port=80, debug=False)
else:
    app.run(debug=True)
