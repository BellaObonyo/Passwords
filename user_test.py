import unittest
import pyperclip
from user import User

class TestUser(unittest.TestCase):
  '''
  Test class that defines test cases for the user class behaviours.

  Args:
    unittest.TestCase: TestCase class that helps in creating user test cases
  '''
  def setUp(self):
    '''
    Set up method to run before each test cases in User
    '''
     self.new_user = User("","NgetiCynthia","0792625077","cynthiabella.obonyo@gmail.com") #creating user object

  def tearDown(self):
    '''
    tearDown method that does clean up after each test case has run.
    '''
    User.user_list = []

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''
