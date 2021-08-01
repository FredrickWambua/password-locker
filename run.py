from user import User
from credential import Credential
import random
import string
import numbers
import getpass
import pyperclip

def create_credential(account_name, key):
    '''
    the function that creates a new credential
    '''
    new_credential = Credential(account_name, key)
    return new_credential
