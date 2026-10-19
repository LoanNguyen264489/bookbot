import sys
from stats import word_count, count_characters, chars_dict_to_sorted_list

def main() -> None:
   if len(sys.argv) < 2:
       print('Usage: python3 main.py <path_to_book>')
       sys.exit(1)
   path = sys.argv[1]
   book = get_book_text(path)
   num_words = word_count(book)
   char_dict = count_characters(book)
   char_list = chars_dict_to_sorted_list(char_dict)
   print_report(path, num_words, char_list)


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def print_report(path: str, word_count: int, sorted_list :list[tuple[str, int]]) -> None:
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for character, count in sorted_list:
          if character.isalpha():
              print(f'{character}: {count}')   
    print('============= END ===============')

main()