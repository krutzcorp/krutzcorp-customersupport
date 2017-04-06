from customersupport.models import Ticket, CallLog
from customersupport.database import db_session
from customersupport.database import init_db
import datetime

init_db()

today = datetime.datetime.now()

cl_1 = {"dateCalled":today,"callingNumber":"111-222-3333","callbackNumber":"111-222-3434","notes":"Nothing to report here","employee":"1","ticket":1}
c_1 = CallLog(cl_1)

td = {"customerId":"1","issue":"REFUND","dateOpened":today,"dateClosed":today,"currentStatus":"CLOSED","sessions":[c_1]}
t = Ticket(td)

db_session.add(c_1)
db_session.add(t)
db_session.commit()

print(Ticket.query.filter_by(customerId='1').all())
print(CallLog.query.all())
 
 
 
 
