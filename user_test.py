import unittest
from user import User


class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for User class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creates test cases
    """

    def setUp(self):
        """
        Setup method to run before each test cases
        """
        self.new_user = User("Baraka", "Ralph", "rbaraka", "pass12345")

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.first_name, "Baraka")
        self.assertEqual(self.new_user.last_name, "Ralph")
        self.assertEqual(self.new_user.user_name, "rbaraka")
        self.assertEqual(self.new_user.password, 'pass12345')

    def test_save_user(self):
        """
        Test to asertain that the new user is saved into the users list and check the users list length
        """
        self.new_user.save_user()
        self.assertEqual(len(User.users), 1)


if __name__ == '__main__':
    unittest.main()

