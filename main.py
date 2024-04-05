def read_book(book_text):
    return print(book_text)

def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_letters(book_text):
    lowercase_book = book_text.lower()
    word_dict = {}
    letters = list(map(chr, range(97, 123)))
    for w in lowercase_book:
        if w in letters:
            if w not in word_dict:
                word_dict[w] = 1
            else:
                word_dict[w] += 1
    sorted_keys = list(word_dict.keys())
    sorted_keys.sort()
    return {i : word_dict[i] for i in sorted_keys}

def report(book_text, book_file):
    report_str = f"--- Begin report of {book_file} ---\n"
    report_str += f"{count_words(book_text)} words found in the document\n\n"
    letters = count_letters(book_text)
    for w in letters.keys():
        report_str += f"The '{str(w)}' character was found {int(letters[w])} times\n"
    report_str += "--- End report ---"
    return report_str

if __name__ == "__main__":
    book_path = "books/frankenstein.txt" 
    book_text = ""
    with open(book_path) as f:
        book_text = f.read()

    read_book(book_text)
    print(count_words(book_text))
    print(count_letters(book_text))
    print(report(book_text, book_path))


