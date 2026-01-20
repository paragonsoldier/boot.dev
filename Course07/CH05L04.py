def doc_format_checker_and_converter(conversion_function, valid_formats):
    def new_function(filename, content):
      if filename.split(".")[1] in valid_formats:
        return conversion_function(content)
      raise ValueError("invalid file format")
    return new_function



# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]
