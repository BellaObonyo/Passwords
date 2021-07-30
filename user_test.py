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
     self.new_user = User("Cynthia","Obonyo","0792625077","cynthiabella.obonyo@gmail.com") #creating user object

  def tearDown(self):
    '''
    tearDown method that does clean up after each test case has run.
    '''
    User.user_list = []

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''
 
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_user.first_name,"Cynthia")
    self.assertEqual(self.new_user.last_name,"Obonyo")
    self.assertEqual(self.new_user.phone_number,"0792625077")
    self.assertEqual(self.new_user.email,"cynthiabella.obonyo@gmail.com")
  def test_save_user(self):
    '''
    test_save_user test case to test if the user object is saved into
    the user list
    '''
    self.new_user.save_user() #saving the user
    self.assertEqual(len(User.user_list),1)
    def test_save_multiple_user(self):
    '''
    test_save_multiple_user to check if we can save multiple contact
    objects to our contact list
    '''
    self.new_user.save_user()
    test_user = User("Bella","Cynthia","0727611875","obonyocy@ueab.ac.ke") #new user
    test_user.save_user()
    self.assertEqual(len(User.user_list),2)

  def test_delete_user(self):
    '''
    test_delete_user to test if we can remove a user from our user list
    '''
 self.new_user.save_user()
    test_user = User("Adongo","Lorrein","0716578937","adoshe@gmail.com") #new user
    test_user.save_user()

    self.new_user.delete_user() #Deleting a user object
    self.assertEqual(len(User.user_list),1)

  def test_find_user_by_number(self):
    '''
    test to check if we can find a user by phone number and display information
    '''

    self.new_user.save_user()
    test_user = User("Brian","Kenny","0716709243","nightrunner@gmail.com") #new user
    test_user.save_user()
 found_user = User.find_by_number("0714042437")

    self.assertEqual(found_user.email,test_user.email)

  def test_user_exists(self):
    '''
    test to check if we can return a Boolean if we cannot find a user
    '''

    self.new_user.save_user()
    test_user = User("Bella","Cynthia","0727611875","obonyocy@ueab.ac.ke") #new user
    test_user.save_user()

    user_exists = User.user_exist("072761175")

    self.assertTrue(user_exists)

  def test_display_all_users(self):