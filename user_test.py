import pyperclip
class user:
    '''
    class tat creates new instancesof users
    '''

    user_list =[] # creates an empty user list

    def _init_(self,first_name,last_name,number,email):

        self.first_name = first_name
        self.last