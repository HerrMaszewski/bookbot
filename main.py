import os
print("Current working directory:", os.getcwd())


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_word_count(text)
    
    print(f"Number of words: {count}")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    count = len(words)
    return count


main()
