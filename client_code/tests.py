
from .firebase import firestore as fs
from .firebase import authentication as auth

def run_tests():
  cred = {
      'apiKey': "AIzaSyDusPnQZzPbV8I_nnwKW1Oj5PbSj_0BLDs",
      'authDomain': "development-945bf.firebaseapp.com",
      'projectId': "development-945bf",
      'storageBucket': "development-945bf.appspot.com",
      'messagingSenderId': "273735084857",
      'appId': "1:273735084857:web:4afc77ceec6c33fde556e8",
      'measurementId': "G-ZTBXYR2MK4"
  }

  #iniitalize firebase
  from . import firebase
  firebase.init_client(cred)

  #Test some
  import anvil.users
  login_email()
  user = get_user()
  print(user)
  #login_token()

"""Firebase Authentication"""
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



    
"""Read Data from Firestore"""
def get_multiple_documents(force_cache=False):
  query = fs.db.collection('test').where('name','==','hello')
  docs = fs.get_docs(query,force_cache=force_cache)
  return docs
  

def get_single_document():
  doc_ref = fs.db.collection('test').doc('doc_uid')
  doc = fs.get_doc(doc_ref)
  return doc
  
  
  
  """Write Data"""
  def set_document():
    doc_ref = fs.db.collection('test').doc('doc_uid')
    doc = fs.get_doc(doc_ref)
    print(doc.data)
  
  def get_single_document():
    doc_ref = fs.db.collection('test').doc('doc_uid')
    doc = fs.get_doc(doc_ref)
    print(doc.data)