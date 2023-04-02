import anvil.js
from .helper import utility
from datetime import datetime

proxy_fs = None
functions = None #initialized with init() -> late


def init(app,region=None):
  '''initalizes the firestore module'''
  global functions
  global proxy_fs
  proxy_fs = anvil.js.import_from("https://www.gstatic.com/firebasejs/9.12.1/firebase-functions.js")
  if region:
    functions = proxy_fs.getFunctions(app,region)
  else:
    functions = proxy_fs.getFunctions(app)

def call(func_name,parameters={}):
  '''calls a cloud function v1'''
  cloud_function = proxy_fs.httpsCallable(functions, func_name);
  result = cloud_function(utility.to_proxy(parameters))
  return utility.from_proxy(result)

def call_v2(function_url,parameters={},callback_func=None):
  '''calls a cloud function v2 - func_url must be the complete function url!'''
  cloud_function = proxy_fs.httpsCallableFromURL(functions, function_url)
  
  if callback_func:
    anvil.js.call('callV2Async',cloud_function,utility.to_proxy(parameters),_call_v2_callback,callback_func)
  else:
    result = cloud_function(utility.to_proxy(parameters))
    return utility.from_proxy(result.data)


def _call_v2_callback(result,callback_func):
  return callback_func(utility.from_proxy(result))


   