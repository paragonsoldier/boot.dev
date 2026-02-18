def count_nested_levels(nested_documents, target_document_id, level=1):
  current_level = level
  target_found_level = -1

  for k,v in nested_documents.items():
    print(k, v, target_document_id, level)
    if k == target_document_id:
      return current_level
      
    result_level = count_nested_levels(v, target_document_id, current_level)
    if result_level != -1:
      target_found_level = result_level

  current_level += 1
  
  return target_found_level
