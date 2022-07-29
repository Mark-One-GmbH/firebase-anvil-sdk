from ._anvil_designer import markone_core_testTemplate
from anvil import *

from markone_core import data

class markone_core_test(markone_core_testTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
