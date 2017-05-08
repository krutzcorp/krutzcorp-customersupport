import unittest
from customersupport.wrappers import sales
from customersupport.wrappers import hr

class TestCase(unittest.TestCase):

    def test_hr_employee(self):
        """ test if response of hr wrapper is correct """
        actual = hr.get_employee(158)
        final = [actual.name, actual.id]
        expected = ['Eric Yoon', 158]
        assert final == expected


    def test_sales_customer(self):
        """ tests for Sales Customer """
        actual = sales.search_customer("Joe")
        c_first = actual[0].first_name
        expected = "Joe"
        assert c_first == expected


    def test_sales_orders(self):
        """ tests for sales order lookup  """
        actual = sales.get_orders("286 Broadway")
        final = []
        for ord in actual:
            a = [ord.id, ord.order_date]
            final.append(a)
        expected =[[1, '1970-01-27T07:59:20.000Z'], [2, '1970-01-22T03:43:37.402Z'], [3, '1970-02-02T13:34:13.347Z'], [10, '2017-05-08T15:52:16.257Z']]
        assert final == expected


    def test_sales_orderinfo(self):
        """ tests for Sales order information """
        actual = sales.get_order_info(1)
        final = [actual.id, actual.order_date, actual.items]
        expected = [1, '1970-01-27T07:59:20.000Z', []]
        assert final == expected


    def test_sales_orders_called(self):
        """ tests for Sales Search Order API is called """
        actual = sales.get_orders("286 Broadway")
        final = []
        for ord in actual:
            a = [ord.id, ord.order_date]
            final.append(a)
        expected = [[1, '1970-01-27T07:59:20.000Z'], [2, '1970-01-22T03:43:37.402Z'], [3, '1970-02-02T13:34:13.347Z'], [10, '2017-05-08T15:52:16.257Z']]
        assert final == expected


    def test_sales_orderinfo_called(self):
        """tests for Sales order information"""
        actual = sales.get_order_info(1, mock=True)
        final = [actual.items, actual.order_date, actual.id]
        expected = [[], '1970-01-27T07:59:20.000Z', 1]
        assert final == expected

    def test_sales_customer_called(self):
        """ Tests to check if search_customer was called """
        actual = sales.search_customer("Joe", mock=True)
        c_first = actual[0].first_name
        expected = "Joe"
        assert c_first == expected


    def test_hr_employee_called(self):
        """ Tests to check if api address is correct and live """
        actual = hr.get_employee(1, mock=True)
        final = [actual.name, actual.id]
        expected = ['Joseph Campione', 1]
        assert final == expected

    def test_sales_return_called(self):
        serial_id = [20, 25]
        actual = sales.initiate_refund(False, 24, 20, mock=True)
        assert actual.status_code == 200

    def test_sales_replace_called(self):
        serial_id = [120133]
        actual = sales.initiate_refund(True, 1, serial_id, mock=True)
        assert actual.status_code == 200

if __name__ == '__main__':
    unittest.main()
