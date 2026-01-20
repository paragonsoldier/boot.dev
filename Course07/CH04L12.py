def list_files(parent_directory, current_filepath=""):
  paths = []
  new_path = ""
  for key in parent_directory:
    new_path = f"{current_filepath}/{key}"
    #print(current_filepath)
    if parent_directory[key] == None:
      paths.append(new_path)
    else:
      paths.extend(list_files(parent_directory[key], new_path))
  return paths
