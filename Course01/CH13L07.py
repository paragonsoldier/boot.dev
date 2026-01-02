def join_strings(strings):
    joined_string = ""
    for string in strings:
        joined_string += string + ","
    return joined_string[:-1]
