


class Listener:
  def __init__(self,callback):
    self._unsubscribe = None
    self._callback = callback

  def _proxy_callback(self,data):
    #TODO convert proxy dict to 
    from . import utility
    self._callback(utility.from_proxy(data))

  def unsubscribe(self):
    '''removes the firestore listener'''
    self._unsubscribe()
    
