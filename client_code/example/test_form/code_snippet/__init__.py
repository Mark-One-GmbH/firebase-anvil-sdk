from ._anvil_designer import code_snippetTemplate
from anvil import *

class code_snippet(code_snippetTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
