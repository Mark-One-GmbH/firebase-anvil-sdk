import anvil.server


def init_firebase_server(skd_config,bucket_id=None,name='default',project_name=None):
  '''Intializes the serer side firestore sdk'''
  import firebase_admin
  from firebase_admin import credentials, firestore, storage

  if bucket_id is None:
    try:
      app = firebase_admin.initialize_app(credentials.Certificate(skd_config),name=name)
    except ValueError as e:
      if "already exist" not in str(e):
        raise e
      app = firebase_admin.get_app(name=name)
    print(app.name)
    firestore_client = firestore.client(app=app)
    if name != 'default':
      firestore_client._database_string_internal = (f"projects/{project_name}/databases/{name}")
    return firestore_client
  else:
    app = firebase_admin.initialize_app(credentials.Certificate(skd_config),{'storageBucket': bucket_id},name=name)
    return firestore.client(app=app), storage.bucket()


"""
Client callable functions:
"""

@anvil.server.callable
def _fs_get_anvil_firestore_auth_token(user_claims=[]):
  import firebase_admin
  from firebase_admin import auth

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
