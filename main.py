import sys
from stats import get_num_words, count_characters, sort_characters_by_frequency


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_count = count_characters(text)
    sorted_char_count = sort_characters_by_frequency(char_count)
    for key, value in sorted_char_count:
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
# This function counts the number of words in a given text.
