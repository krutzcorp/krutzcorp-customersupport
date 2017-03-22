import unittest
import requests
import requests_mock

url = 'http://human-resources.com/employee?employee_id=1'

class HRWrapper:
    def getEmployee(employeeId):
        r = requests.get(url)
        return r

class Stubber:
    def stubMock(m):
        return m.get(url, json={'hello': 'world'}) 
    # This json can be replaced with a real response, 
    # or the response can be passed into the function

class TestCase(unittest.TestCase):

    def testMockCalled(self):
        with requests_mock.mock() as m:
            Stubber.stubMock(m)
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

if __name__ == "__main__":
    unittest.main()
