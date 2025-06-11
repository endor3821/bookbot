from stats import get_numb_words, get_numb_symbols, sort_on_dict
import sys
import os

frankenstin = '/home/tim/workspace/github.com/endor3821/bookbot/books/frankenstein.txt'


def main():
    
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    if not os.path.exists(path):
        print(f"File not found: {path}")
        sys.exit(1)
    if not path.endswith('.txt'):
        print("Please provide a valid text file.")
        sys.exit(1) 

    stats = get_numb_words(path)
    symbals = get_numb_symbols(path)
    sorted = sort_on_dict(symbals)
    
    print('=============BOOKBOT=============')
    print(f'Analyzing book found at {path}')
    print(f'Found {stats} total words')
    print('--------- Character Count -------')
    for char, count in sorted:
        print(f'{char}: {count}')
    print('===============END=================')   

main()