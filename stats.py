def get_num_words(text):
    words = text.split()
    return len(words)


def count_characters(book_text: str) -> int:
    """Counts the number of characters in the book text."""
    count_dict = {}
    for char in book_text:
        char = char.lower()
        count_dict[char] = count_dict.get(char, 0) + 1
    return count_dict


def sort_characters_by_frequency(count_dict):
    """Sorts characters by frequency in descending order."""
    return sorted(count_dict.items(), key=lambda item: item[1], reverse=True)
