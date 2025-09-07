from stats import number_counter

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("./books/frankenstein.txt")
    number_counter(text)
    # print(text)

main()
