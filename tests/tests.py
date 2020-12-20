from instaclient.errors.common import InvalidUserError, InvalidVerificationCodeError, PrivateAccountError, VerificationCodeNecessary
import unittest
from instaclient import InstaClient

# python -m unittest discover -s tests

class TestClient(unittest.TestCase):
    """Test InstaClient methods"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = None

    def test_init(self):
        """
        Test Class __init__()
        """
        username = input('Enter your instagram username: ')
        password = input('Enter your instagram password: ')
        self.client = InstaClient(username, password)
        self.assertNotEqual(self.client, None, 'Should Be of Type Client. Client not created')

    def test_login(self):
        """
        Test Class login()
        """
        try:
            response = self.client.login()
        except VerificationCodeNecessary:
            code = input('Enter the 2FA security code sent to your phone or generated by your Authenticator App:')
            try:
                response = self.client.input_verification_code(code)
            except InvalidVerificationCodeError:
                code = input('The security code you entered is invalid. Please try again: ')
                response = self.client.input_verification_code(code)
        self.assertEqual(response, True, 'Should be True (connected)')

    def test_search_tag(self):
        """
        Test Class search_tag()
        """
        # Test existing tag
        tag = input('Enter an existing IG Tag: ')
        response = self.client.nav_tag(tag) 
        self.assertEqual(response, True, 'Response is false, should be True. Search Existing Tag not Successful')
        # Test inexisting tag
        tag = input('Enter an inexisting IG Tag: ')
        response = self.client.nav_tag(tag)
        self.assertEqual(response, True,  'Response is false, should be True. Search NonExisting Tag not Successful')

    def test_nav_user(self):
        """
        Test Class nav_user()
        """
        # Test Existing User
        user = input('Enter an existing IG username to test nav_user: ')
        response = self.client.nav_user(user)
        self.assertEqual(response, True, 'Response is false, should be True. Search Existing User failed.')
        # Test NonExisting User
        user = input('Enter an inexisting IG username to test nav_user: ')
        response = self.client.nav_user(user)
        self.assertEqual(response, True, 'Response is false, should be True. Search InExisting User failed.')

    def test_nav_user_dm(self):
        """
        Test Class nav_user_dm()
        """
        # Test existing user 
        user = input('Enter an existing IG username to test nav_user_dm: ')
        response = self.client.nav_user_dm(user)
        self.assertEqual(response, True, 'Response is false, should be True. Navifate to Existing User DMs failed.')

        # Test inexisting user
        user = input('Enter an inexisting IG usernameto test nav_user_dm: ')
        response = self.client.nav_user_dm(user)
        self.assertEqual(response, True, 'Response is false, should be True. Navifate to InExisting User DMs failed.')

    def test_get_followers(self):
        """
        Test Class get_followers()
        """
        # Test with existing user
        user = input('Enter a username to get followers: ')
        try:
            response = self.client._scrape_followers(user)
            self.assertIsInstance(response, list, 'Response is not list: type= {} response={}'.format(type(response), response))
        except Exception as error:
            self.assertIsInstance(error, (PrivateAccountError, InvalidUserError), 'An uncaught error has been raised: type={} error= {}'.format(type(error), error))



# TODO test_send_dm()
# TODO test_nav_user_followers()
# TODO test_get_followers()
# TODO test__follow_user()
# TODO test_un_follow_user()
# TODO test_get_user_images()


