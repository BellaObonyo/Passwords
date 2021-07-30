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