def count_vowels(text):
    vowels = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
    count = 0
    unique_vowels = set()
    for char in text: 
        if char in vowels:
            count += 1
            unique_vowels.add(char)
    return count, unique_vowels
