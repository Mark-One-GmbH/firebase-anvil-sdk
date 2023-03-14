import anvil.js
from . import utility
from ..firestore import server_timestamp 

class Batch:
  def __init__(self,proxy_batch):
    self.proxy_batch = proxy_batch
    
  def add(self,doc_dict):
    doc_dict['update_timestamp'] = server_timestamp()
    return self.proxy_batch.add(utility.to_proxy(doc_dict))

  def set(self,doc_ref,doc_dict,merge=False):
    doc_dict['update_timestamp'] = server_timestamp()
    self.proxy_batch.set(doc_ref, utility.to_proxy(doc_dict),{'merge':merge})

  def update(self,doc_ref,doc_dict):
    doc_dict['update_timestamp'] = server_timestamp()
    self.proxy_batch.update(doc_ref,utility.to_proxy(doc_dict))

  def delete(self,doc_ref):
    self.proxy_batch.delete(doc_ref)

  def commit(self,blocking=True):
    '''Executes the batch'''
    if blocking:
      self.proxy_batch.commit()
    else:
      anvil.js.call('batch_commit',self.proxy_batch)