import unittest
from credential import Credential

class TestUser(unittest.TestCase):
    '''
    Test class defining the user credentials
    '''

    def setUp(self):
        '''
        Setup method that runs before each test case
        '''
        self.new_credential = Credential('random', 'any')

    def test_init(self):
        '''
        test method to check if credentials have been initialised properly
        '''
        self.assertEqual(self.new_credential.account_name, 'random')
        self.assertEqual(self.new_credential.key,'any')

    
    if __name__ == '__main__':
        unittest.main()