import anvil.js
proxy_fs = anvil.js.import_from("https://www.gstatic.com/firebasejs/9.9.4/firebase-firestore.js")
db = None #initialized with init() -> late


def init(app):
  '''initalizes the firestore module'''
  global db
  db = proxy_fs.getFirestore(app);


def collection(db,collection_name):
  return proxy_fs.collection(db,collection_name)

def add_doc(doc_ref,doc_data):
  return proxy_fs.addDoc(doc_ref,doc_data)




