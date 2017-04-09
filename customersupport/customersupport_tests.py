import unittest
import requests
import requests_mock
from config import SALES_URL, HR_URL
from customersupport.wrappers import sales
from customersupport.wrappers import hr, mocked_responses

class TestCase(unittest.TestCase):

    def test_hr_employee(self):
        """ test if response of hr wrapper is correct ( hr hasn't given us url yet) """
        actual = hr.get_employee(0)
        expected = mocked_responses.hr_get_employee
        assert actual == expected


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
        actual = sales.get_order_info("John doe 1111 street Rochester NY 14568")
        expected = []
        assert actual == expected


    def test_sales_orderinfo(self):
        """ tests for Sales order information """
        actual = sales.get_order_info(1)
        final = [actual[0].id, actual[0].order_date, actual[0].items]
        expected = [1, '2017-03-01T20:51:26.905Z', set()]
        assert final == expected


    def test_sales_orders_called(self):
        """ tests for Sales Search Order API is called """
        actual = sales.get_order_info("John doe 1111 street Rochester NY 14568", mock=True)
        final = [actual[0].id,actual[0].order_date]
        expected = expected = [1000, '2017-03-01T20:51:26.905Z']
        assert final == expected


    def test_sales_orderinfo_called(self):
        """tests for Sales order information"""
        actual = sales.get_order_info(1, mock=True)
        final = [actual[0].id, actual[0].order_date]
        expected = [1000, '2017-03-01T20:51:26.905Z']
        assert final == expected

    def test_sales_customer_called(self):
        """ Tests to check if search_customer was called """
        actual = sales.search_customer("Joe", mock=True)
        c_first = actual[0].first_name
        expected = "John"
        assert c_first == expected


    def test_hr_employee_called(self):
        """ Tests to check if api address is correct and live """
        actual = hr.get_employee(0, mock=True)
        expected = mocked_responses.hr_get_employee
        assert actual == expected


"""def test_sales_refund_called(self):
        with requests_mock.mock() as m:
            StubberSalesReturn.stubMock(m)
            sales.initiate_refund(True,1,1)
            actual = m.called
            expected = True
            assert actual == expected, "actual: " + str(actual.json())"""


if __name__ == '__main__':
    unittest.main()
