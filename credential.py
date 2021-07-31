import pyperclip
class Credential:
  """
  a class that creates new credentials for credentials
  """
  credential_list = []

  def __init__(self, credential_name, password,number):
    self.credential_name = credential_name
    self.password = password
    self.number = number


  def save_credential(self):
    '''
    save_credential method saves credential object into the credential_list
    '''

    Credential.credential_list.append(self)

  def delete_credential(self):
    '''
    delete_credential method deletes a saved credential from the credential_list
    '''

    Credential.credential_list.remove(self)

  @classmethod
  def find_credential_by_number(cls,number):
    '''
    Method that takes in a number and returns a credential that matches that number.
    Args:
      number:Phone number to search for
    Returns:
      credential  that matches the number.
    '''
    for credential in cls.credential_list:
      if credential.number == number:
        return credential

  @classmethod
  def credential_exist(cls,number):
    '''
    Method that checks if a credential exists from the credential list.
    Args:
        number: Phone number to search if it exists
    Returns :
        Boolean: True or false depending if the credential exists
    '''
    for credential in cls.credential_list:
      if credential.number == number:
        return True

    return False

  @classmethod
  def display_credentials(cls):
    '''
    method that returns the credential list
    '''
    return cls.credential_list

  @classmethod
  def copy_pwd(cls,number):
    credential_found = Credential.find_credential_by_number(number)
    pyperclip.copy(credential_found.password)