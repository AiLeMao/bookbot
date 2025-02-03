

def main():
    # Define the path to the file
    path_to_file = "books/frankenstein.txt"

    # Open the file and read its contents
    with open(path_to_file) as f:
        file_contents = f.read()

    # Print the contents to the console
    print(file_contents)
    
    # hoping this makes it accessable for the next function
    count_words(file_contents)


#count words here or something bro
def count_words(file_contents):
    words = file_contents.split()
    words_count = len(words)
    print(words_count)


# Call the main function to execute the program
if __name__ == "__main__":
    main()