import os

def tabber(html) -> str:
  """
  Required argumetns:
    (1) html -- a string containing the content of an HTML file
  Returns:
    String -- a "properly" formatter string containing the original HTML file
  """
  lines = html.split("\n")
  level = 0
  output = ""
  for line in lines:
    if line.startswith("</"):
      level -= 1
      output += "\t" * level + line + "\n"
      if level < 0:
        level = 0
    elif line.startswith("<") and not line.startswith("<!"):
      output += "\t" * level + line + "\n"
      level += 1
    else:
      output += "\t" * level + line + "\n"
  return output

class Page:
  """
  Page class -- base level requirement in making websites using PyWeb.
  """
  def __init__(self, from_page=None) -> None:
    """
    Optional arguments:
      (1) from_page -- Page object instance
    Returns:
      None
    """
    self.head = from_page.head if from_page else Element("head")
    self.body = from_page.body if from_page else Element("body")

  def init(self) -> tuple:
    """
    Returns:
      Tuple -- includes page instance as well as the head and body elements
    """
    return (self, self.head, self.body)

  def __repr__(self) -> str:
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
      Returns:
        None
    """
    if not os.path.exists("output"):
      os.mkdir("output")
    
    with open(f"output/{name}.{ext}", "w") as f:
      f.write(tabber(str(self)))


class Element:
  """
  Element class -- provides base class for all HTML elements in PyWeb
  """
  def __init__(self, tag, children=None, attrs=dict()) -> None:
    """
    Required arguments:
      (1) tag -- string representation of the tag, e.g. "div"
    Optional arguments:
      (1) children  -- list of Elements to be initialized to this element's children list
      (2) attrs     -- dictionary of properties of the element to initialize with
    Returns:
      None
    """
    self.props = attrs
    self.tag = tag
    self.children = children if children != None else []

  def set_attr(self, attrs) -> None:
    """
    Required arguments:
      (1) attrs -- dictionary of attributes
    Returns:
      None
    """
    self.props = attrs

  def set_style(self, style) -> None:
    """
    Required arguments:
      (1) style -- dictionary of CSS rules
    Returns:
      None
    """
    self.props["style"] = "; ".join([f'{key}: {val}' for key, val in style.items()])

  def add(self, *elements) -> None:
    """
    Optional arguments:
      (1) elements -- list of elements to add as children
    Returns:
      None
    """
    for element in elements:
      self.children.append(element)

  def __get_attribute_string(self) -> str:
    """
    Returns:
      String -- HTML-formatted attributes
    """
    return " ".join([f"{attr}=\"{val}\"" for (attr, val) in self.props.items()])
  
  def __get_children_string(self) -> str:
    """
    Returns:
      String -- combined string representations of all children
    """
    return "\n" + "\n".join([str(child) for child in self.children]) + "\n"
  
  def __repr__(self) -> str:
    """
    Returns:
      String -- complete HTML representation of this element
    """
    attributes_string = self.__get_attribute_string()
    children_string = self.__get_children_string()
    closing = "/>" if len(self.children) == 0 else f">{children_string}</{self.tag}>"
    spacer = " " if len(attributes_string) != 0 else ""
    return f"<{self.tag}{spacer}{attributes_string}{closing}"