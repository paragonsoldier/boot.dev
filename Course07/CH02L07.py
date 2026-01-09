import functools


def join(doc_so_far, sentence):
    return f"{doc_so_far} {sentence}."


def join_first_sentences(sentences, n):
    return functools.reduce(join, sentences[1:n], sentences[0] + ".") if n != 0 else ""

