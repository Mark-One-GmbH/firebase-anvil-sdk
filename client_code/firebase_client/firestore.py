import anvil.js

'''
root level access to the firestore database, is iniitlaized from firebase core
'''
db = None



'''
Main Database Functions

get_docs
get_doc

add_doc
add_docs #todo

add_listener


'''

def get_docs(query,force_cache=False):
  '''
  Executes a firestore query
  Returns: [(doc_uid,doc_dict),...]
  '''
  
  documents = []
  
  #execute query
  source_option = 'cache' if force_cache else 'default'
  querySnapshot = query.get({'source': source_option})  
  
  #serialize query to list of 
  def get_docs(doc): documents.append(Document(doc.id,proxy_to_dict(doc.data())))
  querySnapshot.forEach(get_docs)
  
  return documents


def get_doc(doc_ref,force_cache=False):
  '''
  Executes a firestore query
  Returns a Document
  '''
  
  try:
    #execute query
    source_option = 'cache' if force_cache else 'default' #default used database first, and if offline cache
    doc = doc_ref.get({'source': source_option})  
  except Exception as e:
    return Document(exists = False)
  
  if doc.exists:
    return Document(doc.id,proxy_to_dict(doc.data()))
  else:
    return Document(exists = False)

def add_doc(doc_ref,doc_data):
  try:
    doc = doc_ref.add(doc_data)  
  except Exception as e:
    print('error adding doc')

def add_docs(doc_tuples):
  pass
  



listeners = []
def add_listener(doc_ref,callback):
  from .wrapper.listener import Listener
  global listeners
  l =  Listener(doc_ref,callback)
  listeners.append(l)
  l.start()
  return l


  
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


'''
Subsequent queries will use persistence, if it was enabled successfully
Can only be set after initialization

You can use the methods below to disable network access for your Cloud Firestore client. 
While network access is disabled, all snapshot listeners and document requests retrieve results from the cache. 
Write operations are queued until network access is re-enabled.
'''
def enable_offline_persistance(unlimited_cache_size=True):
  try:
    import anvil.js
    fs_proxy = anvil.js.window.firebase.firestore
    if unlimited_cache_size: fs_proxy().settings({'cacheSizeBytes': fs_proxy.CACHE_SIZE_UNLIMITED})
    fs_proxy().enablePersistence()
  except Exception as e:
    print(f"Error enableing firestore offline persistance {e}")
  

def disable_network():
  import anvil.js
  anvil.js.window.firebase.firestore.disableNetwork()
  
def enable_network():
  import anvil.js
  anvil.js.window.firebase.firestore.enableNetwork()
