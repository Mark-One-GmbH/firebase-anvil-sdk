from ._anvil_designer import test_formTemplate
from anvil import *
from ...firebase_client import firestore as fs
from ...firebase_client import authentication as auth
from ...firebase_client import storage,analytics
from datetime import datetime

class test_form(test_formTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    #test conversion
    doc_ref = fs.doc(fs.db,'test','conversion_test')
    doc_uid,doc_data = fs.get_doc(doc_ref)
    print(doc_data)
    doc_ref2 = fs.doc(fs.db,'test_collection','conversion_test_in')
    fs.set_doc(doc_ref2,{
      'now':datetime.now()
    })

    

  def add_doc_btn_click(self, **event_args):
    collection = fs.collection(fs.db,'test_collection')
    fs.add_doc(collection,{'key':'some_value','key2':'value2'})
    
  def set_doc_btn_click(self, **event_args):
    doc_ref = fs.doc(fs.db,'test_collection','some_uid')
    ret = fs.set_doc(doc_ref,{'key':'some_value'})

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

  def sign_in_token_btn_click(self, **event_args):
    start = datetime.now()
    import anvil.server
    fs_token = anvil.server.call('fs_server_get_auth_token')
    user = auth.sign_in_with_token(fs_token)
    print(user,'token took ',datetime.now()-start)

  def logout_btn_click(self, **event_args):
    auth.logout()

  def transaction_btn_click(self, **event_args):
    transaction = fs.run_transaction(self.transaction_function)

  def transaction_function(self,transaction):
    #Define two document references to work with
    doc_ref1 = fs.doc(fs.db,'test_collection','uid1')
    doc_ref2 = fs.doc(fs.db,'test_collection','uid2')
    #read from doc 1
    doc1 = transaction.get(doc_ref1)
    #write to doc 2
    transaction.update(doc_ref2, { 'new_value': 1234 })

  def upload_media_btn_click(self, **event_args):
    import anvil
    file = anvil.URLMedia("https://anvil.works/ide/img/banner-100.png")
    ref = storage.ref('images/test1.png')
    storage.upload_media(ref,file)
    

  def download_media_btn_click(self, **event_args):
    ref = storage.ref('images/test1.png')
    url = storage.get_download_url(ref)
    print(url)

  def log_event_btn_click(self, **event_args):
    analytics.log_event('testevent')









 










    

  



