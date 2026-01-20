def find_longest_word(document, longest_word=""):
  
  split_doc = document.split(maxsplit=1)
  if not split_doc:
    return longest_word
  
  first_word = split_doc[0]
  if len(first_word) > len(longest_word):
    longest_word = first_word

  if len(split_doc) == 1:
    return longest_word

  rest_of_string = split_doc[1]
  return find_longest_word(rest_of_string, longest_word)