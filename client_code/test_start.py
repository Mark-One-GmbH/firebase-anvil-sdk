


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
firebase.initialize_client(cred)

from . import examples
#examples.sign_up()
from datetime import datetime
start = datetime.now()
examples.sign_in()
print(f'signing in took',datetime.now()-start)
examples.get_user()
examples.sign_out()
examples.get_user()

import anvil.users
start = datetime.now()
anvil.users.login_with_form(remember_by_default=True)
print(f'signing in anvil took',datetime.now()-start)






