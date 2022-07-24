"""
Exporting the Firebase class as a singelton instance
"""


from . import firestore
from . import authentication

    
    
def initialize_app(config:dict)->None:
  '''Initializes the firebase class'''
  
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
  firestore.db =  anvil.js.window.firebase.firestore()


    





