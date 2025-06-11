
#book = '/home/tim/workspace/github.com/endor3821/bookbot/books/frankenstein.txt'


def get_book_text(book):
    with open(book) as f:
        text = f.read()
    return text

def get_numb_words(book_path):
    get_text = get_book_text(book_path)
    words = get_text.split()
    numb_words = len(words)

    return numb_words

def get_numb_symbols(book_path):
    get_text = get_book_text(book_path)
    symbols = {}
    for char in get_text:
        if char.isalpha():
            char = char.lower()
            if char in symbols:
                symbols[char] += 1
            else:
                symbols[char] = 1
    return symbols

def sort_on_dict(d):
    sorted_dict = sorted(d.items(), key=lambda item: item[1], reverse=True)
    return sorted_dict
