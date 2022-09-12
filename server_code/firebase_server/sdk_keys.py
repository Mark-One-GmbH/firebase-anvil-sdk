

def get_firestore_sdk_config():
  return {
    "type": "service_account",
    "project_id": "development-945bf",
    "private_key_id": "f0f7eef024be9d08719caabdd5c4d3b946541353",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQC+GgcWUoJcKkRG\nQMzRFonPeQro5U+8wR9xDErhtVc+BshbHDODVgvOxcVQrlbPv98GMotJKMSZTjbd\nrWDILf9TlGL1a2tlzrnwb+wwyvbpIBvaaHsKN2c5l/5wQbeikgFILAWcOAFjRp+F\n6G32srOcmC1IyEoLaacE20bArpoVamNM9iREn/JacX4FU8keuNZ+h+Sfmwn8RVfV\nKi3vacdKjgJzcgcBJNSsYTAY6jIaIp281EH0ug4SX55pt6iQTHNvq3bkUm28Yzme\nUU8FIUOEGklLfn+0xDGZV08tMSnn1nwjWR1OMu2rPvwP//dXLpatA5Sv75pWlT4/\noa9t9arHAgMBAAECggEASDHoSSDyov/mR+vqHOn7UlC8xO/5VUzenPc3JPrSdBrt\nUjSml5VBDLjtE5PyIhnTIC5n2VPjPfmHOq7Sl5NoaRxsbJnsApD86oQG5gzesnBg\nQ5T0TU/3ItdHaOh8TgA2/mrBgq9+T26NvLQlts/tCGZ+pCp0fFsWc/C2sQxeNg02\nrFxc1ZOtv9g5lCt7/GGAuW1O+Amcv5M3+6TIShXCR0oMyZFwk636zJhistTxOkhC\nwWjR95q1q8MsVEBf7V352FPaS65QiG+oh8ONKbMUlyVxOCvr3y8lna5pzdRa8VnS\nxZq0CWBMWcMkbVlV7+a5Vh2CG6x2gyFR/totWTLJGQKBgQDgt/5vHHmBeydXbbqE\nDe7gcipFRYNWVxUn0uao4x4EBaYe7VAJRTYWgKQfOmErqZAkyhH5GjfVc6zCaotv\n7KD/czirCzIqhD42Vz+c0qlfWwqtgJyOemRsknzr7kF8PdVvvpyQK3RuD6dlEegN\nhMPd8KnsSCU1vxsIMJSf0E3s7QKBgQDYkG5m+eFENNs8bLJQVGwk+4cZuizh03QZ\nGqSog65jZ/9Ebd3WOcMA1i4x55R+OWz4c+uhDH10wV+OBuu/s/58selKgrr82Or7\nPXtnFA0U9qvQMRG6pBHGhRv+thLRCh2kLLnmu71xHVnftQloWpJe1JMXOKqEB2XA\nbhwBBuL0AwKBgQC3ufcORQuar2P0+UO7X+DkJLMmu7SrzLsBOk9X2Yja5Pty4bfE\nPJACSd7loUd8+T9etM+JCMSJge/HbHDga2keMcgtIBQ96q0qpJ7fyuSrj7XlMPfP\nDYY5tnLoOn3T5IIywHck8EJbEfVcjw1YsCmrtW5YPowdq0egpId/OkHb6QKBgQDQ\nHIOru6ephu3DtGTq4yYFqB0dMRcecLiZw0vGkLyN1IuvM7FBw8JMVIaR+IxvfDnm\nzGb8HeeVwppT/vyf/ZWqOMIKk3SjtMSjaWLkHJWxtpZHfFAgPrjCQHo1nLyaW5E+\niqifPX0AbYdHfk6rFJaiQL+VSiQ6um0ire2FYxvIBwKBgQC6/KwxUGzj63tXeqEd\nq/om4mg0pEWpdMOwNUo4VzrxdyTi6l1S550zRonlx/JWYdARmZTW53nKHiOM7S+e\nU+gRF4KLXJ3cGGVDOn2QYhtVugKqpNFK4PLQRMoEQz+xuwr5uWmHtYCW/+eaJnKF\nLoO+vzGKUF1M/jv9isVp3rFsIQ==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-2zg9p@development-945bf.iam.gserviceaccount.com",
    "client_id": "100517515740876744602",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-2zg9p%40development-945bf.iam.gserviceaccount.com"
  }
  
  from anvil import app
  if app.environment.name in ['prod','beta','prod-clocking','beta-clocking','beta-lager','prod-lager']:
   return anvil.secrets.get_secret('prod_firestore_sdk_config')
  else:
   return anvil.secrets.get_secret('qa_firestore_sdk_config')

def get_firestore_client_config():
  from anvil import app
  if app.environment.name in ['prod','beta','prod-clocking','beta-clocking','beta-lager','prod-lager']:
   return anvil.secrets.get_secret('prod_firestore_client_config')
  else:
   return anvil.secrets.get_secret('qa_firestore_client_config')

def get_bucket_id():
  return "development-945bf.appspot.com"

  
  from anvil import app
  if app.environment.name in ['prod','beta','prod-clocking','beta-clocking','beta-lager','prod-lager']:
   return anvil.secrets.get_secret('prod_bucket_id')
  else:
   return anvil.secrets.get_secret('qa_bucket_id')
  