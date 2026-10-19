def word_count(text: str) -> int:
    str_list = text.split()
    return len(str_list)

def count_characters (text: str) -> dict[str, int]:
    new_text = text.lower()
    text_dict = {}
    for char in new_text:
        if char in text_dict:
            text_dict[char] += 1
        else:
            text_dict[char] = 1
    return text_dict

def sort_on (char: tuple[str, int]) -> int:
    return char[1]

def chars_dict_to_sorted_list (char: dict[str, int]) -> list[tuple[str, int]]:
    char_list = []
    for key in char:
        char_list.append((key, char[key]))
    sorted_char_list = sorted(char_list, reverse = True, key=sort_on)
    return sorted_char_list