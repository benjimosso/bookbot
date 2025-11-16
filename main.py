import sys
from stats import get_num_words, character_count, sort_dictionary

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    # path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    output = get_num_words(text)
    char_dic = character_count(text)
    sort_report = sort_dictionary(char_dic)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {output} total words")
    print("--------- Character Count -------")
    for i in sort_report:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
    
    
    
    

main()