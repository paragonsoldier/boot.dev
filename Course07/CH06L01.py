def word_count_aggregator():
  count = 0
  def calc_num_words(doc):
    nonlocal count
    for word in doc.split():
      count += 1
    return count
  return calc_num_words

