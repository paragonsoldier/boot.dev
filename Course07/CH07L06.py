def new_resizer(max_width, max_height):
  def set_min_size(min_width=0, min_height=0):
    if min_width > max_width \
    or min_height > max_height:
      raise Exception("minimum size cannot exceed maximum size")
    def resize_image(width, height):
      width = max(width, min_width)
      width = min(width, max_width)
      height = max(height, min_height)
      height = min(height, max_height)
      return width, height
    return resize_image
  return set_min_size

      
