import sys
from stats import count, get_character_counts, sorting_line

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    print(f"Length of sys.argv: {len(sys.argv)}")
    print(f"sys.argv contents: {sys.argv}")

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)

    print(f"First 50 chars: {text[:50]}")

    final_count = count(text)
    char_counts = get_character_counts(text)
    sorted_char_list = sorting_line(char_counts)

    print(f"{final_count} words found in the document")
    print(f"{char_counts}")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {final_count} total words")
    print("--------- Character Count -------")

    for sorted_char in sorted_char_list:
        print(f"{sorted_char['char']}: {sorted_char['num']}")

    print("============= END ===============")

main()
