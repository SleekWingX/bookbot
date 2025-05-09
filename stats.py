def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_character_count(filepath):
    book_text = get_book_text(filepath)
    book_text_lower = book_text.lower()
    counts = {}
    for char in book_text_lower:
        counts[char] = counts.get(char, 0) + 1
    return counts

def get_num_words(filepath):
    book_text = get_book_text(filepath)
    words = book_text.split()
    total_words = len(words)
    return total_words

def generate_sorted_char_list(filepath):
    sorted_char_list = []
    for char, count in get_character_count(filepath).items():
        if char.isalpha():
            sorted_char_list.append({"char": char, "num": count})
    def sort_on(dict):
        return dict["num"]
    counts = sorted_char_list
    counts.sort(reverse=True, key=sort_on)
    return counts



