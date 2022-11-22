'''
Firebase Authentication
'''

import anvil.js
proxy_auth = anvil.js.import_from("https://www.gstatic.com/firebasejs/9.13/firebase-auth.js")
auth = None

def init(app):
  global auth
  auth = proxy_auth.getAuth(app)
  proxy_auth.setPersistence(auth,proxy_auth.indexedDBLocalPersistence)
  

"""Main Methods"""
def get_user():
  try:
    return FireUser(anvil.js.await_promise(auth.currentUser))
  except Exception as e:
    print('Warning user not found ',e)
    return None

def logout_user():
  anvil.js.await_promise(proxy_auth.signOut(auth))

  
def signup_with_email(email,password):
  userCredential = anvil.js.await_promise(proxy_auth.createUserWithEmailAndPassword(auth,email, password))
  return FireUser(userCredential.user)


def sign_in_with_email(email,password):
  '''Checks if a user is already logged in, if not attempts login flow'''
  userCredential = anvil.js.await_promise(proxy_auth.signInWithEmailAndPassword(auth,email, password))
  return FireUser(userCredential.user)


def sign_in_with_token(token):
  '''Login with a custom token generated with the firebase sdk'''
  return anvil.js.await_promise(proxy_auth.signInWithCustomToken(auth,token))

def login_with_anvil(user_claims=[]):
  import anvil.server
  token = anvil.server.call('_fs_get_anvil_firestore_auth_token',user_claims)
  return sign_in_with_token(token)

'''Wraps a Firestore proxy user'''
class FireUser:
  def __init__(self,proxy_user):
    if proxy_user is None:
      raise ValueError('Unkown Firebase User')
    self.proxy_user = proxy_user

  @property
  def uid(self):
    return self.proxy_user.uid

  @property
  def email(self):
    return self.proxy_user.email

  def logout(self):
    logout_user()
  
  def __repr__(self):
    try:
      return f"<FireUser {self.uid} {self.email}>"
    except Exception as e:
      print(e)
      return 'unknown firebase user'