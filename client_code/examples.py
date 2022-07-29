
from .firebase import firestore as fs
from .firebase import authentication as auth

"""Firebase Authentication"""
def get_user():
  user = auth.get_user()
  print(user)
    
def sign_up():
  user = auth.create_user_with_email_and_password('test@testing.com','password')


def auth_state_changed(user):
  print(f'auth state chagned',user)

def sign_in():
  user = auth.sign_in_with_email_and_password('test@testing.com','password')

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