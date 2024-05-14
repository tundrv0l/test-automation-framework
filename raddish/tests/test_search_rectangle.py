import unittest
from raddish.search_rectangle import SearchRectangle

class TestLog(unittest.TestCase):

    def setUp(self):
        self.rect = SearchRectangle([100, 100, 200, 200])


if __name__ == '__main__':
    unittest.main()