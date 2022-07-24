import anvil.js

'''
root level access to the firestore database, is iniitlaized from firebase core
'''
db = None

'''Helper Functions'''
def get_docs(query):
  '''
  Executes a firestore query
  Returns: [(doc_uid,doc_dict),...]
  '''
  
  documents = []
  
  #execute query
  querySnapshot = query.get()  
  
  #serialize query to list of 
  def get_docs(doc): documents.append(Document(doc.id,proxy_to_dict(doc.data())))
  querySnapshot.forEach(get_docs)
  
  return documents

def get_doc(doc_ref):
  '''
  Executes a firestore query
  Returns a Document
  '''
    
  #execute query
  try:
    doc = doc_ref.get()
  except Exception as e:
    return Document(exists = False)
  
  if doc.exists:
    return Document(doc.id,proxy_to_dict(doc.data()))
  else:
    return Document(exists = False)
  


"""Helper Functions"""
def proxy_to_dict(proxy_obj):
  '''Takes in a proxy obj and serializes it to a python dict'''
  ret = dict(proxy_obj) #TODO include, datetime etc
  return ret

def dict_to_proxy(dict_obj):
  #TODO
  return dict_obj

"""Wrapper Classes"""

class Document:
  def __init__(self,uid='',data={},exists=True):
    self.id = uid
    self.data = data
    self.exists = True
    
  def __repr__(self):
    return f"Firestore Document {self.id}"