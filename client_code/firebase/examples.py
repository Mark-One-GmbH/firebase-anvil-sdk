
from ..firebase import firestore as fs

"""Read Data from Firestore"""
def get_multiple_documents(use_cache=False):
  query = fs.db.collection('test').where('name','==','hello')
  docs = fs.get_docs(query,use_cache=use_cache)
  return docs
  

def get_single_document():
  doc_ref = fs.db.collection('test').doc('doc_uid')
  doc = fs.get_doc(doc_ref)
  return doc
  
  
  
  """Write Data"""
  def set_document():
    doc_ref = fs.db.collection('test').doc('doc_uid')
    doc = fs.get_doc(doc_ref)
    print(doc.data)
  
  def get_single_document():
    doc_ref = fs.db.collection('test').doc('doc_uid')
    doc = fs.get_doc(doc_ref)
    print(doc.data)