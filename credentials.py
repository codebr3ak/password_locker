from user import User
from random import choice


class Credentials:
    """
    Class to create and store user credentials
    """
    user_credential = [
    account_credentials = []
    ]

    class Credentials:
    def __init__(self, website, user_name, account_name, password):
    """
    Class to store user credentials
    Class to create and store user credentials
    """
    pass

    def __init__(self, website, username, account_name, password):
        """
        Method to create instances of class Credentials
        """
        self.website = website
        self.user_name = user_name
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        """
        Function that saves new credentials instances
        """
        Credentials.user_credential.append(self)

     def random_password():
        """
        Function that generates an eight-character alphanumeric password
        """
        alphabet = string.ascii_letters + string.digits
        password = ''.join(choice(alphabet) for i in range(8))

    @classmethod
    def auth_user(cls, user_name, password):
        """
        Function to authenticate user by checking the name and password against the users array
        """
        present_user = ""
        for user in User.users:
            if(user.user_name == user_name and user.password == password):
                present_user = user.user_name
            return present_user

    @classmethod
    def display_credentials(cls,user_name):
         """
        Method to display saved account credentials
        """
        for credential in cls.account_credentials:
            if credential.user_name = user_name:
                account_credentials.append(credential)

        return account_credentials

    @classmethod
    def delete_credentials(cls, user_name):
        """
        Method to delete user credentials
        """
        for credential in cls.account_credentials:
            if credential.user_name = user_name:
                account_credentials.remove(credential)
