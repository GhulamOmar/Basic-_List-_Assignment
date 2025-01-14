import unittest
from unittest.mock import patch
import fun_with_collections.basic_list as basic_list


class MyTestCase(unittest.TestCase):
 def test_make_list(self):
   with patch('fun_with_collections.basic_list.get_input', return_value='9'):
    def test_make_list(self, input):
        self.assertEqual(basic_list.make_list(input), [8, 6, 9])


if __name__ == '__main__':
    unittest.main()
