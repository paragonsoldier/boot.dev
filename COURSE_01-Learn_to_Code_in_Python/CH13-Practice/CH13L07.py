def join_strings(strings):
    joined = ""
    for s in strings:
        joined += s + ","
    return joined[:-1]
