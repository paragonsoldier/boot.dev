def new_collection(initial_docs):
  initial_docs_copy = initial_docs.copy()
  def copy_and_append(s):
    initial_docs_copy.append(s)
    return initial_docs_copy
  return copy_and_append
      

