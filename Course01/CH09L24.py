def filter_messages(messages):
    filtered_messages = []
    dang_count = []
    for message in messages:
        words = message.split()
        good_words = []
        dang_words = []
        for word in words:
            if word == "dang":
                dang_words.append(word)
                continue
            good_words.append(word)
        sentence = " ".join(good_words)
        filtered_messages.append(sentence)
        dang_count.append(len(dang_words))
    return filtered_messages, dang_count
