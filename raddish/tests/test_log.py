import unittest
from unittest.mock import patch
from raddish.log import Log

class TestLog(unittest.TestCase):

    def setUp(self):
        self.log = Log()

    def test_write_debug(self):
        self.log.write('Debug message', 'DEBUG')

if __name__ == '__main__':
    unittest.main()