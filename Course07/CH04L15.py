def count_nested_levels(nested_documents, target_document_id, level=1):
  for k, v in nested_documents.items():
    if k == target_document_id:
      return level
    else:
      next_level = count_nested_levels(v, target_document_id, level + 1)
      if next_level != -1:
        return next_level
  return -1
  
  


