
from . import utility

class Batch:
  def __init__(self,proxy_batch):
    self.proxy_batch = proxy_batch
    
  def add(self,doc_dict):
    return self.proxy_batch.add(utility.to_proxy(doc_dict))

  def set(self,doc_ref,doc_dict,merge=False):
    self.proxy_batch.set(doc_ref, utility.to_proxy(doc_dict),{'merge':merge})

  def update(self,doc_ref,doc_dict):
    self.proxy_batch.update(doc_ref,utility.to_proxy(doc_dict))

  def delete(self,doc_ref):
    self.proxy_batch.delete(doc_ref)

  def commit(self):
    '''Executes the batch'''
    self.proxy_batch.commit()