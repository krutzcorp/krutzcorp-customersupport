import unittest
from customersupport.wrappers import sales
from customersupport.wrappers import hr

class TestCase(unittest.TestCase):

    def test_hr_employee(self):
        """ test if response of hr wrapper is correct ( hr hasn't given us url yet) """
        actual = hr.get_employee(0)
        final = [actual.name, actual.id]
        expected = ['Wendy Williams', 1]
        assert final == expected


    def test_sales_customer(self):
        """ tests for Sales Customer """
        actual = sales.search_customer("Joe")
        c_first = actual[0].first_name
        expected = "Joe"
        assert c_first == expected


# Cant put data into sales DB
    """def test_sales_refund(self):
        with requests_mock.mock() as m:
            StubberSalesReturn.stubMock(m)
            actual = sales.initiate_refund(True,1,1)
            expected = {}
            assert actual.json() == expected, "actual:" + str(actual.json())"""


    def test_sales_orders(self):
        """ tests for Sales order lookup Empty dic since there are currently 0 orders """
        actual = sales.get_order_info(1)
        final = [actual.id, actual.order_date]
        expected = [1,'1970-01-21T02:39:21.000Z']
        assert final == expected


    def test_sales_orderinfo(self):
        """ tests for Sales order information """
        actual = sales.get_order_info(1)
        final = [actual.id, actual.order_date, actual.items]
        expected = [1, '1970-01-21T02:39:21.000Z', actual.items]
        assert final == expected


    def test_sales_orders_called(self):
        """ tests for Sales Search Order API is called """
        actual = sales.get_order_info("John doe 1111 street Rochester NY 14568", mock=True)
        final = [actual[0].id,actual[0].order_date]
        expected = [1000, '2017-03-01T20:51:26.905Z']
        assert final == expected


    def test_sales_orderinfo_called(self):
        """tests for Sales order information"""
        actual = sales.get_order_info(1, mock=True)
        expected = [1000, '2017-03-01T20:51:26.905Z']
        assert actual == expected

    def test_sales_customer_called(self):
        """ Tests to check if search_customer was called """
        actual = sales.search_customer("Joe", mock=True)
        c_first = actual[0].first_name
        expected = "Joe"
        assert c_first == expected


    def test_hr_employee_called(self):
        """ Tests to check if api address is correct and live """
        actual = hr.get_employee(0, mock=True)
        final = [actual.name, actual.id]
        expected = ['Wendy Williams', 1]
        assert final == expected


    def test_sales_return_called(self):
        serial_id = [20, 25]
        actual = sales.initiate_refund(False, 24, serial_id, mock=True)
        print(actual)

    def test_sales_replace_called(self):
        serial_id = [20,25]
        actual = sales.initiate_refund(True, 24, serial_id, mock=True)
        print(actual)
        return False






if __name__ == '__main__':
    unittest.main()
