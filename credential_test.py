import unittest
import pyperclip
from credential import Credential

class TestCredential(unittest.TestCase):
  '''
  Test class that defines test cases for the credential class behaviours.
  Args:
    unittest.TestCase: TestCase class that helps in creating credential test cases
  '''
  def setUp(self):
    '''
    Set up method to run before each test cases in credential
    '''
    self.new_credential = Credential("CynthiaObonyo","1234","0792625077") #creating credential object

  def tearDown(self):
    '''
    tearDown method that does clean up after each test case has run.
    '''
    Credential.credential_list = []

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_credential.credential_name,"CynthiaObonyo")
    self.assertEqual(self.new_credential.password,"1234")
    self.assertEqual(self.new_credential.number,"0792625077")
  def test_save_credential(self):
    '''
    test_save_credential test case to test if the credential object is saved into
    the credential list
    '''
    self.new_credential.save_credential() #saving the credential
    self.assertEqual(len(Credential.credential_list),1)

  def test_save_multiple_credential(self):
    '''
    test_save_multiple_credential to check if we can save multiple contact
    objects to our contact list
    '''
    self.new_credential.save_credential()
    test_credential = Credential("BellaCynthia","Bel123","0727611875") #new credential
    test_credential.save_credential()
    self.assertEqual(len(Credential.credential_list),2)

  def test_delete_credential(self):
    '''
    test_delete_credential to test if we can remove a credential from our credential list
    '''
    self.new_credential.save_credential()
    test_credential = Credential("BellaCynthia","Bel123","072761175") #new credential
    test_credential.save_credential()

    self.new_credential.delete_credential() #Deleting a credential object
    self.assertEqual(len(Credential.credential_list),1)

  def test_find_credential_by_number(self):
    '''
    test to check if we can find a credential by phone number and display information
    '''

    self.new_credential.save_credential()
    test_credential = Credential("BellaCynthia","Bel123","072761175") #new credential
    test_credential.save_credential()

    found_credential = Credential.find_credential_by_number("072761175")

    self.assertEqual(found_credential.credential_name,test_credential.credential_name)

  def test_credential_exists(self):
    '''
    test to check if we can return a Boolean if we cannot find a credential
    '''

    self.new_credential.save_credential()
    test_credential = Credential("BellaCynthia","Bel123","072761175") #new credential
    test_credential.save_credential()

    credential_exists = Credential.credential_exist("072761175")

    self.assertTrue(credential_exists)

  def test_display_all_credentials(self):
    '''
    method that returns a list of all credentials saved
    '''
    self.assertEqual(Credential.display_credentials(),Credential.credential_list)

  def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found credential
        '''

        self.new_credential.save_credential()
        Credential.copy_pwd("0792625077")

        self.assertEqual(self.new_credential.password,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()


