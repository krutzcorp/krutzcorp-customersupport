from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class CallLogTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    def test_call_log_is_reachable(self):
        self.browser.get('http://localhost:5000')
        self.assertIn("New Call", self.browser.title)

        inputbox = self.browser.find_element_by_id('phone_called_from')
        self.assertEqual(inputbox.get_attribute('placeholder'), '(222) 867-5309')

        inputbox.send_keys('555-555-5555')
        inputbox = self.browser.find_element_by_id('phone_call_back')
        self.assertEqual(inputbox.get_attribute('placeholder'), '(222) 867-5309')

        inputbox.send_keys('444-444-4444')

        self.browser.find_element_by_id('submit_button').click()

        self.browser.get('http://localhost:5000/calllog')
        self.assertIn("Call Logs", self.browser.title)

if __name__ == '__main__':
    unittest.main()
