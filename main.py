def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = get_word_count(text)
    print(f"{word_count} words found in this file!")

def get_word_count(text):
    words = text.split()
    return len(words)


def get_text(path):
    with open(path) as f:
        return f.read()
    


# Call the main function to execute the program
main()