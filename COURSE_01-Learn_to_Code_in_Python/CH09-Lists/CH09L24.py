def filter_messages(messages):
    filtered_messages = []
    dang_counts = []
    for message in messages:
        words = message.split()
        good_words = []
        dangs = []
        for word in words:
            if word == "dang":
                dangs.append(word)
            else:
                good_words.append(word)
        filtered_messages.append(" ".join(good_words))
        num_dangs = len(dangs)
        dang_counts.append(num_dangs)

    return filtered_messages, dang_counts
