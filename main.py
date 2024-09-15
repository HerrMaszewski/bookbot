import os
print("Current working directory:", os.getcwd())


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    chars_dict = get_character_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    
    print(f"--- Begin raport of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End raport ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

    
def get_word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count


def get_character_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1   
    return chars


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


main()
