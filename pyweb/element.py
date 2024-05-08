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
    self.inline = False
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
    out = None
    if self.inline:
      out = "".join([str(child) for child in self.children])
    else:
      out = "\n" + "\n".join([str(child) for child in self.children]) + "\n"
    return out
  
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