
from ..firebase_core import firestore as fs

"""Read Data from Firestore"""
def get_multiple_documents():
  query = fs.db.collection('test').where('name','==','hello')
  docs = fs.get_docs(query)
  print(docs)
  

def get_single_document():
  doc_ref = fs.db.collection('test').doc('doc_uid')
  doc = fs.get_doc(doc_ref)
  print(doc.data)
  
  
  
  """Write Data"""
  def set_document():
    doc_ref = fs.db.collection('test').doc('doc_uid')
    doc = fs.get_doc(doc_ref)
    print(doc.data)
  
  def get_single_document():
    doc_ref = fs.db.collection('test').doc('doc_uid')
    doc = fs.get_doc(doc_ref)
    print(doc.data)