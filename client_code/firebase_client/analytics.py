import anvil.js
proxy_analytics = anvil.js.import_from("https://www.gstatic.com/firebasejs/9.9.4/firebase-analytics.js")
analytics = None #initialized with init() -> late


def init(app):
  '''initalizes the firestore module'''
  global analytics
  analytics = proxy_analytics.getAnalytics(app)


def log_event(event_name):
  proxy_analytics.logEvent(analytics, str(event_name))

def set_user_properties(user_properties):
  proxy_analytics.setUserProperties(analytics, user_properties)
