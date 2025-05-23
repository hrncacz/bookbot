from stats import count_words, count_letters
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        full_book = get_book_text(sys.argv[1])
        letters = count_letters(full_book)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print(f'Found {count_words(full_book)} total words')
        print("--------- Character Count -------")
        for i in letters:
            print(f"{i}: {letters[i]}")
        print("============= END ===============")


main()
