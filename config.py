import secrets

if(secrets.PRODUCTION):
	print('Using Mysql database')
	DATABASE_URI = 'mysql+pymysql://customersupport:'+secrets.MYSQL_PASS+'@localhost/CustomerSupport'
else:
	print('Using SQLite database')
	DATABASE_URI = 'sqlite:///customer-support.db'

HR_URL = 'http://vm343a.se.rit.edu'
# SALES_URL = 'http://sales.krutz.site'
SALES_URL = 'http://vm343c.se.rit.edu/api'
