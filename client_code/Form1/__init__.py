from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def form_show(self, **event_args):
    # Any code you write here will run when the form opens.
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    from ..firebase import examples
    from datetime import datetime
    start = datetime.now()
    ret = examples.get_multiple_documents(True)
    print(datetime.now()-start)
    Notification(str(ret),timeout=100).show()

