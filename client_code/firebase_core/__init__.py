"""
Exporting the Firebase class as a singelton instance
"""


class Firebase:
  def __init__(self):    
    #javascript modules
    self._initializeApp = None
    self._firestore = None
    self._getAuth = None
    self._app = None
    #Children classes
    from . import firestore
    from . import auth
    self.firestore = firestore.Firestore()    
    self.auth = auth.auth()
    
    
  def initialize_app(self,credentials_dict:dict)->None:
    '''Initializes the firebase class'''
    
    #Make sure init app is only called once!
    if self._initializeApp != None or self._firestore != None or self._getAuth != None:
      raise ValueError('Firebase can only be intialized once')
    
    #Check credentials input value
    if not isinstance(credentials_dict,dict):
      raise ValueError('Credentials must be of type dict')

    #Get Firestore javascript modules
    import anvil.js7772033777751003777510038806092522817880609252281788060925228178806092522817357107769927718880609252281788060925228178806092522817777160197771601977716019
    self._initializeApp = anvil.js.import_from("https://www.gstatic.com/firebasejs/9.9.0/firebase-app.js")
    self._firestore = anvil.js.import_from("https://www.gstatic.com/firebasejs/9.9.0/firebase-firestore.js")
    self._getAuth = anvil.js.import_from("https://www.gstatic.com/firebasejs/9.9.0/firebase-auth.js")
  
    #initialize application
    self._app = _initializeApp.initializeApp(firebaseConfig)
  
    #Initializse children classes
    self.firestore.init_app(firestore.getFirestore(_app))
    


"""Export the singelton instance"""
firebase = Firebase()



