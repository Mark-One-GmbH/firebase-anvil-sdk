from ..firebase_client import authentication as auth
from datetime import datetime


def test_auth_with_anvil():
  import anvil.users
  anvil.users.login_with_form()
  auth.login_with_anvil()

def get_user():
  user = auth.get_user()
  print(user)
    
def sign_up():
  user = auth.signup_with_email('test@testing.com','password')

def auth_state_changed(user):
  print(f'auth state chagned',user)

def login_email():
  user = auth.login_with_email('test@testing.com','password')

def login_token():
  some_token = ''
  user = auth.login_with_token(some_token)

def sign_out():
  auth.sign_out()
