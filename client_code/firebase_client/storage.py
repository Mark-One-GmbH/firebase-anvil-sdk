import anvil.js
proxy_storage = None
storage = None #initialized with init() -> late


def init(app):
  '''initalizes the firestore module'''
  global storage
  global proxy_storage
  proxy_storage = anvil.js.import_from("https://www.gstatic.com/firebasejs/10.4.0/firebase-storage.js")
  storage = proxy_storage.getStorage(app)

def ref(path):
  '''creates a storage reference e.g: ref("images/image1.png") '''
  #Create a child reference
  return proxy_storage.ref(storage, path)

def upload_media(storage_ref,media_obj):
  metadata = {'contentType': media_obj.content_type}
  proxy_storage.uploadBytes(storage_ref, media_obj.get_bytes(),metadata)

def get_download_url(storage_ref):
  '''Gets a dwonloadable media url for the image, can be used as source of an image compoent'''
  return proxy_storage.getDownloadURL(storage_ref)

def delete_file(storage_ref):
  return proxy_storage.deleteObject(storage_ref)

def list_files():
  raise ValueError('Not yet implemented')
  '''
  https://firebase.google.com/docs/storage/web/list-files?authuser=0
  '''
  



