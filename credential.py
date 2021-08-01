class Credential:
    '''
    Class that generates new instances of user credentials
    '''
    credential_list = []

    def __init__(self, account_name, key):
        self.account_name = account_name
        self.key = key

    def save_credentials(self):
        '''
        this method saves the credentials of a user when they create an account
        '''
        Credential.credential_list.append(self)

    def display_credentials(cls):
        '''
        the method that returns the credentials
        '''
        return cls.credential_list