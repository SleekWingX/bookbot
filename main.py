import sys
from stats import get_num_words, generate_sorted_char_list
#example usage = python3 main.py <books/frankenstein.txt>

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Beginning report of {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(filepath)} total words")
    print("--------- Character Count -------")
    for item in generate_sorted_char_list(filepath):
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()