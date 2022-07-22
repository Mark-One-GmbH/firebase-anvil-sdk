"""
Exporting the Firebase class as a singelton instance
"""


class Firebase:
  def __init__(self):    
    #javascript modules
    self._initializeApp = None
    self._getFirestore = None
    self._getAuth = None
    self._app = None
    #Children classes
    from . import firestore
    from . import authentication
    self.firestore = firestore.Firestore()    
    self.auth = authentication.Authentication()
    
    
  def initialize_app(self,credentials_dict:dict)->None:
    '''Initializes the firebase class'''
    
    #Make sure init app is only called once!
    if self._initializeApp != None or self._getFirestore != None or self._getAuth != None:
      raise ValueError('Firebase can only be intialized once')
    
    #Check credentials input value
    if not isinstance(credentials_dict,dict):
      raise ValueError('Credentials must be of type dict')

    #Get Firestore javascript modules
    import anvil.js
    self._initializeApp = anvil.js.import_from("https://www.gstatic.com/firebasejs/9.9.0/firebase-app.js")
    self._getFirestore = anvil.js.import_from("https://www.gstatic.com/firebasejs/9.9.0/firebase-firestore.js")
    self._getAuth = anvil.js.import_from("https://www.gstatic.com/firebasejs/9.9.0/firebase-auth.js")
  
    #initialize application
    self._app = self._initializeApp.initializeApp(credentials_dict)
  
    #Initializse children classes
    self.firestore.init_app(self._getFirestore,self._getFirestore.getFirestore(self._app))
    


"""Export the singelton instance"""
firebase = Firebase()



