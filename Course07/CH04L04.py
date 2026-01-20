def zipmap(keys, values):
  zipped = {}
  if len(keys) == 0 or len(values) == 0:
    return {}
  zipped.update(zipmap(keys[1:], values[1:]))
  zipped[keys[0]] = values[0]
  return zipped