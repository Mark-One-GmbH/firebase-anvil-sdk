import anvil.server
import firebase_admin
from firebase_admin import credentials, firestore, storage, auth, messaging
from . import sdk_keys

cred = credentials.Certificate(sdk_keys.get_firestore_sdk_config())
firebase_admin.initialize_app(cred,{'storageBucket': sdk_keys.get_bucket_id()})
#Top Level database access
__db = firestore.client()
__bucket = storage.bucket()

  

"""
Client callable functions:
"""

@anvil.server.callable
def fs_server_get_auth_token():
  import anvil.users
  user = anvil.users.get_user()
  user_uid = str(user.get_id())
  
  #create additional claims -> add specific user relevant claims to support security rules
  additional_claims = {
    'user_uid':user_uid,
  }
  
  #Create Firebase Token and return string
  return auth.create_custom_token(user_uid, additional_claims).decode("utf-8") 

  
