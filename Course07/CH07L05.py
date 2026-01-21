def create_markdown_image(alt_text):
  img = f"![{alt_text}]"
  def add_url(url):
    nonlocal img
    url = url.replace("(", "%28")
    url = url.replace(")", "%29")
    img += f"({url})"
    def add_title(title=None):
      nonlocal img
      if title:
        img = f'{img[:-1]} "{title}")'
      return img
    return add_title
  return add_url

      

