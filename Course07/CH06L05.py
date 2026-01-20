import copy

def css_styles(initial_styles):
  initial_styles_copy = copy.deepcopy(initial_styles)
  def add_style(selector, property, value):
    if selector not in initial_styles_copy:
      initial_styles_copy[selector] = {}
    initial_styles_copy[selector][property] = value
    return initial_styles_copy
  return add_style





  return add_style
