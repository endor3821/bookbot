from stats import get_numb_words, get_numb_symbols

frankenstin = '/home/tim/workspace/github.com/endor3821/bookbot/books/frankenstein.txt'


def main():
    stats = get_numb_words(frankenstin)
    symbals = get_numb_symbols(frankenstin)
    
    print(f'{stats} words found in the document.')
    print(f'{symbals} ') 
main()