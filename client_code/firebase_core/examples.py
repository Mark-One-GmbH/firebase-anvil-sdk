


def get_multiple_documents():
  #get the firestore modules
  from .. import firebase_core
  fs = firebase_core.firestore
  #form query
  query = fs.db.collection('test').where('name','==','hello')
  #execute query
  docs = fs.get_docs(query)
  print(docs)
  

def get_single_document():
  #get the firestore modules
  from .. import firebase_core
  fs = firebase_core.firestore
  #get doc reference
  doc_ref = fs.db.collection('test').doc('doc_uid')
  #execute query
  doc = fs.get_doc(doc_ref)
  print(doc.data)