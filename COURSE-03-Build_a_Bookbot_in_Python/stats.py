def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    character_counts = {}
    for character in list(text):
        character = character.lower()
        if character in character_counts:
            character_counts[character] += 1
        else: 
            character_counts.setdefault(character, 1)
    return character_counts

def sort_on(items):
    return items["num"]

def sort_by_character_count(character_counts):
    sorted = []
    for char,count in character_counts.items():
        sorted.append({"char": char, "num": count})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

