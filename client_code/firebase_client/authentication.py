'''
Firebase Authentication
'''

import anvil.js
proxy_auth = anvil.js.import_from("https://www.gstatic.com/firebasejs/9.9.4/firebase-auth.js")
auth = None

def init(app):
  global auth
  auth = proxy_auth.getAuth()


"""Main Methods"""
def get_user():
  try:
    return FireUser(anvil.js.await_promise(auth.currentUser))
  except Exception as e:
    return None

def logout():
  anvil.js.await_promise(proxy_auth.signOut(auth))

  
def signup_with_email(email,password):
  userCredential = anvil.js.await_promise(proxy_auth.createUserWithEmailAndPassword(auth,email, password))
  return FireUser(userCredential.user)



def login_with_email(email,password):
  userCredential = anvil.js.await_promise(proxy_auth.signInWithEmailAndPassword(auth,email, password))
  return FireUser(userCredential.user)



def login_with_token(token):
  fs_user = anvil.js.await_promise(proxy_auth.signInWithCustomToken(auth,token))
  


'''Wraps a Firestore proxy user'''
class FireUser:
  def __init__(self,proxy_user):
    if proxy_user is None:
      raise ValueError('Unkown Firebase User')
    self.proxy_user = proxy_user

  @property
  def uid(self):
    return self.proxy_user.uid

  def __repr__(self):
    try:
      return f"<FireUser {self.proxy_user.email}>"
    except Exception as e:
      return 'unknown firebase user'