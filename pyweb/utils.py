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