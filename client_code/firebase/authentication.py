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
  proxy_user = anvil.js.await_promise(_auth().currentUser)

def sign_out():
  anvil.js.await_promise(_auth().signOut())

  
def create_user_with_email_and_password(email,password):
  try:
    userCredential = anvil.js.await_promise(_auth().createUserWithEmailAndPassword(email, password))
    return FireUser(userCredential.user)
  except Exception as e:
    print(f"Error signing up to firestore",e)


def sign_in_with_email_and_password(email,password):
  try:
    userCredential = anvil.js.await_promise(_auth().signInWithEmailAndPassword(email, password))
    return FireUser(userCredential.user)
  except Exception as e:
    print(f"Error signing in to firestore",e)

def listen_to_auth_state_changed(user,callback):
  _auth().onAuthStateChanged(user,callback) 


'''Wraps a Firestore proxy user'''
class FireUser:
  def __init__(self,proxy_user):
    self.proxy_user = proxy_user

  @property
  def uid(self):
    return self.proxy_user.uid