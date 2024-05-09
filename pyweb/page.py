from os import path, mkdir
from .element import Element

class Page:
  """
  Page class -- base level requirement in making websites using PyWeb.
  """
  def __init__(self, from_page=None) -> None:
    """
    Optional arguments:
      (1) from_page -- Page object instance
    """
    self.head = from_page.head if from_page else Element("head")
    self.body = from_page.body if from_page else Element("body")

  def init(self) -> tuple:
    """
    Returns:
      Tuple -- includes page instance as well as the head and body elements
    """
    return (self, self.head, self.body)

  def __str__(self) -> str:
    """
    Returns:
      String -- represents a valid HTML page
    """
    start = "<!DOCTYPE html>\n<html>"
    end = "</html>"
    return f"{start}\n{self.head}\n{self.body}\n{end}"
  
  def export(self, name, ext="html") -> None:
    """
      Required arguments:
        (1) name -- name of the file being exported
      Optional arguments:
        (1) ext -- extension of the file, defaults to HTML
    """
    if not path.exists("output"):
      mkdir("output")
    
    with open(f"output/{name}.{ext}", "w") as f:
      f.write(str(self))

  def set_title(self, title: str) -> None:
    """
    Required arguments:
      (1) title -- string representing the title of the document
    """
    title_element = Element("title", [title])
    title_element.inline = True
    self.head.add(title_element)
