def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    num_characters = count_characters(text)
    getReport = return_report(count_characters(text))
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(words):
    charNums = {}
    for char in words.lower():
       charNums[char] = charNums.get(char, 0) + 1
    return charNums

def return_report(dictionary):
    char_list = list(dictionary.items())
    sorted_chars = sorted(char_list, key=lambda x:x[1], reverse=True)

    for char_tuple in sorted_chars:
        char = char_tuple[0]
        count = char_tuple[1]
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")


main()
