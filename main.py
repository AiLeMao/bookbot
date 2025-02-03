def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = get_word_count(text)
    letter_count = count_letters(text)
    
    
    # Print the report command
    print_report(book_path, word_count, letter_count)




#take the text. convert to lowercase. count and pray it drops it out correctly due to being a library
def count_letters(text):
    letter_count = {}

    for letter in text:
        letter = letter.lower() #lowercase babyyyy
        if letter in letter_count:
            letter_count[letter] += 1
        else :
            letter_count[letter] = 1

    return(letter_count)


# Print the report function content
def print_report(book_path, word_count, letter_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    # Convert the dictionary to a list of dictionaries
    letters_list = [{"char": char, "num": count} for char, count in letter_count.items()]

    # Sort the list by the "num" key in descending order
    letters_list.sort(reverse=True, key=lambda x: x["num"])

    # Print the sorted character counts
    for item in letters_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

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