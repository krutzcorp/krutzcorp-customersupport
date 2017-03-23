import unittest
import requests_mock
from customersupport.hrwrapper import HRWrapper

url = 'http://human-resources.com/employee?employee_id=1'

class TestCase(unittest.TestCase):

    def testMockCalled(self):
        with requests_mock.mock() as m:
            #Stubber.stubMock(m)
            HRWrapper.getEmployee(1)
            actual = m.called
            expected = True
            assert actual == expected, "actual: " + str(actual.json()) 

    def testMockReturnsCorrectResponse(self):
        with requests_mock.mock() as m:
            Stubber.stubMock(m)
            actual = HRWrapper.getEmployee(1)
            expected = {'hello': 'world'}
            assert actual.json() == expected, "actual: " + str(actual.json()) 

class Stubber:
    def stubMock(m):
        url = 'http://human-resources.com/employee?employee_id=1'
        return m.get(url, json={'hello': 'world'}) 
    # This json can be replaced with a real response, 
    # or the response can be passed into the function

if __name__ == "__main__":
    unittest.main()
