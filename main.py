def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = get_word_count(text)
    count_letters(text)

#take the text. convert to lowercase. count and pray it drops it out correctly due to being a library
def count_letters(text):
    letter_count = {}

    for letter in text:
        letter = letter.lower() #lowercase babyyyy
        if letter in letter_count:
            letter_count[letter] += 1
        else :
            letter_count[letter] = 1

    print(letter_count)


#takes "text" and splits it by strings aka words. length now gives the amount of strings aka words.
def get_word_count(text):
    words = text.split()
    return len(words)

#getting the book and writing it to "text"
def get_text(path):
    with open(path) as f:
        return f.read()
    



# Call the main function to execute the program
main()