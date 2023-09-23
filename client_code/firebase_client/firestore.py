import anvil.js
from .helper import utility
from datetime import datetime

proxy_fs = None
db = None #initialized with init() -> late


def init(app,enable_offline_cache=False):
  '''initalizes the firestore module'''
  global db
  global proxy_fs
  proxy_fs = anvil.js.import_from("https://www.gstatic.com/firebasejs/10.4.0/firebase-firestore.js")
  db = proxy_fs.getFirestore(app)

  #TODO configure cache size!
  #Offline Caching
  if enable_offline_cache:
    try:
      anvil.js.call('enableMultiTabIndexedDbPersistence',proxy_fs,db)
    except Exception as e:
      print('Error enabeling offline persistance',e)
    
def disable_network():
  '''forces all subsequent queries to the offline cache'''
  anvil.js.await_promise(proxy_fs.disableNetwork(db))

def enable_network():
  '''reverts disable_network'''
  anvil.js.await_promise(proxy_fs.enableNetwork(db))


'''Helper Methods'''
def collection(db,collection_name):
  return proxy_fs.collection(db,collection_name)

def doc(db,collection_name,doc_uid=None):
  if doc_uid and doc_uid != 'new':
    return proxy_fs.doc(db, str(collection_name), str(doc_uid))
  else:
    return proxy_fs.doc(collection(db,collection_name))

def document_id():
  return proxy_fs.documentId()

def where(key,operator,value):
  if isinstance(value,datetime): value = utility.to_proxy(value)
  return proxy_fs.where(key,operator,value)

def order_by(attribute,sort_by='asc'):
  '''sort_by asc, desc'''
  return proxy_fs.orderBy(attribute,sort_by)

def limit(amount=100):
  return proxy_fs.limit(amount)

def query(collection,where):
  if not isinstance(where,list): where = [where]
  return proxy_fs.query(collection,*where)

def increment(number):
  return proxy_fs.increment(number)
  
def delete_field():
  return proxy_fs.deleteField()

def server_timestamp():
  return proxy_fs.serverTimestamp()
  

'''Data Manipulation'''
def add_doc(collection,doc_data,blocking=True):
  doc_data['update_timestamp'] = server_timestamp()
  if blocking:
    doc = proxy_fs.addDoc(collection,utility.to_proxy(doc_data))
    return doc.id
  else:
    anvil.js.call('addDoc',proxy_fs,collection,utility.to_proxy(doc_data))

def set_doc(doc_ref,doc_data,merge=False,blocking=True):
  '''Set a document'''
  doc_data['update_timestamp'] = server_timestamp()
  if blocking:
    return proxy_fs.setDoc(doc_ref,utility.to_proxy(doc_data),{'merge':merge})
  else:
    anvil.js.call('setDoc',proxy_fs,doc_ref,utility.to_proxy(doc_data),merge)

def update_doc(doc_ref,update_dict,blocking=True):
  update_dict['update_timestamp'] = server_timestamp()
  if blocking:
    return proxy_fs.updateDoc(doc_ref,utility.to_proxy(update_dict))
  else:
    anvil.js.call('updateDoc',proxy_fs,doc_ref,utility.to_proxy(update_dict))

def delete_doc(doc_ref,blocking=True):
  if blocking:
    return proxy_fs.deleteDoc(doc_ref)
  else:
    anvil.js.call('deleteDoc',proxy_fs,doc_ref)

  
def get_doc(doc_ref)->tuple:
  '''Returns uid,data or None,Error '''
  doc_snap = proxy_fs.getDoc(doc_ref)
  if doc_snap.exists():
    return doc_snap.id,utility.from_proxy(doc_snap.data())
  else:
    return None, None

def get_doc_from_cache(doc_ref):
  '''Get Doc from cache - raises an error if not present'''
  doc_snap = proxy_fs.getDocFromCache(doc_ref)
  return doc_snap.id,utility.from_proxy(doc_snap.data())


def get_docs(query,callback_func=None):
  '''
  ececutes a query and returns a list of uid,data tuples 
  '''
  if callback_func:
    anvil.js.call('getDocsAsync',proxy_fs,query,_get_docs_callback,callback_func)
  else:
    querySnapshot = proxy_fs.getDocs(query)
    return _convert_snapshot(querySnapshot)

def _get_docs_callback(querySnapshot,callback_func):
  return callback_func(_convert_snapshot(querySnapshot))

def get_all(doc_refs):
  querySnapshot = proxy_fs.getDocs(query)
  return _convert_snapshot(querySnapshot)
  
def _convert_snapshot(querySnapshot):
  ret_list = []
  def convert_docs(doc):
    ret_list.append((doc.id,utility.from_proxy(doc.data())))
  
  querySnapshot.forEach(convert_docs)
  return ret_list

def get_docs_from_cache(query):
  '''get documents, forcing the sdk to fetch from the offline chache'''
  querySnapshot = proxy_fs.getDocsFromCache(query)
  
  ret_list = []
  def convert_docs(doc):
    ret_list.append((doc.id,utility.from_proxy(doc.data())))
    
  querySnapshot.forEach(convert_docs)
  return ret_list

def get_collection_group(collection_id):
  return proxy_fs.collectionGroup(db,collection_id)
  

def arrayUnion(element):
  if isinstance(element,list):
    return proxy_fs.arrayUnion(*utility.to_proxy(element))
  else:
    return proxy_fs.arrayUnion(utility.to_proxy(element))

def arrayRemove(element):
  if isinstance(element,list):
    return proxy_fs.arrayRemove(*utility.to_proxy(element))
  else:
    return proxy_fs.arrayRemove(utility.to_proxy(element))


@anvil.js.report_exceptions
def listen_to_docs(query,callback):
  from .helper.listener import DocsListener
  l = DocsListener(callback)
  l.unsubscribe = proxy_fs.onSnapshot(query,l._proxy_callback)
  return l
  
@anvil.js.report_exceptions
def listen_to_doc(doc_ref,callback):
  from .helper.listener import DocListener
  l = DocListener(callback)
  l.unsubscribe = proxy_fs.onSnapshot(doc_ref,l._proxy_callback)
  return l
  

def write_batch():
  from .helper.batch import Batch
  return Batch(proxy_fs.writeBatch(db))

def run_transaction(function):
  '''Takes in a function which must be run as a transaction'''
  return anvil.js.await_promise(proxy_fs.runTransaction(db,function))


  





