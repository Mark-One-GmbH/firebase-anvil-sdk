import anvil.server
import firebase_admin
from firebase_admin import credentials, firestore, storage, auth, messaging


def init_firebase_server(skd_config,bucket_id=None):
  '''Intializes the serer side firestore sdk'''
  if bucket_id is None:
    firebase_admin.initialize_app(credentials.Certificate(skd_config))
    return firestore.client()
  else:
    firebase_admin.initialize_app(credentials.Certificate(skd_config),{'storageBucket': bucket_id})
    return firestore.client(), storage.bucket()

  

"""
Client callable functions:
"""

@anvil.server.callable
def _fs_get_anvil_firestore_auth_token(user_claims=[]):
  import anvil.users
  user = anvil.users.get_user()
  user_uid = str(user.get_id())
  
  #create additional claims -> add specific user relevant claims to support security rules
  additional_claims = {
    'user_uid':user_uid,
  }
  for claim in user_claims:
    additional_claims[claim] = user[claim]
  
  #Create Firebase Token and return string
  return auth.create_custom_token(user_uid, additional_claims).decode("utf-8") 

  
