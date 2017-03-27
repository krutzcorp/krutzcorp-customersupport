import unittest
from customersupport.models import Employee
from customersupport.controllers import session
from customersupport.wrappers import hr
from customersupport.wrappers import sales
from customersupport import session, customersearch, ordersearch, ticket


class TestCase(unittest.TestCase):
    #def setUp(self):

    #def tearDown(self):
    def routes_tests(self):
        # test HR route
        test_session_user = Employee(session.get_employee_stubbed())
        test_customers = customersearch()
        self.assertEqual(test_session_user.name, "Corbin Mallioux")
        assert len(test_customers) == 2
        assert test_session_user.name == "Corbin Mallioux"
        assert test_session_user.id == "1"

    def test_HR_API(self):
        #should return None since API we're connecting too isn't implemented yet.
        self.assertEqual(hr.get_employee(1,False), None)

    def test_Sales_search_cust(self):
        # should return None since API we're connecting too isn't implemented yet.
            info = ["0","John","Smith"]
            sales_search = sales.search_customer(info[0],info[1],info[2])
            self.assertEqual(sales_search,None)

    def test_sales_refund(self):
        # should return None since API we're connecting too isn't implemented yet.
            info = [True, 24, [20,21]]
            sales_refund = sales.initiate_refund(info[0],info[1],info[2])
            self.assertEqual(sales_refund,None)

    def test_sales_getorders(self):
        # should return None since API we're connecting too isn't implemented yet.
            info = ["address",True,1,True,True,True,True]
            sales_grab_orders = sales.get_orders(info[0],info[1],info[2],info[3],info[4],info[5],info[6])
            self.assertEqual(sales_grab_orders,None)

    def test_sales_orderinfo(self):
        # should return None since API we're connecting too isn't implemented yet.
            info = [1, True, True, True, True]
            sales_order_info = sales.get_order_info(info[0], info[1], info[2], info[3], info[4])
            self.assertEqual(sales_order_info, None)

    #def test_status(self):

if __name__ == '__main__':
    unittest.main()
