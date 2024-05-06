import os

class Page:
  def __init__(self) -> None:
    self.elements = list()

  def add(self, *elements) -> None:
    for element in elements:
      self.elements.append(element)

  def __repr__(self) -> str:
    return "\n".join([str(elem) for elem in self.elements])
  
  def export(self, name, ext="html"):
    if not os.path.exists("output"):
      os.mkdir("output")
    
    with open(f"output/{name}.{ext}", "w") as f:
      f.write(str(self))


class Element:
  def __init__(self, tag, children=None, attrs=dict()) -> None:
    self.props = attrs
    self.tag = tag
    self.children = children if children != None else []

  def setAttr(self, attr, val) -> None:
    self.props[attr] = val

  def setCSS(self, CSS) -> None:
    self.props["style"] = CSS

  def add(self, *elements) -> None:
    for element in elements:
      self.children.append(element)

  def __get_attribute_string(self) -> str:
    return " ".join([f"{attr}=\"{val}\"" for (attr, val) in self.props.items()])
  
  def __get_children_string(self) -> str:
    return "\n" + "\n".join([str(child) for child in self.children]) + "\n"
  
  def __repr__(self) -> str:
    attributes_string = self.__get_attribute_string()
    children_string = self.__get_children_string()
    closing = "/>" if len(self.children) == 0 else f">{children_string}</{self.tag}>"
    spacer = " " if len(attributes_string) != 0 else ""
    return f"<{self.tag}{spacer}{attributes_string}{closing}"