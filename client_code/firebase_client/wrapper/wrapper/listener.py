

class Listener:
  def __init__(self,doc_ref, callback):
    self.doc_ref = doc_ref
    self.callback = callback
    self.proxy_listener = None


  def _listener_callback(self,data):
    print('newdata',data)
    self.callback(data)

  
  def start(self):
    import anvil.js
    self.proxy_listener = anvil.js.call('new_listener')
    self.proxy_listener.start(self.doc_ref,self._listener_callback)

  def stop(self):
    self.proxy_listener.unsubscribe()

