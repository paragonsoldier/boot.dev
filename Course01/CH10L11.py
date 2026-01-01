def merge(dict1, dict2):
    merged_dict = {}
    for key in dict1:
        value = dict1[key]
        merged_dict[key] = value
    for key in dict2:
        value = dict2[key]
        merged_dict[key] = value
    return merged_dict
