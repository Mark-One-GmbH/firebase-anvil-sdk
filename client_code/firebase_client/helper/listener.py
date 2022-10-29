


class DocsListener:
  def __init__(self,callback):
    self._unsubscribe = None
    self._callback = callback

  def _proxy_callback(self,snapshot):
    #TODO convert proxy dict to 
    from . import utility
    docs = []
    def add_doc(doc):
      docs.append((doc.id,utility.from_proxy(doc.data())))
      
    snapshot.forEach(add_doc)
    self._callback(docs)

  def unsubscribe(self):
    '''removes the firestore listener'''
    self._unsubscribe()
    
class DocListener:
  def __init__(self,callback):
    self._unsubscribe = None
    self._callback = callback

  def _proxy_callback(self,snapshot):
    #TODO convert proxy dict to 
    from . import utility
    self._callback((doc.id,utility.from_proxy(doc.data())))

  def unsubscribe(self):
    '''removes the firestore listener'''
    self._unsubscribe()