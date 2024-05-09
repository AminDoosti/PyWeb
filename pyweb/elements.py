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
    """
    self.url = url
    super().__init__("a", [text], {"href": url} | attrs)
    self.inline = True
  
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
    """
    Required arguments:
      (1) text -- the abbreviated text
      (2) title -- the full version of the abbreviated text
    """
    super().__init__("abbr", [text], {"title": title})
    self.inline = True

class Article(Element):
  """
  Info:
    Sets up the HTML <article> element
  """
  def __init__(self, children=None) -> None:
    """
    Optional arguments:
      (1) children -- initializes children on creation
    """
    super().__init__("article", children, {})

class Aside(Element):
  """
  Info:
    Sets up the HTML <aside> element
  """
  def __init__(self, children=None) -> None:
    """
    Optional arguments:
      (1) children -- initializes children on creation
    """
    super().__init__("aside", children, {})

class Bold(Element):
  """
  Info:
    Sets up the HTML <b> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- text that needs to be bolded
    """
    super().__init__("b", [text], {})
    self.inline = True

class BDI(Element):
  """
  Info:
    Sets up the HTML <bdi> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- text that requires bi-directional isolation
    """
    super().__init__("bdi", [text], {})
    self.inline = True

class BDO(Element):
  """
  Info:
    Sets up the HTML <bdo> element
  """
  def __init__(self, text, direction="rtl") -> None:
    """
    Required arguments:
      (1) text -- text that needs to be directionally overwritten
    Optional arguments:
      (1) dir -- direction of the text, either "rtl" or "ltr"
    """
    super().__init__("bdo", [text], {"dir": direction})

class BlockQuote(Element):
  """
  Info:
    Sets up the HTML <blockquote> element
  """
  def __init__(self, quote, source=None) -> None:
    """
    Required arguments:
      (1) quote -- text that is being quoted
    Optional arguments:
      (1) source -- source of the quotation
    """
    super().__init__("blockquote", [quote], {} if not source else {"cite": source})

class LineBreak(Element):
  """
  Info:
    Sets up the HTML <br> element
  """
  def __init__(self) -> None:
    """
    """
    super().__init__("br", [], {})

class Button(Element):
  """
  Info:
    Sets up the HTML <button> element
  """
  def __init__(self, text, type="button") -> None:
    """
    Required arguments:
      (1) text -- written text on the button
    Optional arguments:
      (1) tyoe -- type of button
    """
    super().__init__("button", [text], {"type": type})
    self.inline = True

class Canvas(Element):
  """
  Info:
    Sets up the HTML <canvas> element
  """
  def __init__(self) -> None:
    """
    """
    support_warning = "Your browser does not support the HTML canvas element."
    super().__init__("canvas", [support_warning], {})

class Cite(Element):
  """
  Info:
    Sets up the HTML <cite> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- citation text
    """
    super().__init__("cite", [text], {})
    self.inline = True

class Code(Element):
  """
  Info:
    Sets up the HTML <code> element
  """
  def __init__(self, code) -> None:
    """
    Required arguments:
      (1) code -- text that needs code representation 
    """
    super().__init__("code", [code], {})
    self.inline = True

class Data(Element):
  """
  Info:
    Sets up the HTML <data> element
  """
  def __init__(self, text, value) -> None:
    """
    Required arguments:
      (1) text -- text within the element
      (2) value -- value of the data element
    """
    super().__init__("data", [text], {"value": value})
    self.inline = True

class Del(Element):
  """
  Info:
    Sets up the HTML <del> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- text that is being deleted
    """
    super().__init__("del", [text], {})
    self.inline = True

class DFN(Element):
  """
  Info:
    Sets up the HTML <dfn> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- text that is being defined
    """
    super().__init__("dfn", [text], {})
    self.inline = True

class Div(Element):
  """
  Info:
    Sets up the HTML <div> element
  """
  def __init__(self, children=None) -> None:
    """
    Optional arguments:
      (1) children -- initializes children on creation
    """
    super().__init__("div", children, {})

class Emph(Element):
  """
  Info:
    Sets up the HTML <em> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- text that needs emphasizing
    """
    super().__init__("em", [text], {})
    self.inline = True

class Footer(Element):
  """
  Info:
    Sets up the HTML <footer> element
  """
  def __init__(self, children=None) -> None:
    """
    Optional arguments:
      (1) children -- initializes children on creation
    """
    super().__init__("footer", children, {})

class H1(Element):
  """
  Info:
    Sets up the HTML <h1> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- text within the heading element
    """
    super().__init__("h1", [text], {})
    self.inline = True

class H2(Element):
  """
  Info:
    Sets up the HTML <h2> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- text within the heading element
    """
    super().__init__("h2", [text], {})
    self.inline = True

class H3(Element):
  """
  Info:
    Sets up the HTML <h3> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- text within the heading element
    """
    super().__init__("h3", [text], {})
    self.inline = True

class H4(Element):
  """
  Info:
    Sets up the HTML <h4> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- text within the heading element
    """
    super().__init__("h4", [text], {})
    self.inline = True

class H5(Element):
  """
  Info:
    Sets up the HTML <h5> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- text within the heading element
    """
    super().__init__("h5", [text], {})
    self.inline = True

class H6(Element):
  """
  Info:
    Sets up the HTML <h6> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- text within the heading element
    """
    super().__init__("h6", [text], {})
    self.inline = True

class Header(Element):
  """
  Info:
    Sets up the HTML <header> element
  """
  def __init__(self, children=None) -> None:
    """
    Optional arguments:
      (1) children -- initializes children on creation
    """
    super().__init__("header", children, {})

class HR(Element):
  """
  Info:
    Sets up the HTML <hr> element
  """
  def __init__(self) -> None:
    """
    """
    super().__init__("hr", [], {})
    self.inline = True

class Italic(Element):
  """
  Info:
    Sets up the HTML <i> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- text that needs to be italisized
    """
    super().__init__("i", [text], {})
    self.inline = True

class Image(Element):
  """
  Info:
    Sets up the HTML <img> element
  """
  def __init__(self, src, alt=None, width=None, height=None, attrs=dict()) -> None:
    """
    Required arguments:
      (1) src -- source path of the image
    Optional arguments:
      (1) alt -- alternate text
      (2) width -- width of image
      (3) height -- height of image
      (4) attrs -- dictionary of all other attributes
    """
    formatted_src = src
    if not (src.startswith("/") or src.startswith("./") or src.startswith("../")):
      formatted_src = "/" + src

    self._fixed_attributes = {"src": formatted_src}
    if alt: self._fixed_attributes = self._fixed_attributes | {"alt": alt}
    if width: self._fixed_attributes = self._fixed_attributes | {"width": width}
    if height: self._fixed_attributes = self._fixed_attributes | {"height": height}
    super().__init__("img", [], self._fixed_attributes | attrs)
    self.inline = True
  
  def set_attr(self, attrs) -> None:
    """
    Info:
      Prevents user from overwriting the "href" attribute.
      Refer to Element's comment for more info.
    """
    return super().set_attr(self._fixed_attributes | attrs)

class Ins(Element):
  """
  Info:
    Sets up the HTML <ins> element
  """
  def __init__(self, text, cite=None, datetime=None) -> None:
    """
    Required arguments:
      (1) text -- text that needs to be inserted
    """
    fixed_attrs = {}
    if cite: fixed_attrs = fixed_attrs | {"cite": cite}
    if datetime: fixed_attrs = fixed_attrs | {"datetime": datetime}
    super().__init__("ins", [text], fixed_attrs)
    self.inline = True

class Main(Element):
  """
  Info:
    Sets up the HTML <main> element
  """
  def __init__(self, children=None) -> None:
    """
    Optional arguments:
      (1) children -- initializes children on creation
    """
    super().__init__("main", children, {})

class Mark(Element):
  """
  Info:
    Sets up the HTML <mark> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- text that needs to be highlighted
    """
    super().__init__("mark", [text], {})

class Nav(Element):
  """
  Info:
    Sets up the HTML <nav> element
  """
  def __init__(self, children=None) -> None:
    """
    Optional arguments:
      (1) children -- initializes children on creation
    """
    super().__init__("nav", children, {})

class Paragraph(Element):
  """
  Info:
    Sets up the HTML <p> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- paragraph text
    """
    super().__init__("p", [text], {})

class Quote(Element):
  """
  Info:
    Sets up the HTML <q> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- text that needs to be quoted
    """
    super().__init__("q", [text], {})
    self.inline = True

class Section(Element):
  """
  Info:
    Sets up the HTML <section> element
  """
  def __init__(self, children=None) -> None:
    """
    Optional arguments:
      (1) children -- initializes children on creation
    """
    super().__init__("section", children, {})

class Text(Element):
  """
  Info:
    Sets up the HTML <span> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- initialized text
    """
    super().__init__("span", [text], {})

class Strong(Element):
  """
  Info:
    Sets up the HTML <strong> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- text that needs to be strong
    """
    super().__init__("strong", [text], {})
    self.inline = True

class Subscript(Element):
  """
  Info:
    Sets up the HTML <sub> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- text that needs to be subscripted
    """
    super().__init__("sub", [text], {})
    self.inline = True

class Superscript(Element):
  """
  Info:
    Sets up the HTML <sup> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- text that needs to be superscripted
    """
    super().__init__("sup", [text], {})
    self.inline = True

class Time(Element):
  """
  Info:
    Sets up the HTML <time> element
  """
  def __init__(self, text, datetime=None) -> None:
    """
    Required arguments:
      (1) text -- text wrapped in time
    Optional arguments:
      (1) datetime -- date and time associated with the element
    """
    super().__init__("time", [text], {} if not datetime else {"datetime": datetime})
    self.inline = True

class Underline(Element):
  """
  Info:
    Sets up the HTML <u> element
  """
  def __init__(self, text) -> None:
    """
    Required arguments:
      (1) text -- text that needs to be underlined
    """
    super().__init__("u", [text], {})
    self.inline = True

class WordBreak(Element):
  """
  Info:
    Sets up the HTML <wbr> element
  """
  def __init__(self) -> None:
    super().__init__("wbr", [], {})
