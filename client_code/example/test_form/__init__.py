from ._anvil_designer import test_formTemplate
from anvil import *
from ... import firebase_client

class test_form(test_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def add_doc_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass



