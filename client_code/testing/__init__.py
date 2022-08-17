

def run_all_tests():
  from . import firebase
  from . import auth
  from . import firestore

  firebase.test_init_fb()
  auth.test_auth_with_anvil()
  firestore.get_multiple_documents()
  firestore.add_listener()
  firestore.add_document()
  