import pyperclip
import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class defining test cases for user  class
    '''
    def setUp(self):
        '''
        A set up method which runs before each test case
        '''
        self.new_user = User('Fredrick','19xy13!')

    def test_init(self):
        '''
        Test method that checks if the user object is initialised properly
        '''
        self.assertEqual(self.new_user.name, 'Fredrick')
        self.assertEqual(self.new_user.password, '19xy13!')

if __name__ == '__main__':
    unittest.main()