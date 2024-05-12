import unittest
from unittest.mock import patch
from raddish.log import Log

class TestLog(unittest.TestCase):

    def setUp(self):
        self.log = Log()

    def test_write_debug(self):
        self.log.write('Debug message', 'DEBUG')

    def test_write_info(self):
        self.log.write('Info message', 'INFO')

    def test_write_warning(self):
        self.log.write('Warning message', 'WARNING')

    def test_write_error(self):
        self.log.write('Error message', 'ERROR')


    def test_write_default(self):
        self.log.write('Default message')

if __name__ == '__main__':
    unittest.main()