#!/usr/bin/env python3.6
import random
from user import User
from credential import Credential

#functions for user_account
def create_user(fname,lname,phone,email):
  '''
  Function to create a new user
  '''
  new_user = User(fname,lname,phone,email)
  return new_user

def save_user(user):
  '''
  Function to save user
  '''
  user.save_user()

def del_user(user):
  '''
  Function to delete a user
  '''
  user.delete_user()

def copy_email(user,number):
  '''
  Function to delete a user
  '''
  user.copy_email(number)

def find_user(number):
  '''
  Function that finds a user by number and returns the user
  '''
  return User.find_by_number(number)

def check_existing_user(number):
  '''
  Function that check if user exists with number and returns a Boolean
  '''
  return User.user_exist(number)

def display_users():
  '''
  Function that returns all the saved users
  '''
  return User.display_users()



#functions for user_credential
def create_credential(uname,password,phone):
  '''
  Function to create a new credential
  '''
  new_credential = Credential(uname,password,phone)
  return new_credential

def save_credential(credential):
  '''
  Function to save credential
  '''
  credential.save_credential()

def del_credential(credential):
  '''
  Function to delete a credential
  '''
  credential.delete_credential()

def copy_pwd(credential,number):
  '''
  Function to delete a credential
  '''
  credential.copy_pwd(number)

def find_credential(number):
  '''
  Function that finds a credential by number and returns the credential
  '''
  return Credential.find_credential_by_number(number)

def check_existing_credential(number):
  '''
  Function that check if credential exists with number and returns a Boolean
  '''
  return Credential.credential_exist(number)

def display_credentials():
  '''
  Function that returns all the saved credentials
  '''
  return Credential.display_credentials()


def main():
  print("Welcome to your password locker account \n")
  print("Enter command to chose what to do: \n create - command to create new account choosing your own password  \n create-auto - command to create account with auto generated password \n exit - command to exit the program \n")

  while True:
    short_code = input().lower()

    #user creating own password
    if short_code == 'create':
      print("New user Account")
      print("-"*10)

      print ("Enter your first name ....")
      f_name = input()

      print("Enter your last name ...")
      l_name = input()

      print("Enter your username ...")
      u_name = input()
      print("Enter password ...")
      u_password = input()

      print("Enter your phone number ...")
      p_number = input()

      print("Enter your email address ...")
      e_address = input()
      print("-"*10)
      print("-"*60)

      save_user(create_user(f_name,l_name,p_number,e_address)) # create and save new user.
      print(f"New user {f_name} {l_name} created")
      print("-"*10)

      save_credential(create_credential(u_name,u_password,p_number)) # create and save new user.
      print(f"New Credentials: username = {u_name} , password = {u_password} created")
      print("-"*10)
      print("Enter command login -to login to your account")

    #creating account with auto generated password
    if short_code == 'create-auto':
      print("New user Account")
      print("-"*10)

      print ("Enter first name ....")
      f_name = input()

      print("Enter last name ...")
      l_name = input()

      print("Enter username ...")
      u_name = input()
      print("-"*10)
      print("-"*60)
      characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!-/\|_@#$%&*?"
      u_password = "".join(random.sample(characters, 8))
      print(f"Your autogenerated password is {u_password}")
       print("\n")
      print("Enter Phone number ...")
      p_number = input()

      print("Enter email address ...")
      e_address = input()
      print("-"*10)
      print("-"*60)

      save_user(create_user(f_name,l_name,p_number,e_address)) # create and save new user.
      print(f"New user {f_name} {l_name} created")
      print("-"*10)

      save_credential(create_credential(u_name,u_password,p_number)) # create and save new user.
      print(f"New Credentials: username = {u_name} , password = {u_password} created")
      print("-"*10)
      print("Enter command login -to login to your account")

    #Login code
    if short_code == 'login':
      print("Welcome to login Interface")
      print("Enter your username")
      input_user_name = input()

      print("Enter your password")
      input_user_password = input()
      print("-"*10)
      print("-"*60)

      if input_user_name != u_name or input_user_password != u_password:
        print("ACCESS DENIED!!")
        print("Invalid username or password!!!!")
        print("Try again")
      else:
        print("ACCESS GRANTED!!")
        print(f"Welcome {f_name} {l_name} to your account")
        print("Use the following command to do some action with your account: \n create - command to create new account with user choosing own password  \n create-auto - command to create account with auto generated password \n display-u -command to display user details \n find-u - command to search for user \n delete-u - command to delete user \n copy-e - command to copy email address \n display-c - command to display credentials \n find-c - command to search credentials \n delete-c - command to delete credentials \n copy-pwd -command to copy password ")

    elif short_code == 'display-u':

      if display_users():
        print("Here is a list of all your users")
        print('\n')

        for user in display_users():
          print(f"{user.first_name} {user.last_name} .....{user.phone_number}")

        print('\n')
      else:
        print('\n')
        print("You dont seem to have any users saved yet")
        print('\n')

    #display credentials
    elif short_code == 'display-c':

      if display_credentials():
        print("Here is a list of all your credentials")
        print('\n')

        for credential in display_credentials():
          print(f"Username: {credential.credential_name}, password:  {credential.password} .....{credential.number}")

        print('\n')
      else:
        print("You dont seem to have any users saved yet")
        print('\n')

    #find user
    elif short_code == 'find-u':
      print("Enter the number you want to search for")

      search_number = input()
      print("-"*10)
      print("-"*60)
      if check_existing_user(search_number):
        search_user = find_user(search_number)
        print(f"{search_user.first_name} {search_user.last_name}")
        print('-' * 20)

        print(f"Phone number.......{search_user.phone_number}")
        print(f"Email address.......{search_user.email}")
      else:
           print("That user does not exist")

    #find credential
    elif short_code == 'find-c':
      print("Enter the number you want to search credential from")


      search_number = input()
      print("-"*10)
      print("-"*60)
      if check_existing_credential(search_number):
        search_credential = find_credential(search_number)
        print(f"Username: {search_credential.credential_name}, Password: {search_credential.password}, Phone: {search_credential.number}")
        print('-' * 20)

      else:
        print("That credential does not exist")

    #delete user
    elif short_code == 'delete-u':

      print("Enter the number you want to delete")

      delete_number = input()
      print("-"*10)
      print("-"*60)
      if check_existing_user(delete_number):
        dl_user = find_user(delete_number)
        print(f"<<{dl_user.first_name}>> <<{dl_user.last_name}>> will be deleted")
        dl_user = del_user(dl_user)
        print("User deleted successfully")

      else:
        print("That user does not exist")

    #delete credential
    elif short_code == 'delete-c':

      print("Enter the number you want to delete password from")

      delete_number = input()
      print("-"*10)
      print("-"*60)
      if check_existing_credential(delete_number):
        dl_pwd = find_credential(delete_number)
        print(f"<<{dl_pwd.credential_name}>> with password <<{dl_pwd.password}>> will be deleted")
        dl_pwd = del_credential(dl_pwd)
        print("Credential deleted successfully")

      else:
        print("That credential does not exist")

    #copy email
    elif short_code == 'copy-e':

      print("Enter the number you want to copy email from")

      find_number = input()
      print("-"*10)
      print("-"*60)
      if check_existing_user(find_number):
        email_user = find_user(find_number)
        print(f"{email_user.first_name} {email_user.last_name}  {email_user.email} email address will be copied")
        email_user = copy_email(email_user,find_number)
        print("Email address copied successfully")

      else:
        print("That user does not exist")

    #copy password 
    elif short_code == 'copy-pwd':

      print("Enter the number you want to copy password from")

      find_number = input()
      print("-"*10)
      print("-"*60)
      if check_existing_credential(find_number):
        pwd_credential = find_credential(find_number)
        print(f"Password: {pwd_credential.password}  will be copied")
        pwd_credential = copy_pwd(pwd_credential,find_number)
        print("Password copied successfully")

      else:
        print("That user does not exist")

    elif short_code == "exit":
      print("Bye .......")
      break
    else:
      print("")

if _name_ == '_main_':

  main()