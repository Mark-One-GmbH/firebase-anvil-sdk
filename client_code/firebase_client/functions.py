import anvil.js
from .helper import utility
from datetime import datetime

proxy_fs = anvil.js.import_from("https://www.gstatic.com/firebasejs/9.12.1/firebase-functions.js")
functions = None #initialized with init() -> late


def init(app,region=None):
  '''initalizes the firestore module'''
  global functions
  if region:
    functions = proxy_fs.getFunctions(app,region)
  else:
    functions = proxy_fs.getFunctions(app)

def call(func_name,parameters={}):
  cloud_function = proxy_fs.httpsCallable(functions, func_name);
  result = cloud_function(parameters)
  return result