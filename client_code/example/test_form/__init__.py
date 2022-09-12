from ._anvil_designer import test_formTemplate
from anvil import *
from ...firebase_client import firestore as fs
from ...firebase_client import authentication as auth
from datetime import datetime

class test_form(test_formTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def add_doc_btn_click(self, **event_args):
    collection = fs.collection(fs.db,'test_collection')
    fs.add_doc(collection,{'key':'some_value','key2':'value2'})
    
  def set_doc_btn_click(self, **event_args):
    doc_ref = fs.doc(fs.db,'test_collection','some_uid')
    fs.set_doc(doc_ref,{'key':'some_value'})
    
  def update_doc_click(self, **event_args):
    doc_ref = fs.doc(fs.db,'test_collection','some_uid')
    fs.update_doc(doc_ref,{'key':'new_value'})
    
  def get_doc_btn_click(self, **event_args):
    doc_ref = fs.doc(fs.db,'test_collection','some_uid')
    doc_uid,doc_data = fs.get_doc(doc_ref)
    print(doc_uid,doc_data)

  def get_query_btn_click(self, **event_args):
    test_collection = fs.collection(fs.db,'test_collection')
    q = fs.query(test_collection,[fs.where('key','==','some_value'),fs.where('key2','==','value2')])
    documents = fs.get_docs(q)
    print(documents)

  def set_listener_btn_click(self, **event_args):
    test_collection = fs.collection(fs.db,'test_collection')
    q = fs.query(test_collection,fs.where('key','==','some_value'))
    listener = fs.listen_to_docs(q,self.listener_changed)

  def listener_changed(self,data):
    Notification('new data arrived',timeout=5).show()

  def batch_btn_click(self, **event_args):
    batch = fs.write_batch()
    doc_ref1 = fs.doc(fs.db,'test_collection','uid1')
    doc_ref2 = fs.doc(fs.db,'test_collection','uid2')
    batch.set(doc_ref2,{'batch_key':'value'})
    batch.set(doc_ref2,{'batch_key':'value'})
    batch.commit()

  def sign_in_btn_click(self, **event_args):
    start = datetime.now()
    user = auth.sign_in_with_email('mark.breuss@markone.at','1234567')
    print(user,'took ',datetime.now()-start)
    
  def sign_up_btn_click(self, **event_args):
    user = auth.signup_with_email('mark.breuss@markone.at','1234567')
    print(user)

  def get_user_btn_click(self, **event_args):
    start = datetime.now()
    user = auth.get_user()
    print(user,'took ',datetime.now()-start)

 










    

  



