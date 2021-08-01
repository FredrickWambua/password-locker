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

    def test_save_user(self):
        '''
        Test method to test if the user has been saved on the user list
        '''
        self.new_user.save_user() # method to save user
        self.assertEqual(len(User.user_list),2) #expecting 1 !=2 since there is only one contact saved currently

    def test_save_many_users(self):
        '''
        Test case to check if multiple users can be saved
        '''
        self.new_user.save_user() # method to save user
        self.assertEqual(len(User.user_list),4)

if __name__ == '__main__':
    unittest.main()