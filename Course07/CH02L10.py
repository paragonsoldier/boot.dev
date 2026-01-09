valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line


def pair_document_with_format(doc_names, doc_formats):
  # I didn't catch the `zip` was a predefined function 
  # I originally wrote the solution with my own implementation of zip,
  # which is this commented out section. 
  # zipped_docs = list(map(lambda x: (doc_names[x], doc_formats[x]), range(len(doc_names))))
  # filtered_docs = list(filter(lambda tup: tup[1] in valid_formats, zipped_docs))
  zipped = list(zip(doc_names, doc_formats))
  return list(filter(lambda tup: tup[1] in valid_formats, zipped))