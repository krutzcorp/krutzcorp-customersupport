import requests

url = 'http://human-resources.com/employee?employee_id=1'

class HRWrapper:
    def getEmployee(employeeId):
        r = requests.get(url)
        return r

