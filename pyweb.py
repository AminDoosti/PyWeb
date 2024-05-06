import os

def tabber(html) -> str:
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
  def __init__(self) -> None:
    self.head = Element("head")
    self.body = Element("body")

  def __repr__(self) -> str:
    start = "<!DOCTYPE html>\n<html>"
    end = "</html>"
    return f"{start}\n{self.head}\n{self.body}\n{end}"
  
  def export(self, name, ext="html") -> None:
    if not os.path.exists("output"):
      os.mkdir("output")
    
    with open(f"output/{name}.{ext}", "w") as f:
      f.write(tabber(str(self)))


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