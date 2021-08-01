class User:
    '''
    initialise a class that generates new instance of user accounts
    '''
    user_list = [] 

    def __init__(self,name,password): #creates a user instance
        self.name = name
        self.password = password

    def save_user(self):
        '''
        this is the method that saves a user when they create an account
        '''
        User.user_list.append(self)
