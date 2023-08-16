import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # in case if you want to do smth once at the beginning
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):  # in case you want to do smth once at the end
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Lucas', 'Marietan', 110000)
        self.emp_2 = Employee('John', 'Doe', 55000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Lucas.Marietan@email.com')
        self.assertEqual(self.emp_2.email, 'John.Doe@email.com')

        self.emp_1.first = 'Diana'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'Diana.Marietan@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Doe@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Lucas Marietan')
        self.assertEqual(self.emp_2.fullname, 'John Doe')

        self.emp_1.first = 'Diana'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'Diana Marietan')
        self.assertEqual(self.emp_2.fullname, 'Jane Doe')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 115500)
        self.assertEqual(self.emp_2.pay, 57750)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            # Simulate successful call to API
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success!'

            schedule = self.emp_1.monthly_schedule('May')

            # mocked_get used instead of requests.get and we assert if the API call is made with the correct url
            mocked_get.assert_called_with('http://company.com/Marietan/May')
            self.assertEqual(schedule, 'Success!')

            # Simulate failed call to API
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')

            # mocked_get used instead of requests.get and we assert if the API call is made with the correct url
            mocked_get.assert_called_with('http://company.com/Doe/June')
            self.assertEqual(schedule, 'Bad response!')


if __name__ == '__main__':
    unittest.main()
