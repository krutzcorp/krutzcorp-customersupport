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
        json = {'Hola': 'hola'}
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

    #def tearDown(self):

#test if server is alive
    '''def test_sales_response(self):
        test = SALES_URL + '/customer'
        response = requests.get(test)
        assert (response.ok)
    def test_sales_response2(self):
        test = SALES_URL + '/return'
        response = requests.get('http://vm343c.se.rit.edu/api/return')
        assert (response.ok)
    def test_sales_response3(self):
        test = SALES_URL + '/search'
        response = requests.get('http://vm343c.se.rit.edu/api/search')
        assert(response.ok)
    def test_sales_response4(self):
        test = SALES_URL + '/order'
        response = requests.get('http://vm343c.se.rit.edu/api/order')
        assert(response.ok)
    def test_hr_response1(self):
        test = HR_URL + '/customer'
        response = requests.get(test)
        assert(response.ok)'''

#test if wrapper is called
    def test_HR_API(self):
        # should return None since API isn't returning data yet
        self.assertEqual(isinstance(hr.get_employee(1, False),Employee),True)

#test if hr wrapper is working
    def testHRMockCalled(self):
        with requests_mock.mock() as m:
            Stubber.stubMock(m)
            hr_wrapper.get_employee(1)
            actual = m.called
            expected = True
            assert actual == expected, "actual: " + str(actual.json())

#test if response of hr wrapper is correct
    def testHRMockReturnsCorrectResponse(self):
        with requests_mock.mock() as m:
            Stubber.stubMock(m)
            actual = hr.get_employee(1)
            expected = {"employee_id": 1, "name": "Corban Mailloux"}
            assert actual.json() == expected, "actual: " + str(actual.json())

#tests for Sales Customer
    def test_sales_customer(self):
        with requests_mock.mock() as m:
            StubberSalesCustomer.stubMock(m)
            actual = sales.search_customer("Joe")
            expected = {"firstName": "Joe"}
            assert actual.json() == expected, "actual:" + str(actual.json())

    def test_sales_customer_called(self):
        with requests_mock.mock() as m:
            StubberSalesCustomer.stubMock(m)
            sales.search_customer("Joe")
            actual = m.called
            expected = True
            assert actual == expected, "actual: " + str(actual.json())

#tests for Sales Refund
    def test_sales_refund(self):
        with requests_mock.mock() as m:
            StubberSalesReturn.stubMock(m)
            actual = sales.initiate_refund(True,1,1)
            expected = {}
            assert actual.json() == expected, "actual:" + str(actual.json())

    def test_sales_refund_called(self):
        with requests_mock.mock() as m:
            StubberSalesReturn.stubMock(m)
            sales.initiate_refund(True,1,1)
            actual = m.called
            expected = True
            assert actual == expected, "actual: " + str(actual.json())

#tests for Sales order lookup
    def test_sales_orders(self):
        with requests_mock.mock() as m:
            StubberSalesOrder.stubMock(m)
            actual = sales.get_orders("John doe 1111 street Rochester NY 14568")
            expected = {"orders":[]}
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
            StubberSalesOrderInfo.stubMock(m)
            actual = sales.get_order_info(1)
            expected = {}
            assert actual.json() == expected, "actual:" + str(actual.json())

    def test_sales_orderinfo_called(self):
        with requests_mock.mock() as m:
            StubberSalesOrderInfo.stubMock(m)
            sales.get_order_info(1)
            actual = m.call
            expected = True
            assert actual == expected, "actual: " + str(actual.json())


if __name__ == '__main__':
    unittest.main()
