

class Firestore:
  def __init__(self):
    self._db = None
    self._fs_proxy = None
    
  def init_app(self,firestore_proxy,db):
    self._fs_proxy = firestore_proxy
    self._db = db #Root level database
    #API Modules
    self.doc = self._fs_proxy.doc
    self.collection = self._fs_proxy.collection
    self.setDoc = self._fs_proxy.setDoc
    self.getDocs = self._fs_proxy.doc
    self.orderBy = self._fs_proxy.orderBy
    self.limit = self._fs_proxy.limit
    self.onSnapshot = self._fs_proxy.onSnapshot
    self.enableIndexedDbPersistence = self._fs_proxy.enableIndexedDbPersistence
    self.CACHE_SIZE_UNLIMITED = self._fs_proxy.CACHE_SIZE_UNLIMITED
    self.disableNetwork = self._fs_proxy.disableNetwork
    self.enableNetwork = self._fs_proxy.enableNetwork
    self.startAt = self._fs_proxy.startAt
    self.endAt = self._fs_proxy.endAt
    #db refs
    self.db_ref = self.collection(self._db, "cities")
    
    
  def get_ref(self,collection):
     return self.collection(self._db, collection)
    
  '''
  This is a wrapper around the official Web9 Firestore SDK
  https://firebase.google.com/docs/reference/js/firestore_?authuser=0
  '''
  
  def getDocs(self,query):
    '''Reads the document referred to by this DocumentReference'''
    return self._fs_proxy.getDocs(query)
  
  def query(self,reference,where):
    '''Creates a new immutable instance of Query that is extended to also include additional query constraints'''
    print(reference,where)
    return self._fs_proxy.query(reference,where)
  
  def where(self,attribute,operation,value):
    return self._fs_proxy.where(attribute,operation,value)

# app = initializeApp.initializeApp(firebaseConfig)
# db = firestore.getFirestore(app)
# auth = getAuth.getAuth(app)


# query = firestore.query(firestore.collection(db, "global_settings")) #, where("capital", "==", true))
# querySnapshot = firestore.getDocs(query)

# for doc in querySnapshot:
#   print(doc)
