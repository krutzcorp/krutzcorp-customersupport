import requests_mock
from customersupport.hrwrapper_spec import Stubber
from customersupport.hrwrapper import HRWrapper

class SessionController:

    def getEmployee():
        HRWrapper.getEmployee(1)

    def getEmployeeStubbed():
        with requests_mock.mock() as m:
            Stubber.stubMock(m)
            return HRWrapper.getEmployee(1)
