def file_type_getter(file_extension_tuples):
    extension_dict = {}
    for file_extension_tuple in file_extension_tuples:
        for extension in file_extension_tuple[1]:
            extension_dict[extension] = file_extension_tuple[0]

    return lambda extension: extension_dict.get(extension, "Unknown") 
