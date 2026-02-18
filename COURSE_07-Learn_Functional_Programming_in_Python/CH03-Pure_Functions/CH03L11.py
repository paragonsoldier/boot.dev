def remove_emphasis(doc):
    lines = doc.split("\n")
    new_lines = map(remove_line_emphasis, lines)
    return "\n".join(new_lines)


# Don't touch below this line


def remove_line_emphasis(line):
    words = line.split()
    new_words = map(remove_word_emphasis, words)
    return " ".join(new_words)


def remove_word_emphasis(word):
    return word.strip("*")
