import sys
from stats import get_num_words, get_num_characters, sort_by_character_count

def get_book_text(file_path):
    with open(file_path) as f:
        return(f.read())

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")

    num_characters = get_num_characters(book_text)
    num_characters = sort_by_character_count(num_characters)
    for i in num_characters:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")

main()