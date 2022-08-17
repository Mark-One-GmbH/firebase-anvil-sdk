
def test_init_fb():
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
  from .. import firebase_client
  firebase_client.init_client(cred)


