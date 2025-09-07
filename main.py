from stats import number_counter, character_counter, sorting_values
import sys

def get_book_text(filepath):
    # Read as UTF-8; adjust errors handling if you have mixed encodings
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def main():
    # Require exactly one argument: the path to the book file
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: file not found -> {book_path}")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: could not decode file as UTF-8 -> {book_path}")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    number_counter(text)

    print("--------- Character Count -------")
    count_text = character_counter(text)
    sorted_list = sorting_values(count_text)

    for entry in sorted_list:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()