import anvil.js
from .helper import utility
from datetime import datetime
import time

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


on_error_ret = None
on_result_ret = None
def call_v2(function_url,parameters={},callback_func=None,error_callback_func=None,timeout=60):
  '''calls a cloud function v2 - func_url must be the complete function url!'''
  cloud_function = proxy_fs.httpsCallableFromURL(functions, function_url)
  
  if callback_func:
    anvil.js.call('callV2Async',cloud_function,utility.to_proxy(parameters),_call_v2_callback,callback_func,error_callback_func)
  else:
    start_time = datetime.now()
    global on_error_ret
    global on_result_ret
    
    on_error_ret = None
    on_result_ret = None
    def on_result(res):
      global on_result_ret
      on_result_ret = res
      
    def on_error(err):
      global on_error_ret
      on_error_ret = True

    #Call Function
    anvil.js.call('callV2Async',cloud_function,utility.to_proxy(parameters),_call_v2_callback,on_result,on_error)

    #Await Result
    while on_error_ret is None and on_result_ret is None and (datetime.now()-start_time).total_seconds() < timeout:
      time.sleep(0.05)

    #return result
    if (datetime.now()-start_time).total_seconds() < timeout:
      return utility.from_proxy(on_error_ret.data)
    else:
      raise ValueError('timeout')



def _call_v2_callback(result,callback_func):
  return callback_func(utility.from_proxy(result))



   