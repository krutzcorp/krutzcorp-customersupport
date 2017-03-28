import unittest
import requests
import requests_mock
from config import SALES_URL, HR_URL
from customersupport.wrappers import sales
from customersupport.models import Employee
from customersupport.wrappers import hr
from customersupport.wrappers import hr as hr_wrapper


class Stubber:
    @staticmethod
    def stubMock(m,json=None):
        if json is None:
            return m.get(HR_URL, json={'hello': 'world'})
        else:
            return m.get(HR_URL, json=json)
            # This json can be replaced with a real response,
            # or the response can be passed into the function
class StubberSalesCustomer:
    def stubMock(m, json=None):
        json = {'customers': [{'customerId': 2, 'firstName': 'Joe', 'lastName': 'Jefferson', 'email': 'therealjoe@joemail.com', 'phone': '1231231234'}]}
        if json is None:
            return m.get(SALES_URL, json={'Hola': 'Hola'})
        else:
            return m.get('http://vm343c.se.rit.edu/api/customer?firstName=Joe',json=json)
class StubberSalesOrder:
    def stubMock(m, json=None):
        text = 'http://vm343c.se.rit.edu/api/order/search?address=John+doe+1111+street+Rochester+NY+14568&billingAddress=False&paymentInfo=False&shippingInfo=False&customerInfo=False&items=False'
        json ={"orders":[]}
        if json is None:
            return m.get(SALES_URL, json={'Hola': 'Hola'})
        else:
            return m.get(text,json=json)
class StubberSalesOrderInfo:
    def stubMock(m, json=None):
        text = 'http://vm343c.se.rit.edu/api/order?orderId=1&paymentInfo=False&shippingInfo=False&customerInfo=False&items=False'
        json = {"orders":[{"id":1,"customerId":1,"repId":99,"cost":200,"orderDate":"2017-03-01T20:51:26.905Z","isPaid":False,"taxPercentage":8}]}
        if json is None:
            return m.get(SALES_URL, json={'Hola': 'Hola'})
        else:
            return m.get(text,json=json)
class StubberSalesReturn:
    def stubMock(m, json=None):
        json={'Hola': 'Hola'}
        if json is None:
            return m.get(SALES_URL, json={'Hola': 'Hola'})
        else:
            return m.get('http://vm343c.se.rit.edu/api/return',json=json)


class TestCase(unittest.TestCase):

    #def setUp(self):
        #tbd implemented

    #def tearDown(self):
        #tbd implemented

#test if wrapper is called
    def test_HR_API(self):
        # should return None we dont know the URL for the API
        self.assertEqual(isinstance(hr.get_employee(1, False),Employee),False)

#test if hr wrapper is called. Uncomment when we have url address
    """def testHRMockCalled(self):
        with requests_mock.mock() as m:
            Stubber.stubMock(m)
            hr_wrapper.get_employee(1)
            actual = m.called
            expected = True
            assert actual == expected, "actual: " + str(actual.json())"""

#test if response of hr wrapper is correct ( hr hasn't given us url yet)
    """def testHRMockReturnsCorrectResponse(self):
        with requests_mock.mock() as m:
            Stubber.stubMock(m)
            actual = hr.get_employee(1)
            expected = {"employee_id": 1, "name": "Corban Mailloux"}
            assert actual.json() == expected, "actual: " + str(actual.json())"""

#tests for Sales Customer
    def test_sales_customer(self):
        with requests_mock.mock() as m:
            StubberSalesCustomer.stubMock(m)
            actual = sales.search_customer("Joe")
            c_first = actual[0].first_name
            expected = "Joe"
            assert c_first == expected

#Tests to check if search_customer was called
    def test_sales_customer_called(self):
        with requests_mock.mock() as m:
            StubberSalesCustomer.stubMock(m)
            sales.search_customer("Joe")
            actual = m.called
            expected = True
            assert actual == expected, "actual: " + str(actual.json())

# Cant put data into sales DB
    """def test_sales_refund(self):
        with requests_mock.mock() as m:
            StubberSalesReturn.stubMock(m)
            actual = sales.initiate_refund(True,1,1)
            expected = {}
            assert actual.json() == expected, "actual:" + str(actual.json())"""

# API for returns doesn't exist yet so should be 404
    def test_sales_refund_called(self):
        '''with requests_mock.mock() as m:
            StubberSalesReturn.stubMock(m)
            sales.initiate_refund(True,1,1)
            actual = m.called
            expected = True
            assert actual == expected, "actual: " + str(actual.json())'''

#tests for Sales order lookup Empty dic since there are currently 0 orders
    def test_sales_orders(self):
        with requests_mock.mock() as m:
            StubberSalesOrder.stubMock(m)
            actual = sales.get_orders("John doe 1111 street Rochester NY 14568")
            expected = []
            assert actual == expected

    def test_sales_orders_called(self):
        with requests_mock.mock() as m:
            StubberSalesOrder.stubMock(m)
            sales.get_orders("John doe 1111 street Rochester NY 14568")
            actual = m.called
            expected = True
            assert actual == expected, "actual: " + str(actual.json())

#tests for Sales order information
    def test_sales_orderinfo(self):
        with requests_mock.mock() as m:
            final = []
            StubberSalesOrderInfo.stubMock(m)
            actual = sales.get_order_info(1)
            final = [actual[0].id, actual[0].order_date, actual[0].items]
            expected = [1, '2017-03-01T20:51:26.905Z', set()]
            assert final == expected

    '''def test_sales_orderinfo_called(self):
        with requests_mock.mock() as m:
            StubberSalesOrderInfo.stubMock(m)
            sales.get_order_info(1)
            actual = m.call
            expected = True
            assert actual == expected, "actual: " + str(actual.json())'''

#check to see if server is alive
    def test_sales_orderinfo_called(self):
        r = requests.get('http://vm343c.se.rit.edu/api/order?orderId=1&paymentInfo=False&shippingInfo=False&customerInfo=False&items=False')
        assert r.status_code == 200

if __name__ == '__main__':
    unittest.main()
