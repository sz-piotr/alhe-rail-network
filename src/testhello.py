import unittest
from hello import get_hello

class TestHello(unittest.TestCase):

    def test_get_hello(self):
        self.assertEqual(get_hello(), 'hello')


if __name__ == '__main__':
    unittest.main()
