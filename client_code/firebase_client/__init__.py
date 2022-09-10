'''
Main Firebase class that handles initialization and access to firebase services
'''

#main module
import anvil.js
proxy_firebase = anvil.js.import_from("https://www.gstatic.com/firebasejs/9.9.4/firebase-app.js")
app = None #initializes late by calling intialize_app()

#export sub modules
from . import firestore
from . import authentication
from . import analytics
from . import storage

    
def initialize_app(config:dict)->None:
  '''Initializes the firebase class for client side environments'''
  
  #Check credentials input value
  if not isinstance(config,dict):
    raise ValueError('Credentials must be of type dict')
  
  #initialize application
  global app
  app = proxy_firebase.initializeApp(config)
  
  #Init Firestoe
  firestore.init(app)






