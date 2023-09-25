import anvil.js
from .helper import utility
from datetime import datetime, timedelta
import time

proxy_fs = None
functions = None #initialized with init() -> late


def init(app,region=None):
  '''initalizes the firestore module'''
  global functions
  global proxy_fs
  proxy_fs = anvil.js.import_from("https://www.gstatic.com/firebasejs/10.4.0/firebase-functions.js")
  if region:
    functions = proxy_fs.getFunctions(app,region)
  else:
    functions = proxy_fs.getFunctions(app)

def call(func_name,parameters={}):
  '''calls a cloud function v1'''
  cloud_function = proxy_fs.httpsCallable(functions, func_name);
  result = cloud_function(utility.to_proxy(parameters))
  return utility.from_proxy(result)


#on_error_ret = None
#on_result_ret = None
on_result_dict = {}
def call_v2(function_url,parameters={},callback_func=None,error_callback_func=None,timeout=60):
  '''calls a cloud function v2 - func_url must be the complete function url!'''
  cloud_function = proxy_fs.httpsCallableFromURL(functions, function_url)
  
  if callback_func:
    anvil.js.call('callV2Async',cloud_function,utility.to_proxy(parameters),_call_v2_callback,callback_func,error_callback_func,'')
  else:
    start_time = datetime.now()

    delete_keys = [res_uid for res_uid,result_dict in on_result_dict.items() if (result_dict.get('timestamp') + timedelta(seconds=60)) < start_time]
    for delete_key in delete_keys:
      on_result_dict.pop(delete_key)

    new_uid = utility.get_uid()
    on_result_dict[new_uid] = {'timestamp':start_time}
    
    def on_result(res, uid):
      global on_result_dict
      on_result_dict[uid]['result'] = res
      
    def on_error(err):
      global on_result_dict
      on_result_dict[uid]['error'] = res

    #Call Function
    anvil.js.call('callV2Async',cloud_function,utility.to_proxy(parameters),_call_v2_callback,on_result,on_error,new_uid)

    #Await Result
    while on_result_dict[new_uid].get('error') is None and on_result_dict[new_uid].get('result') is None and (datetime.now()-start_time).total_seconds() < timeout:
      time.sleep(0.05)

    #return result
    if (datetime.now()-start_time).total_seconds() < timeout:
      return utility.from_proxy(on_result_dict[new_uid].get('result'))
    else:
      raise ValueError('timeout')



def _call_v2_callback(result,callback_func,uid):
  if uid: return callback_func(utility.from_proxy(result), uid)
  return callback_func(utility.from_proxy(result))



   
