'''
Main Firebase class that handles initialization and access to firebase services
'''

#main module
import anvil.js

proxy_firebase = None
app = None #initializes late by calling intialize_app()

#export sub modules
from . import firestore
from . import authentication
from . import storage
from . import functions


def initialize_app(config:dict,database=None,enable_offline_cache=False,function_region=None,persistence='local_persistence')->None:
  '''Initializes the firebase class for client side environments'''
  anvil.js.report_all_exceptions(True)

  #Check credentials input value
  if not isinstance(config,dict):
    raise ValueError('Credentials must be of type dict')

  #initialize application
  global proxy_firebase
  global app
  proxy_firebase = anvil.js.import_from("https://www.gstatic.com/firebasejs/10.4.0/firebase-app.js")
  app = anvil.js.await_promise(proxy_firebase.initializeApp(config))
  #Initialize sub modules
  authentication.init(app,persistence)
  firestore.init(app,database=database,enable_offline_cache=enable_offline_cache)
  storage.init(app)
  functions.init(app,region=function_region)
