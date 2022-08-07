"""
Exporting the Firebase class as a singelton instance
"""

initialized = False
from . import firestore
from . import authentication

    
def initialize_client(config:dict)->None:
  '''Initializes the firebase class for client side environments'''
  
  #Check credentials input value
  if not isinstance(config,dict):
    raise ValueError('Credentials must be of type dict')

  #Get Firestore javascript modules
  import anvil.js
  anvil.js.import_from("https://www.gstatic.com/firebasejs/8.10.1/firebase-app.js")
  anvil.js.import_from("https://www.gstatic.com/firebasejs/8.10.1/firebase-firestore.js")
  anvil.js.import_from("https://www.gstatic.com/firebasejs/8.10.1/firebase-auth.js")


  #initialize application
  anvil.js.window.firebase.initializeApp(config)
  
  #Init Firestoe
  firestore.enable_offline_persistance()
  firestore.db =  anvil.js.window.firebase.firestore()
  firestore.environment = 'client'
  
  #init authentication
  authentication.auth = anvil.js.window.firebase.auth()
  #todo set persistance
  #firebase.auth().setPersistence(firebase.auth.Auth.Persistence.SESSION)

  
  #Initialization finished
  global initialized
  initialized = True






