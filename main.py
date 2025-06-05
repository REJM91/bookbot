import sys
from stats import word_count
from stats import char_count
from stats import sort_char_dict

def get_book_text(filepath):    
    with open(filepath) as file:
        return file.read()

def main():
    """
    Main function to execute the book reading functionality.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]  # Path to the book file
    book_text = get_book_text(filepath)
    count = word_count(book_text)
    sorted_dict = sort_char_dict(char_count(book_text))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    for char, num in sorted_dict:
        print(f"{char}: {num}")
    
    sys.exit(0)  # Exit the program with a status code of 1

main()  # Execute the main function