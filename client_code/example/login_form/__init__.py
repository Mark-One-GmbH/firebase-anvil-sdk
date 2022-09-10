from ._anvil_designer import login_formTemplate
from anvil import *

class login_form(login_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
