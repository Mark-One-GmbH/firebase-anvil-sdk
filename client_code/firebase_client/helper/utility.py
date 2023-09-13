'''
Utility methods to work with proxy obj, conversion and general javascript
'''
import anvil.js
from anvil.js.window import document 
from anvil.js.window import Date
proxy_type = type(document)
from datetime import datetime


def from_proxy(proxy_obj):
  '''
    Input: Firestore proxy dict
    Output: Python Dictionary
    
    Supports: Arrays, Dicts, Firestore Timestamps
    TODO: Geopoint, References
  '''
  if isinstance(proxy_obj, proxy_type):
    '''Proxy Type Timestamp, Dic'''
    if getattr(proxy_obj, "toMillis", None):
      return datetime.fromtimestamp(proxy_obj.toMillis()/1000.0)
    else:
      #can keys be of type proxy obj?
      return dict([(k,from_proxy(v)) for k,v in dict(proxy_obj).items()])
  elif isinstance(proxy_obj,list):
    '''Proxy Type Array'''
    return [from_proxy(i) for i in proxy_obj]
  else:
    '''No proxy obj'''
    return proxy_obj



def to_proxy(obj):
  '''
  Input: dict, list, datetime
  Output: a Value 
  
  '''
  if isinstance(obj,datetime):
    return anvil.js.new(Date,datetime.timestamp(obj)* 1000)
  elif isinstance(obj,dict):
      return dict([(k,to_proxy(v)) for k,v in obj.items()])
  elif isinstance(obj,list):
    return [to_proxy(i) for i in obj]
  else:
    return obj
  


def get_uid():
  import random
  hexdigits = "0123456789ABCDEF"
  random_digits = "".join([ hexdigits[random.randint(0,0xF)] for _ in range(32) ])
  return random_digits