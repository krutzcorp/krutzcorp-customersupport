import unittest
import requests_mock
from customersupport.wrappers import hr as hr_wrapper
from config import HR_URL


class TestCase(unittest.TestCase):
    def testMockCalled(self):
        with requests_mock.mock() as m:
            Stubber.stubMock(m)
            hr_wrapper.get_employee(1)
            actual = m.called
            expected = True
            assert actual == expected, "actual: " + str(actual.json())

    def testMockReturnsCorrectResponse(self):
        with requests_mock.mock() as m:
            Stubber.stubMock(m)
            actual = hr_wrapper.get_employee(1)
            expected = {'hello': 'world'}
            assert actual.json() == expected, "actual: " + str(actual.json())


class Stubber:
    @staticmethod
    def stubMock(m, json=None):
        if json is None:
            return m.get(HR_URL, json={'hello': 'world'})
        else:
            return m.get(HR_URL, json=json)
            # This json can be replaced with a real response,
            # or the response can be passed into the function


if __name__ == "__main__":
    unittest.main()
