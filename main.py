from stats import (
    word_counter,
    character_sort,
    sort_by_count
)

import sys

def get_book_path():
    if len(sys.argv) < 2:
        print("Bookbot Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]


def main():
    book_path = get_book_path() 
    text = get_book_text(book_path)
    num_words = word_counter(text)
    char_dict = character_sort(text)
    sorted_dicts = sort_by_count(char_dict)
    print_formatter(book_path, num_words, sorted_dicts)
    

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    

def print_formatter(book_path, num_words, sorted_dicts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_dicts:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
    
    
main()
