

class Firestore:
  def __init__(self):
    self.db = None
    
  def init_app(self,db):
    self.db = db
   




# app = initializeApp.initializeApp(firebaseConfig)
# db = firestore.getFirestore(app)
# auth = getAuth.getAuth(app)


# query = firestore.query(firestore.collection(db, "global_settings")) #, where("capital", "==", true))
# querySnapshot = firestore.getDocs(query)

# for doc in querySnapshot:
#   print(doc)
