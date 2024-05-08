from .element import Element

"""
Info:
  This file contains helpful HTML elements created using the Element class
"""

class Link(Element):
  """
  Info:
    Sets up the HTML <a> element
  """
  def __init__(self, url, text, attrs=dict()) -> None:
    """
    Required arguments:
      (1) url -- url of page to direct the user to
      (2) text -- placeholder text inside the href element
    Optional arguments:
      (1) attrs -- dictionary of all other attributes
    Returns:
      None
    """
    self.url = url
    super().__init__("a", [text], {"href": url} | attrs)
  
  def set_attr(self, attrs) -> None:
    """
    Info:
      Prevents user from overwriting the "href" attribute.
      Refer to Element's comment for more info.
    """
    return super().set_attr({"href": self.url} | attrs)
  

class Abbr(Element):
  """
  Info:
    Sets up the HTML <abbr> element
  """
  def __init__(self, text, title) -> None:
    super().__init__("abbr", [text], {"title": title})
    self.inline = True