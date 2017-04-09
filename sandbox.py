from customersupport.models import Ticket, CallLog
from customersupport.database import db_session
from customersupport.database import init_db
import datetime

init_db()

today = datetime.datetime.now()

cl_1 = {"date_called":today,"calling_number":"111-222-3333","callback_number":"111-222-3434","notes":"Nothing to report here","employee":"1","ticket":1}
c_1 = CallLog(cl_1)

td = {"customer_id":"1","issue":"REFUND","date_opened":today,"date_closed":today,"current_status":"CLOSED","sessions":[c_1]}
t = Ticket(td)

td_2 = td
td_2['customer_id']=2
t_2 = Ticket(td_2)

db_session.add(c_1)
db_session.add(t)
db_session.add(t_2)
db_session.commit()

print(Ticket.query.filter_by(customer_id='1').all())
print(CallLog.query.all())
 
 
 
 
