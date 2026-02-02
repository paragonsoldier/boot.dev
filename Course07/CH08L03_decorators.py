def configure_plugin_decorator(func):
  def wrapper_func(*args):
    converted = dict(args)
    return func(**converted)
  return wrapper_func