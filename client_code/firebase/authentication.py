import anvil.js

'''
root level access to the firestore database, is iniitlaized from firebase core
'''
auth = None

def _auth():
  import anvil.js
  return anvil.js.window.firebase.auth()

"""Main Methods"""

def get_user():
  try:
    return FireUser(anvil.js.await_promise(_auth().currentUser))
  except Exception as e:
    return None

def logout():
  anvil.js.await_promise(_auth().signOut())

  
def signup_with_email(email,password):
  try:
    userCredential = anvil.js.await_promise(_auth().createUserWithEmailAndPassword(email, password))
    return FireUser(userCredential.user)
  except Exception as e:
    print(f"Error signing up to firestore",e)


def login_with_email(email,password):
  try:
    userCredential = anvil.js.await_promise(_auth().signInWithEmailAndPassword(email, password))
    return FireUser(userCredential.user)
  except Exception as e:
    print(f"Error signing in to firestore",e)



'''Wraps a Firestore proxy user'''
class FireUser:
  def __init__(self,proxy_user):
    if proxy_user is None:
      raise ValueError('Unkown Firebase User')
    self.proxy_user = proxy_user

  @property
  def uid(self):
    return self.proxy_user.uid